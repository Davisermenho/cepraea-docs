#!/usr/bin/env python3
"""Tests for the persistence layer (store.py)."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPOSITORY))

from espaut.store import (
    DEFAULT_CONFIG,
    append_jsonl,
    find_store,
    init_store,
    load_config,
    read_json,
    read_jsonl,
    require_store,
    write_json,
    write_jsonl,
    new_id,
)


def test_init_store() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = init_store(root)
        checks = {
            "store_exists": "PASS" if store.is_dir() else "FAIL",
            "tasks_dir": "PASS" if (store / "tasks").is_dir() else "FAIL",
            "evidence_dir": "PASS" if (store / "evidence").is_dir() else "FAIL",
            "decisions_dir": "PASS" if (store / "decisions").is_dir() else "FAIL",
            "cache_dir": "PASS" if (store / "cache").is_dir() else "FAIL",
            "config_exists": "PASS" if (store / "config.json").exists() else "FAIL",
            "events_exists": "PASS" if (store / "events.jsonl").exists() else "FAIL",
        }
        config = read_json(store / "config.json")
        checks["config_has_schema_version"] = (
            "PASS" if config.get("schema_version") == "0.1.0" else "FAIL"
        )
        return checks


def test_find_store() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        init_store(root)
        checks = {
            "find_from_root": "PASS" if find_store(root) is not None else "FAIL",
        }
        child = root / "sub" / "deep"
        child.mkdir(parents=True)
        checks["find_from_child"] = (
            "PASS" if find_store(child) is not None else "FAIL"
        )
    with tempfile.TemporaryDirectory() as isolated:
        checks["not_found"] = "PASS" if find_store(Path(isolated)) is None else "FAIL"
        return checks


def test_require_store_raises() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        try:
            require_store(Path(tmp))
            return {"raises": "FAIL"}
        except FileNotFoundError:
            return {"raises": "PASS"}


def test_json_roundtrip() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "data.json"
        original = {"chave": "valor", "número": 42, "lista": [1, 2, 3]}
        write_json(path, original)
        loaded = read_json(path)
        return {
            "roundtrip": "PASS" if loaded == original else "FAIL",
            "encoding": "PASS" if "valor" in path.read_text(encoding="utf-8") else "FAIL",
        }


def test_jsonl_roundtrip() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "log.jsonl"
        records = [{"id": 1, "msg": "first"}, {"id": 2, "msg": "second"}]
        write_jsonl(path, records)
        loaded = read_jsonl(path)
        checks = {"write_read": "PASS" if loaded == records else "FAIL"}

        append_jsonl(path, {"id": 3, "msg": "third"})
        loaded2 = read_jsonl(path)
        checks["append"] = "PASS" if len(loaded2) == 3 and loaded2[2]["id"] == 3 else "FAIL"
        return checks


def test_atomic_write() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "atomic.json"
        write_json(path, {"v": 1})
        write_json(path, {"v": 2})
        loaded = read_json(path)
        no_tmp = not path.with_suffix(".json.tmp").exists()
        return {
            "overwrite": "PASS" if loaded == {"v": 2} else "FAIL",
            "no_tmp_leftover": "PASS" if no_tmp else "FAIL",
        }


def test_new_id() -> dict[str, str]:
    a = new_id("TSK-")
    b = new_id("TSK-")
    return {
        "has_prefix": "PASS" if a.startswith("TSK-") else "FAIL",
        "unique": "PASS" if a != b else "FAIL",
        "length": "PASS" if len(a) == 16 else "FAIL",
    }


def test_load_config_defaults() -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = init_store(root)
        config = load_config(store)
        return {
            "has_defaults": "PASS" if config["merge_policy"] == "manual" else "FAIL",
            "schema_version": "PASS" if config["schema_version"] == "0.1.0" else "FAIL",
        }


ALL_TESTS = [
    ("init_store", test_init_store),
    ("find_store", test_find_store),
    ("require_store_raises", test_require_store_raises),
    ("json_roundtrip", test_json_roundtrip),
    ("jsonl_roundtrip", test_jsonl_roundtrip),
    ("atomic_write", test_atomic_write),
    ("new_id", test_new_id),
    ("load_config_defaults", test_load_config_defaults),
]


def main() -> int:
    total_pass = 0
    total_checks = 0

    for name, fn in ALL_TESTS:
        try:
            checks = fn()
        except Exception as exc:
            print(f"  [FAIL] {name} — exception: {exc}")
            total_checks += 1
            continue

        for sub, status in checks.items():
            total_checks += 1
            mark = "PASS" if status == "PASS" else "FAIL"
            if status == "PASS":
                total_pass += 1
            print(f"  [{mark}] {name}.{sub}")

    print(f"\nstore: {total_pass}/{total_checks} passed")
    return 0 if total_pass == total_checks else 1


if __name__ == "__main__":
    raise SystemExit(main())
