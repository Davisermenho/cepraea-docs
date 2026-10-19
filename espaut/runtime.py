#!/usr/bin/env python3
"""Stable ESPAUT runtime deployment, verification, update, and rollback.

The active hook path is a stable symlink. Releases are immutable directories
with a hash manifest, so an update never executes from a temporary Git clone.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

from espaut import __version__


LAYOUT_VERSION = 1
ESPAUT_MARKERS = (
    "ESPAUT-GLOBAL-HOOKS",
    "espaut/ide_hook.py",
    "espaut\\ide_hook.py",
    "espaut-runtime/current/espaut/runtime_hook.py",
)


class RuntimeDeploymentError(RuntimeError):
    """Deployment or integrity validation failed."""


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_json(path: Path, value: Any, mode: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        if mode is not None:
            os.chmod(tmp, mode)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def _atomic_bytes(path: Path, value: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp, mode)
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def _release_name(version: str, implementation_sha: str) -> str:
    if not re.fullmatch(r"[0-9A-Za-z][0-9A-Za-z._-]{0,63}", version):
        raise RuntimeDeploymentError("invalid release version")
    if not re.fullmatch(r"[0-9a-f]{7,64}", implementation_sha):
        raise RuntimeDeploymentError("implementation SHA must be a hexadecimal Git SHA")
    return f"{version}-{implementation_sha[:12]}"


def _source_files(source_root: Path) -> list[Path]:
    package = source_root / "espaut"
    schemas = source_root / "schemas"
    if not (package / "runtime_hook.py").is_file():
        raise RuntimeDeploymentError("runtime_hook.py is missing from source")
    files = sorted(p for p in package.rglob("*.py") if "__pycache__" not in p.parts)
    if schemas.is_dir():
        files.extend(sorted(schemas.glob("*.json")))
    return files


def _copy_release(source_root: Path, destination: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for source in _source_files(source_root):
        relative = source.relative_to(source_root)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        hashes[relative.as_posix()] = _sha256(target)
    return hashes


def verify_release(release: Path) -> dict[str, Any]:
    manifest_path = release / "release-manifest.json"
    if not manifest_path.is_file():
        return {"status": "invalid", "reason": "manifest missing"}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"status": "invalid", "reason": "manifest unreadable"}
    mismatches = []
    for relative, expected in manifest.get("files", {}).items():
        candidate = release / relative
        if not candidate.is_file() or _sha256(candidate) != expected:
            mismatches.append(relative)
    return {
        "status": "verified" if not mismatches else "invalid",
        "mismatches": mismatches,
        "manifest": manifest,
    }


def _run_validation(source_root: Path, command: list[str] | None) -> dict[str, Any]:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    commands = [command] if command else [
        [sys.executable, "-B", str(test.relative_to(source_root))]
        for test in sorted((source_root / "tests" / "espaut").glob("test_*.py"))
    ]
    if not commands:
        return {"commands": [], "exit_code": 1, "reason": "no validation tests found"}
    stdout = []
    stderr = []
    exit_code = 0
    for argv in commands:
        result = subprocess.run(
            argv, cwd=source_root, env=environment, capture_output=True, text=True,
            timeout=300, check=False,
        )
        stdout.append(result.stdout)
        stderr.append(result.stderr)
        if result.returncode != 0:
            exit_code = result.returncode
            break
    return {
        "commands": commands,
        "exit_code": exit_code,
        "stdout_sha256": hashlib.sha256("".join(stdout).encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256("".join(stderr).encode()).hexdigest(),
    }


def _verify_source_revision(source_root: Path, implementation_sha: str) -> None:
    """Require the deployment source to be the exact clean Git revision."""
    head = subprocess.run(
        ["git", "-C", str(source_root), "rev-parse", "HEAD"],
        capture_output=True, text=True, timeout=20, check=False,
    )
    if head.returncode != 0 or head.stdout.strip() != implementation_sha:
        raise RuntimeDeploymentError("source checkout does not match implementation SHA")
    status = subprocess.run(
        ["git", "-C", str(source_root), "status", "--porcelain=v1", "--untracked-files=all"],
        capture_output=True, text=True, timeout=20, check=False,
    )
    if status.returncode != 0 or status.stdout:
        raise RuntimeDeploymentError("source checkout is not clean; immutable release required")


def deploy_runtime(
    source_root: Path,
    runtime_root: Path,
    *,
    implementation_sha: str,
    version: str = __version__,
    validation_command: list[str] | None = None,
) -> dict[str, Any]:
    """Validate, stage, and atomically activate an immutable release."""
    source_root = source_root.resolve()
    runtime_root = runtime_root.resolve()
    release_name = _release_name(version, implementation_sha)
    _verify_source_revision(source_root, implementation_sha)
    validation = _run_validation(source_root, validation_command)
    if validation["exit_code"] != 0:
        raise RuntimeDeploymentError("source validation failed; active runtime unchanged")

    versions = runtime_root / "versions"
    staging = runtime_root / "staging"
    versions.mkdir(parents=True, exist_ok=True)
    staging.mkdir(parents=True, exist_ok=True)
    runtime_root.joinpath("state").mkdir(parents=True, exist_ok=True, mode=0o700)
    stage = Path(tempfile.mkdtemp(prefix=f"{release_name}.", dir=staging))
    try:
        hashes = _copy_release(source_root, stage)
        manifest = {
            "layout_version": LAYOUT_VERSION,
            "version": version,
            "implementation_sha": implementation_sha,
            "release": release_name,
            "created_at": _now(),
            "source_root": str(source_root),
            "files": hashes,
            "validation": validation,
        }
        _atomic_json(stage / "release-manifest.json", manifest, 0o600)
        smoke_env = os.environ.copy()
        smoke_env["PYTHONPATH"] = str(stage)
        smoke_env["PYTHONDONTWRITEBYTECODE"] = "1"
        smoke = subprocess.run(
            [sys.executable, "-B", "-c",
             "from espaut import __version__; from espaut.runtime_hook import parse_args; print(__version__)"],
            env=smoke_env, capture_output=True, text=True, timeout=30, check=False,
        )
        if smoke.returncode != 0 or smoke.stdout.strip() != version:
            raise RuntimeDeploymentError("staged runtime smoke test failed")
        target = versions / release_name
        if target.exists():
            existing = verify_release(target)
            if existing.get("status") != "verified" or existing["manifest"].get("files") != hashes:
                raise RuntimeDeploymentError("release name already exists with different content")
            shutil.rmtree(stage)
        else:
            os.replace(stage, target)

        current = runtime_root / "current"
        previous = os.readlink(current) if current.is_symlink() else None
        next_link = runtime_root / ".current.next"
        next_link.unlink(missing_ok=True)
        os.symlink(os.path.relpath(target, runtime_root), next_link)
        os.replace(next_link, current)
        active = {
            **manifest,
            "activated_at": _now(),
            "previous_release": previous,
            "active_path": str(target),
        }
        _atomic_json(runtime_root / "active-manifest.json", active, 0o600)
        history_path = runtime_root / "activation-history.json"
        history = []
        if history_path.is_file():
            history = json.loads(history_path.read_text(encoding="utf-8"))
        history.append({
            "activated_at": active["activated_at"],
            "release": release_name,
            "previous_release": previous,
            "implementation_sha": implementation_sha,
        })
        _atomic_json(history_path, history, 0o600)
        return {"status": "activated", "release": release_name, "previous_release": previous}
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def rollback_runtime(runtime_root: Path) -> dict[str, Any]:
    """Atomically reactivate the immediately previous verified release."""
    runtime_root = runtime_root.resolve()
    active_path = runtime_root / "active-manifest.json"
    if not active_path.is_file():
        raise RuntimeDeploymentError("active runtime manifest missing")
    active = json.loads(active_path.read_text(encoding="utf-8"))
    previous = active.get("previous_release")
    if not previous:
        raise RuntimeDeploymentError("no previous release available")
    target = (runtime_root / previous).resolve()
    versions = (runtime_root / "versions").resolve()
    if versions not in target.parents or verify_release(target).get("status") != "verified":
        raise RuntimeDeploymentError("previous release failed integrity verification")
    current = runtime_root / "current"
    next_link = runtime_root / ".current.next"
    next_link.unlink(missing_ok=True)
    os.symlink(os.path.relpath(target, runtime_root), next_link)
    os.replace(next_link, current)
    manifest = verify_release(target)["manifest"]
    _atomic_json(runtime_root / "active-manifest.json", {
        **manifest,
        "activated_at": _now(),
        "previous_release": f"versions/{active['release']}",
        "active_path": str(target),
        "rollback_from": active["release"],
    }, 0o600)
    return {"status": "rolled_back", "release": manifest["release"], "from": active["release"]}


def hook_command(runtime_root: Path, provider: str, phase: str) -> str:
    script = runtime_root.resolve() / "current" / "espaut" / "runtime_hook.py"
    return f'/usr/bin/python3 -B "{script}" --provider {provider} --phase {phase}'


def _is_espaut_handler(handler: dict[str, Any]) -> bool:
    command = str(handler.get("command", ""))
    return any(marker in command for marker in ESPAUT_MARKERS)


def install_hook_config(path: Path, runtime_root: Path, provider: str) -> dict[str, Any]:
    """Replace only ESPAUT handlers, preserving every third-party setting."""
    path = path.resolve()
    original = path.read_bytes() if path.is_file() else b"{}\n"
    try:
        config = json.loads(original.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise RuntimeDeploymentError(f"invalid hook config: {path}") from exc
    if not isinstance(config, dict):
        raise RuntimeDeploymentError(f"hook config must be an object: {path}")
    hooks = config.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise RuntimeDeploymentError(f"hooks must be an object: {path}")
    removed = 0
    for event, groups in list(hooks.items()):
        if not isinstance(groups, list):
            continue
        retained_groups = []
        for group in groups:
            if not isinstance(group, dict) or not isinstance(group.get("hooks"), list):
                retained_groups.append(group)
                continue
            retained_handlers = [h for h in group["hooks"] if not (isinstance(h, dict) and _is_espaut_handler(h))]
            removed += len(group["hooks"]) - len(retained_handlers)
            if retained_handlers:
                retained_groups.append({**group, "hooks": retained_handlers})
        hooks[event] = retained_groups
    for event, phase in (("UserPromptSubmit", "pre"), ("Stop", "post")):
        hooks.setdefault(event, []).append({
            "hooks": [{
                "type": "command",
                "command": hook_command(runtime_root, provider, phase),
                "timeout": 15,
                "statusMessage": "ESPAUT: registrando ciclo seguro",
            }]
        })

    backup_dir = runtime_root.resolve() / "backups" / "hook-configs"
    backup_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = backup_dir / f"{provider}-{stamp}-{hashlib.sha256(original).hexdigest()[:12]}.json"
    backup.write_bytes(original)
    os.chmod(backup, 0o600)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o600
    _atomic_json(path, config, mode)
    return {"status": "installed", "path": str(path), "backup": str(backup), "removed": removed}


def deploy_and_install(
    source_root: Path,
    runtime_root: Path,
    *,
    implementation_sha: str,
    version: str = __version__,
    hook_configs: dict[str, Path] | None = None,
) -> dict[str, Any]:
    """Deploy code and hook configs as one recoverable activation."""
    runtime_root = runtime_root.resolve()
    current = runtime_root / "current"
    active_path = runtime_root / "active-manifest.json"
    previous_link = os.readlink(current) if current.is_symlink() else None
    previous_active = active_path.read_bytes() if active_path.is_file() else None
    originals: dict[str, tuple[Path, bytes | None, int]] = {}
    for provider, config_path in (hook_configs or {}).items():
        resolved = config_path.resolve()
        originals[provider] = (
            resolved,
            resolved.read_bytes() if resolved.is_file() else None,
            resolved.stat().st_mode & 0o777 if resolved.exists() else 0o600,
        )
    result = deploy_runtime(
        source_root, runtime_root,
        implementation_sha=implementation_sha, version=version,
    )
    installed: dict[str, Any] = {}
    try:
        for provider, (path, _, _) in originals.items():
            installed[provider] = install_hook_config(path, runtime_root, provider)
    except Exception:
        for path, content, mode in originals.values():
            if content is None:
                path.unlink(missing_ok=True)
            else:
                _atomic_bytes(path, content, mode)
        replacement = runtime_root / ".current.recover"
        replacement.unlink(missing_ok=True)
        if previous_link is None:
            current.unlink(missing_ok=True)
        else:
            os.symlink(previous_link, replacement)
            os.replace(replacement, current)
        if previous_active is None:
            active_path.unlink(missing_ok=True)
        else:
            _atomic_bytes(active_path, previous_active, 0o600)
        raise
    result["hook_configs"] = installed
    return result


def runtime_status(runtime_root: Path, hook_configs: dict[str, Path] | None = None) -> dict[str, Any]:
    runtime_root = runtime_root.resolve()
    current = runtime_root / "current"
    if not current.is_symlink():
        return {"status": "not_installed", "runtime_root": str(runtime_root)}
    target = current.resolve()
    verification = verify_release(target)
    result: dict[str, Any] = {
        "status": "active" if verification.get("status") == "verified" else "invalid",
        "runtime_root": str(runtime_root),
        "active_path": str(target),
        "release": verification.get("manifest", {}).get("release"),
        "version": verification.get("manifest", {}).get("version"),
        "implementation_sha": verification.get("manifest", {}).get("implementation_sha"),
        "integrity": verification.get("status"),
    }
    if hook_configs:
        installed = {}
        for provider, path in hook_configs.items():
            commands: set[str] = set()
            if path.is_file():
                try:
                    config = json.loads(path.read_text(encoding="utf-8"))
                    for groups in config.get("hooks", {}).values():
                        for group in groups if isinstance(groups, list) else []:
                            for handler in group.get("hooks", []) if isinstance(group, dict) else []:
                                if isinstance(handler, dict) and isinstance(handler.get("command"), str):
                                    commands.add(handler["command"])
                except (OSError, ValueError, AttributeError):
                    commands = set()
            installed[provider] = all(
                hook_command(runtime_root, provider, phase) in commands
                for phase in ("pre", "post")
            )
        result["hooks"] = installed
        if not all(installed.values()):
            result["status"] = "invalid"
    return result


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="python -m espaut.runtime")
    parser.add_argument("--runtime-root", type=Path, required=True)
    sub = parser.add_subparsers(dest="command", required=True)
    deploy = sub.add_parser("deploy")
    deploy.add_argument("--source", type=Path, required=True)
    deploy.add_argument("--implementation-sha", required=True)
    deploy.add_argument("--version", default=__version__)
    deploy.add_argument("--claude-settings", type=Path)
    deploy.add_argument("--codex-hooks", type=Path)
    sub.add_parser("status")
    sub.add_parser("rollback")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.command == "deploy":
            configs = {}
            if args.claude_settings:
                configs["claude"] = args.claude_settings
            if args.codex_hooks:
                configs["codex"] = args.codex_hooks
            result = deploy_and_install(
                args.source, args.runtime_root,
                implementation_sha=args.implementation_sha,
                version=args.version,
                hook_configs=configs,
            )
        elif args.command == "rollback":
            result = rollback_runtime(args.runtime_root)
        else:
            result = runtime_status(args.runtime_root)
    except (OSError, ValueError, RuntimeDeploymentError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
