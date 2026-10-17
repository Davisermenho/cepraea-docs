#!/usr/bin/env python3
"""Execute the predeclared U01 T01-T04 controlled tests."""

from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
from pathlib import Path
from typing import Any, Callable


REPOSITORY = Path(__file__).resolve().parents[2]
PLAN_PATH = Path(__file__).with_name("test_cases.json")
MODULE_PATH = REPOSITORY / "scripts" / "u01_inventory.py"


def load_module():
    spec = importlib.util.spec_from_file_location("u01_inventory", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U01 = load_module()


def load_plan() -> dict[str, Any]:
    with PLAN_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def case(plan: dict[str, Any], test_id: str) -> dict[str, Any]:
    return next(item for item in plan["tests"] if item["id"] == test_id)


def write_controlled_files(root: Path, files: dict[str, str]) -> None:
    for relative_path, value in files.items():
        target = root / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        if relative_path.endswith(".bin"):
            target.write_bytes(bytes.fromhex(value))
        else:
            target.write_text(value, encoding="utf-8")


def run_t01(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T01")
    with tempfile.TemporaryDirectory(prefix="u01-t01-") as temp:
        root = Path(temp)
        write_controlled_files(root, definition["input"]["controlled_files"])
        inventory = U01.build_inventory(root)
        actual = {
            "file_count": inventory["summary"]["file_entry_count"],
            "relative_paths": [item["relative_path"] for item in inventory["files"]],
            "read_error_count": inventory["summary"]["read_error_count"],
        }
    return result(definition, actual)


def run_t02(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T02")
    with tempfile.TemporaryDirectory(prefix="u01-t02-") as temp:
        path = Path(temp) / definition["input"]["relative_path"]
        path.write_bytes(definition["input"]["bytes_utf8"].encode("utf-8"))
        actual = {"sha256": U01.sha256_file(path)}
    return result(definition, actual)


def run_t03(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T03")
    with tempfile.TemporaryDirectory(prefix="u01-t03-") as temp:
        root = Path(temp)
        write_controlled_files(root, definition["input"]["controlled_files"])
        inventory = U01.build_inventory(root)
        duplicate_paths = (
            inventory["duplicate_groups"][0]["paths"]
            if inventory["duplicate_groups"]
            else []
        )
        actual = {
            "duplicate_group_count": len(inventory["duplicate_groups"]),
            "duplicate_paths": duplicate_paths,
        }
    return result(definition, actual)


def run_t04(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T04")
    with tempfile.TemporaryDirectory(prefix="u01-t04-") as temp:
        root = Path(temp)
        write_controlled_files(root, definition["input"]["controlled_files"])
        before = U01.build_snapshot(root)
        U01.build_inventory(root)
        after = U01.build_snapshot(root)
        comparison = U01.compare_snapshots(before, after)["actual"]
        actual = {
            "added": comparison["added"],
            "removed": comparison["removed"],
            "changed": comparison["changed"],
            "unchanged_count": comparison["unchanged_count"],
        }
    return result(definition, actual)


def output_hashes(output: Path) -> dict[str, str]:
    return {
        path.name: U01.sha256_file(path)
        for path in sorted(output.iterdir())
        if path.is_file()
    }


def run_t13(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T13")
    with tempfile.TemporaryDirectory(prefix="u01-t13-") as temp:
        root = Path(temp) / "source"
        output = Path(temp) / "output"
        root.mkdir()
        write_controlled_files(root, definition["input"]["controlled_files"])
        inventory = U01.build_inventory(root)
        U01.write_inventory_outputs(output, inventory)
        first = output_hashes(output)
        U01.write_inventory_outputs(output, U01.build_inventory(root))
        second = output_hashes(output)
        expected_names = {
            "ENT-01-manifesto-corpus.json",
            "ENT-01-manifesto-corpus.csv",
            "ENT-02-indice-fontes.md",
            "ENT-02-indice-fontes.csv",
        }
        actual = {
            "content_equivalent": first == second,
            "output_file_count_first": len(first),
            "output_file_count_second": len(second),
            "unexpected_additional_files": sorted(set(second) - expected_names),
        }
    return result(definition, actual)


def run_t14(plan: dict[str, Any]) -> dict[str, Any]:
    definition = case(plan, "T14")
    with tempfile.TemporaryDirectory(prefix="u01-t14-") as temp:
        root = Path(temp) / "source"
        output = Path(temp) / "output"
        root.mkdir()
        output.mkdir()
        write_controlled_files(root, definition["input"]["controlled_files"])
        partial_path = output / "ENT-01-manifesto-corpus.json"
        partial_path.write_text("{\"partial\":", encoding="utf-8")
        U01.write_inventory_outputs(output, U01.build_inventory(root))
        manifest_valid_json = True
        try:
            manifest = json.loads(partial_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest_valid_json = False
            manifest = {"summary": {"file_entry_count": None}}
        actual = {
            "manifest_valid_json": manifest_valid_json,
            "manifest_file_count": manifest["summary"]["file_entry_count"],
            "complete_output_file_count": len(output_hashes(output)),
            "partial_content_retained": "partial" in manifest,
        }
    return result(definition, actual)


def result(definition: dict[str, Any], actual: dict[str, Any]) -> dict[str, Any]:
    expected = definition["expected"]
    return {
        "id": definition["id"],
        "name": definition["name"],
        "status": "PASS" if actual == expected else "FAIL",
        "expected": expected,
        "actual": actual,
    }


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--output")
    args = cli.parse_args()
    plan = load_plan()
    runners: list[Callable[[dict[str, Any]], dict[str, Any]]] = [
        run_t01,
        run_t02,
        run_t03,
        run_t04,
        run_t13,
        run_t14,
    ]
    results = [runner(plan) for runner in runners]
    report = {
        "schema_version": "1.0.0",
        "unit": "U01",
        "plan": str(PLAN_PATH.relative_to(REPOSITORY)),
        "all_passed": all(item["status"] == "PASS" for item in results),
        "results": results,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
