#!/usr/bin/env python3
"""U01 corpus inventory using only the Python standard library.

The source tree is opened for reading only. All generated files are written to
an explicitly separate output directory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import stat
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "1.0.0"
CHUNK_SIZE = 1024 * 1024

FORMAT_BY_EXTENSION = {
    ".md": ("Markdown", "text/markdown", "SUPPORTED"),
    ".txt": ("Plain text", "text/plain", "SUPPORTED"),
    ".sql": ("SQL", "application/sql", "SUPPORTED"),
    ".json": ("JSON", "application/json", "SUPPORTED"),
    ".yaml": ("YAML", "application/yaml", "SUPPORTED"),
    ".yml": ("YAML", "application/yaml", "SUPPORTED"),
    ".pdf": ("PDF", "application/pdf", "SUPPORTED"),
    ".pptx": (
        "PowerPoint Open XML",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "SUPPORTED",
    ),
}


def json_dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=False)
        handle.write("\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def files_equal(left: Path, right: Path) -> bool:
    if left.stat().st_size != right.stat().st_size:
        return False
    with left.open("rb") as first, right.open("rb") as second:
        while True:
            first_chunk = first.read(CHUNK_SIZE)
            second_chunk = second.read(CHUNK_SIZE)
            if first_chunk != second_chunk:
                return False
            if not first_chunk:
                return True


def looks_like_utf8_text(path: Path) -> bool:
    with path.open("rb") as handle:
        sample = handle.read(64 * 1024)
    if b"\x00" in sample:
        return False
    try:
        sample.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return True


def identify_format(path: Path) -> dict[str, str]:
    extension = path.suffix.lower()
    known = FORMAT_BY_EXTENSION.get(extension)
    if known:
        name, media_type, support = known
        return {
            "extension": extension,
            "format": name,
            "media_type": media_type,
            "format_status": support,
        }
    try:
        if looks_like_utf8_text(path):
            return {
                "extension": extension,
                "format": "Plain text (detected)",
                "media_type": "text/plain",
                "format_status": "SUPPORTED",
            }
    except OSError:
        pass
    return {
        "extension": extension,
        "format": "Unknown binary",
        "media_type": "application/octet-stream",
        "format_status": "PENDING",
    }


def validate_format(path: Path, format_name: str) -> tuple[str, str | None]:
    """Perform lightweight structural checks, without extracting content."""
    try:
        if format_name in {"Markdown", "Plain text", "Plain text (detected)", "SQL"}:
            path.read_text(encoding="utf-8")
            return "PASS", None
        if format_name == "JSON":
            with path.open("r", encoding="utf-8") as handle:
                json.load(handle)
            return "PASS", None
        if format_name == "PDF":
            with path.open("rb") as handle:
                if handle.read(5) != b"%PDF-":
                    return "FAIL", "PDF_HEADER_MISSING"
            return "PASS", None
        if format_name == "PowerPoint Open XML":
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                required = {"[Content_Types].xml", "ppt/presentation.xml"}
                missing = sorted(required - names)
                if missing:
                    return "FAIL", "PPTX_REQUIRED_MEMBERS_MISSING:" + ",".join(missing)
                bad_member = archive.testzip()
                if bad_member:
                    return "FAIL", f"PPTX_CRC_ERROR:{bad_member}"
            return "PASS", None
        if format_name == "YAML":
            path.read_text(encoding="utf-8")
            return "PASS_TEXT_ONLY", None
        if format_name == "Unknown binary":
            return "PENDING", "FORMAT_SUPPORT_PENDING"
        return "NOT_APPLICABLE", None
    except (OSError, UnicodeError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        return "FAIL", f"{type(exc).__name__}:{exc}"


def scan_tree(source: Path) -> tuple[list[Path], list[dict[str, str]], list[dict[str, str]]]:
    files: list[Path] = []
    directories: list[dict[str, str]] = []
    directory_errors: list[dict[str, str]] = []

    def walk(directory: Path) -> None:
        relative = "." if directory == source else directory.relative_to(source).as_posix()
        try:
            entries = sorted(os.scandir(directory), key=lambda item: item.name)
            directories.append({"relative_path": relative, "status": "READABLE"})
        except OSError as exc:
            directories.append({"relative_path": relative, "status": "ERROR"})
            directory_errors.append(
                {"relative_path": relative, "error": f"{type(exc).__name__}:{exc}"}
            )
            return
        for entry in entries:
            path = Path(entry.path)
            try:
                if entry.is_symlink():
                    # Symlinks are registered as exclusions; they are not followed.
                    files.append(path)
                elif entry.is_dir(follow_symlinks=False):
                    walk(path)
                else:
                    files.append(path)
            except OSError:
                files.append(path)

    walk(source)
    return sorted(files, key=lambda p: p.relative_to(source).as_posix()), directories, directory_errors


def build_inventory(source: Path) -> dict[str, Any]:
    source = source.resolve()
    if not source.is_dir():
        raise ValueError(f"Corpus directory does not exist or is not a directory: {source}")

    paths, directories, directory_errors = scan_tree(source)
    records: list[dict[str, Any]] = []
    exclusions: list[dict[str, str]] = []

    for index, path in enumerate(paths, start=1):
        relative_path = path.relative_to(source).as_posix()
        record: dict[str, Any] = {
            "source_id": f"SRC-U01-{index:04d}",
            "relative_path": relative_path,
            "extension": path.suffix.lower(),
            "format": None,
            "media_type": None,
            "size_bytes": None,
            "sha256": None,
            "read_status": "ERROR",
            "inventory_status": "ERROR",
            "format_status": "PENDING",
            "format_validation": "NOT_RUN",
            "duplicate_group_id": None,
            "authority_status": "NOT_ASSESSED_U01",
            "errors": [],
        }
        try:
            file_stat = path.lstat()
            record["size_bytes"] = file_stat.st_size
            if stat.S_ISLNK(file_stat.st_mode):
                record["inventory_status"] = "EXCLUDED"
                record["read_status"] = "NOT_READ"
                record["errors"].append("SYMLINK_NOT_FOLLOWED")
                exclusions.append(
                    {
                        "relative_path": relative_path,
                        "reason": "SYMLINK_NOT_FOLLOWED",
                    }
                )
                records.append(record)
                continue
            if not stat.S_ISREG(file_stat.st_mode):
                record["inventory_status"] = "EXCLUDED"
                record["read_status"] = "NOT_READ"
                record["errors"].append("NON_REGULAR_FILE")
                exclusions.append(
                    {"relative_path": relative_path, "reason": "NON_REGULAR_FILE"}
                )
                records.append(record)
                continue
            format_info = identify_format(path)
            record.update(format_info)
            record["sha256"] = sha256_file(path)
            record["read_status"] = "READABLE"
            validation, validation_error = validate_format(path, record["format"])
            record["format_validation"] = validation
            if validation_error:
                record["errors"].append(validation_error)
            record["inventory_status"] = (
                "REGISTERED" if validation not in {"FAIL"} else "REGISTERED_WITH_FORMAT_ERROR"
            )
        except (OSError, UnicodeError) as exc:
            record["errors"].append(f"{type(exc).__name__}:{exc}")
        records.append(record)

    candidates: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record["read_status"] == "READABLE" and record["sha256"]:
            candidates[(record["size_bytes"], record["sha256"])].append(record)

    duplicate_groups: list[dict[str, Any]] = []
    duplicate_index = 0
    for candidate_records in sorted(candidates.values(), key=lambda group: group[0]["relative_path"]):
        if len(candidate_records) < 2:
            continue
        remaining = list(candidate_records)
        while remaining:
            reference = remaining.pop(0)
            equal = [reference]
            unequal: list[dict[str, Any]] = []
            for candidate in remaining:
                try:
                    if files_equal(source / reference["relative_path"], source / candidate["relative_path"]):
                        equal.append(candidate)
                    else:
                        unequal.append(candidate)
                except OSError as exc:
                    candidate["errors"].append(f"DUPLICATE_COMPARE_ERROR:{type(exc).__name__}:{exc}")
                    unequal.append(candidate)
            remaining = unequal
            if len(equal) > 1:
                duplicate_index += 1
                group_id = f"DUP-{duplicate_index:04d}"
                for record in equal:
                    record["duplicate_group_id"] = group_id
                duplicate_groups.append(
                    {
                        "duplicate_group_id": group_id,
                        "sha256": reference["sha256"],
                        "size_bytes": reference["size_bytes"],
                        "paths": sorted(item["relative_path"] for item in equal),
                        "binary_comparison": "PASS",
                    }
                )

    format_counts = Counter(record["format"] or "Unidentified" for record in records)
    readable_count = sum(record["read_status"] == "READABLE" for record in records)
    excluded_count = sum(record["inventory_status"] == "EXCLUDED" for record in records)
    read_error_count = sum(
        record["read_status"] == "ERROR" and record["inventory_status"] != "EXCLUDED"
        for record in records
    )
    format_error_count = sum(record["format_validation"] == "FAIL" for record in records)
    pending_format_count = sum(record["format_status"] == "PENDING" for record in records)

    return {
        "schema_version": SCHEMA_VERSION,
        "unit": "U01",
        "source_root": str(source),
        "scope": {
            "recursive": True,
            "symlinks_followed": False,
            "outputs_inside_source": False,
        },
        "format_policy": {
            "SUPPORTED": "Formato identificável na U01; não implica extrator homologado na U02.",
            "PENDING": "Formato não identificado/suportado pela política de identificação da U01.",
            "yaml_validation": "Somente legibilidade UTF-8; validação sintática requer decisão da U02.",
            "u02_extraction_status": "NOT_EVALUATED_U01",
        },
        "directories": directories,
        "files": records,
        "duplicate_groups": duplicate_groups,
        "exclusions": exclusions,
        "directory_errors": directory_errors,
        "summary": {
            "directory_count": len(directories),
            "file_entry_count": len(records),
            "readable_file_count": readable_count,
            "read_error_count": read_error_count,
            "format_error_count": format_error_count,
            "pending_format_count": pending_format_count,
            "excluded_entry_count": excluded_count,
            "duplicate_group_count": len(duplicate_groups),
            "duplicate_file_count": sum(len(group["paths"]) for group in duplicate_groups),
            "total_readable_bytes": sum(
                record["size_bytes"] or 0
                for record in records
                if record["read_status"] == "READABLE"
            ),
            "formats": dict(sorted(format_counts.items())),
        },
    }


def write_manifest_csv(path: Path, records: Iterable[dict[str, Any]]) -> None:
    fields = [
        "source_id",
        "relative_path",
        "extension",
        "format",
        "media_type",
        "size_bytes",
        "sha256",
        "read_status",
        "inventory_status",
        "format_status",
        "format_validation",
        "duplicate_group_id",
        "authority_status",
        "errors",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = {field: record.get(field) for field in fields}
            row["errors"] = " | ".join(record.get("errors", []))
            writer.writerow(row)


def markdown_cell(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def write_source_index(path: Path, inventory: dict[str, Any]) -> None:
    summary = inventory["summary"]
    lines = [
        "# ENT-02 — Índice de Fontes",
        "",
        f"- Unidade: `{inventory['unit']}`",
        f"- Corpus: `{inventory['source_root']}`",
        f"- Fontes registradas: **{summary['file_entry_count']}**",
        "- Autoridade documental: **não avaliada na U01**",
        "- Observação: `SUPPORTED` significa apenas identificação técnica na U01; não homologa extração na U02.",
        "",
        "| ID | Caminho relativo | Formato | Bytes | SHA-256 | Estado | Duplicata |",
        "| --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for record in inventory["files"]:
        values = [
            record["source_id"],
            record["relative_path"],
            record["format"],
            record["size_bytes"],
            record["sha256"],
            record["inventory_status"],
            record["duplicate_group_id"],
        ]
        lines.append("| " + " | ".join(markdown_cell(value) for value in values) + " |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_inventory_outputs(output: Path, inventory: dict[str, Any]) -> None:
    output.mkdir(parents=True, exist_ok=True)
    json_dump(output / "ENT-01-manifesto-corpus.json", inventory)
    write_manifest_csv(output / "ENT-01-manifesto-corpus.csv", inventory["files"])
    write_source_index(output / "ENT-02-indice-fontes.md", inventory)
    write_manifest_csv(output / "ENT-02-indice-fontes.csv", inventory["files"])


def build_snapshot(source: Path) -> dict[str, Any]:
    inventory = build_inventory(source)
    return {
        "schema_version": SCHEMA_VERSION,
        "source_root": inventory["source_root"],
        "files": [
            {
                "relative_path": record["relative_path"],
                "size_bytes": record["size_bytes"],
                "sha256": record["sha256"],
                "read_status": record["read_status"],
            }
            for record in inventory["files"]
        ],
        "directory_errors": inventory["directory_errors"],
    }


def compare_snapshots(before: dict[str, Any], after: dict[str, Any]) -> dict[str, Any]:
    def indexed(snapshot: dict[str, Any]) -> dict[str, tuple[Any, Any, Any]]:
        return {
            item["relative_path"]: (item["size_bytes"], item["sha256"], item["read_status"])
            for item in snapshot["files"]
        }

    left = indexed(before)
    right = indexed(after)
    added = sorted(set(right) - set(left))
    removed = sorted(set(left) - set(right))
    changed = sorted(path for path in set(left) & set(right) if left[path] != right[path])
    unchanged = sorted(path for path in set(left) & set(right) if left[path] == right[path])
    passed = not added and not removed and not changed
    return {
        "test_id": "T04-ACTUAL",
        "name": "Preservação do corpus real",
        "status": "PASS" if passed else "FAIL",
        "expected": {"added": [], "removed": [], "changed": []},
        "actual": {
            "added": added,
            "removed": removed,
            "changed": changed,
            "unchanged_count": len(unchanged),
        },
    }


def ensure_separate(source: Path, output: Path) -> None:
    source_resolved = source.resolve()
    output_resolved = output.resolve()
    if output_resolved == source_resolved or source_resolved in output_resolved.parents:
        raise ValueError("Output must be outside the source corpus")


def command_inventory(args: argparse.Namespace) -> int:
    source = Path(args.source)
    output = Path(args.output)
    ensure_separate(source, output)
    inventory = build_inventory(source)
    write_inventory_outputs(output, inventory)
    summary = inventory["summary"]
    print("U01 INVENTORY COMPLETE")
    print(f"source_root={inventory['source_root']}")
    for key, value in summary.items():
        if key != "formats":
            print(f"{key}={value}")
    print("formats=" + json.dumps(summary["formats"], ensure_ascii=False, sort_keys=True))
    return 0


def command_snapshot(args: argparse.Namespace) -> int:
    snapshot = build_snapshot(Path(args.source))
    json_dump(Path(args.output), snapshot)
    print(f"SNAPSHOT COMPLETE files={len(snapshot['files'])} output={Path(args.output)}")
    return 0


def command_compare(args: argparse.Namespace) -> int:
    with Path(args.before).open(encoding="utf-8") as handle:
        before = json.load(handle)
    with Path(args.after).open(encoding="utf-8") as handle:
        after = json.load(handle)
    result = compare_snapshots(before, after)
    if args.output:
        json_dump(Path(args.output), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    inventory = commands.add_parser("inventory", help="Generate ENT-01 and ENT-02")
    inventory.add_argument("--source", required=True)
    inventory.add_argument("--output", required=True)
    inventory.set_defaults(func=command_inventory)
    snapshot = commands.add_parser("snapshot", help="Capture paths, sizes and hashes")
    snapshot.add_argument("--source", required=True)
    snapshot.add_argument("--output", required=True)
    snapshot.set_defaults(func=command_snapshot)
    compare = commands.add_parser("compare", help="Compare two corpus snapshots")
    compare.add_argument("--before", required=True)
    compare.add_argument("--after", required=True)
    compare.add_argument("--output")
    compare.set_defaults(func=command_compare)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
