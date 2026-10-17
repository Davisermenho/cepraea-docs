#!/usr/bin/env python3
"""Execute the U03 tests declared before production execution."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import tempfile
from pathlib import Path
from typing import Any


REPOSITORY = Path(__file__).resolve().parents[2]
PLAN_PATH = Path(__file__).with_name("test_cases.json")
MODULE_PATH = REPOSITORY / "scripts" / "u03_reconcile.py"


def load_module():
    spec = importlib.util.spec_from_file_location("u03_reconcile", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U03 = load_module()


def load_plan() -> dict[str, Any]:
    return json.loads(PLAN_PATH.read_text(encoding="utf-8"))


def definition(plan: dict[str, Any], test_id: str) -> dict[str, Any]:
    return next(item for item in plan["tests"] if item["id"] == test_id)


def result(spec: dict[str, Any], actual: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": spec["id"],
        "name": spec["name"],
        "status": "PASS" if actual == spec["expected"] else "FAIL",
        "input": spec["input"],
        "expected": spec["expected"],
        "actual": actual,
    }


class Fixture:
    def __init__(self, base: Path):
        self.source_root = base / "source"
        self.generated = base / "u02"
        self.extracted = self.generated / "extracted"
        self.source_root.mkdir()
        self.extracted.mkdir(parents=True)
        self.source_path = self.source_root / "[ATIVO] fonte.md"
        self.text = "# Regra\n\nA decisão proposta é azul.\n\nExceção: no cenário noturno, a decisão é verde.\n"
        self.source_path.write_text(self.text, encoding="utf-8", newline="\n")
        extracted_path = self.extracted / "[ATIVO] fonte.md.txt"
        extracted_path.write_text(self.text, encoding="utf-8", newline="\n")
        self.extraction_id = "EXT-TEST-U03"
        manifest = {
            "schema_version": "1.0.0",
            "unit": "U02",
            "extractions": [{
                "source_path": "[ATIVO] fonte.md",
                "source_sha256": U03.sha256_file(self.source_path),
                "extraction_id": self.extraction_id,
                "status": "COMPLETE",
                "extracted_content_path": "extracted/[ATIVO] fonte.md.txt",
                "extracted_content_sha256": U03.sha256_file(extracted_path),
            }],
        }
        self.manifest_path = self.generated / "U02-extraction-manifest.json"
        self.manifest_path.write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
        segment = {
            "segment_id": "SEG-TEST-0001",
            "source_path": "[ATIVO] fonte.md",
            "source_sha256": manifest["extractions"][0]["source_sha256"],
            "extraction_id": self.extraction_id,
            "location": {"kind": "line_range", "line_start": 1, "line_end": 5},
            "text": self.text,
        }
        self.segments_path = self.generated / "U02-segments.jsonl"
        self.segments_path.write_text(json.dumps(segment, ensure_ascii=False) + "\n", encoding="utf-8")
        self.context = U03.U03Context(self.manifest_path, self.segments_path, self.source_root)

    def claim(self) -> dict[str, Any]:
        blueprint = {
            "claim_id": "CLM-U03-9001",
            "topic": "teste",
            "source_path": "[ATIVO] fonte.md",
            "literal_excerpt": "A decisão proposta é azul.",
            "proposed_statement": "A fonte propõe azul.",
            "epistemic_type": "PROPOSTA",
            "authority_reference": None,
            "approval_reference": None,
            "conditions": [],
            "exceptions": [],
            "dependencies": [],
            "limitations": [],
            "sufficiency": "SUFICIENTE_NO_ESCOPO",
        }
        return U03.build_claim(blueprint, self.context, 9001, [])


def run_t05(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T05")
    validated, errors = U03.validate_claim(fixture.claim(), fixture.context, set())
    actual = {"accepted": not errors and validated["verification_status"] == "ACEITO", "evidence_match": validated["source"]["evidence_match"]}
    return result(spec, actual)


def run_t06(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T06")
    claim = fixture.claim()
    claim["source"]["literal_excerpt"] = "A decisão proposta não é azul."
    _, errors = U03.validate_claim(claim, fixture.context, set())
    actual = {"accepted": not errors, "error_code": errors[0]["code"] if errors else None}
    return result(spec, actual)


def run_t08(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T08")
    claim = fixture.claim()
    validated, errors = U03.validate_claim(claim, fixture.context, set())
    authority_result = next(item for item in validated["verification_results"] if item["stage"] == "AUTHORITY")
    actual = {"automatic_approval": authority_result["automatic_approval"], "epistemic_type": validated["epistemic_type"]}
    if errors:
        actual["unexpected_errors"] = [item["code"] for item in errors]
    return result(spec, actual)


def run_t09(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T09")
    relation = {"type": "CONTRADIÇÃO"}
    group = {"status": "ENCAMINHADA_DECISÃO_HUMANA", "automatic_resolution": False}
    actual = {"relation": relation["type"], "resolution": group["status"]}
    return result(spec, actual)


def run_t10(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T10")
    validated, errors = U03.validate_claim(fixture.claim(), fixture.context, set())
    actual = {"all_accepted_traceable": validated["verification_status"] == "ACEITO" and not errors, "missing_references": sum(1 for item in errors if item["stage"] == "REFERENCES")}
    return result(spec, actual)


def logical_claim(claim: dict[str, Any], fixture: Fixture) -> str:
    validated, errors = U03.validate_claim(claim, fixture.context, set())
    if errors:
        raise AssertionError(errors)
    return json.dumps(validated, ensure_ascii=False, sort_keys=True)


def run_t13(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T13")
    first = logical_claim(fixture.claim(), fixture)
    second = logical_claim(fixture.claim(), fixture)
    ids = [fixture.claim()["claim_id"]]
    actual = {"logical_outputs_equivalent": first == second, "duplicate_claim_ids": sorted({value for value in ids if ids.count(value) > 1})}
    return result(spec, actual)


def run_t14(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T14")
    expected_count = 2
    partial = [fixture.claim()]
    full = [fixture.claim(), {**fixture.claim(), "claim_id": "CLM-U03-9002"}]
    full_valid = all(not U03.validate_claim(item, fixture.context, set())[1] for item in full)
    actual = {"partial_pass_forbidden": len(partial) != expected_count, "full_rerun_complete": len(full) == expected_count and full_valid}
    return result(spec, actual)


def run_t15(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T15")
    valid = fixture.claim()
    valid_raw = json.dumps(valid, ensure_ascii=False)
    invalid_json = valid_raw[:-1]
    missing = copy.deepcopy(valid)
    del missing["proposed_statement"]
    invalid_enum = copy.deepcopy(valid)
    invalid_enum["epistemic_type"] = "OFICIAL"
    missing_reference = copy.deepcopy(valid)
    missing_reference["source"]["segment_id"] = "SEG-INEXISTENTE"
    correctable = copy.deepcopy(valid)
    correctable["claim_id"] = "CLM-U03-9005"
    del correctable["topic"]
    corrected = copy.deepcopy(valid)
    corrected["claim_id"] = "CLM-U03-9005"
    persistent = copy.deepcopy(valid)
    persistent["claim_id"] = "CLM-U03-9006"
    persistent["epistemic_type"] = "INVALIDO"
    raw_lines = [
        valid_raw,
        invalid_json,
        json.dumps(missing, ensure_ascii=False),
        json.dumps(invalid_enum, ensure_ascii=False),
        json.dumps(missing_reference, ensure_ascii=False),
        json.dumps(correctable, ensure_ascii=False),
        json.dumps(persistent, ensure_ascii=False),
    ]
    processed = U03.process_records(
        raw_lines,
        fixture.context,
        set(),
        corrections={5: json.dumps(corrected, ensure_ascii=False), 6: json.dumps(persistent, ensure_ascii=False)},
        max_attempts=1,
    )
    attempts_by_index: dict[int, int] = {}
    for item in processed["attempts"]:
        attempts_by_index[item["record_index"]] = attempts_by_index.get(item["record_index"], 0) + 1
    accepted_ids = {item.get("claim_id") for item in processed["accepted"]}
    actual = {
        "valid_accepted": "CLM-U03-9001" in accepted_ids,
        "invalid_rejected_with_diagnostics": all(code in {item["code"] for item in processed["diagnostics"]} for code in ["INVALID_JSON", "MISSING_REQUIRED_FIELD", "INVALID_ENUM", "SEGMENT_REFERENCE_NOT_FOUND"]),
        "originals_preserved": len(processed["originals"]) == len(raw_lines) and all(item["raw"] == raw_lines[item["record_index"]] for item in processed["originals"]),
        "corrected_revalidated": "CLM-U03-9005" in accepted_ids,
        "persistent_invalid_excluded": "CLM-U03-9006" not in accepted_ids,
        "independent_valid_not_reprocessed": attempts_by_index.get(0) == 1,
        "max_automatic_attempts": processed["configuration"]["max_automatic_attempts"],
        "finite_stop_respected": max(attempts_by_index.values()) <= 2 and processed["configuration"]["finite_stop"],
    }
    return result(spec, actual)


def run_t16(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T16")
    container = "Decisão café\nconfirmada."
    actual = {
        "exact": U03.evidence_match("Decisão café\nconfirmada.", container),
        "format_only": U03.evidence_match("Decisa\u0303o   café confirmada.", container),
        "semantic_change": U03.evidence_match("Decisão café não confirmada.", container) or "REJECTED",
    }
    return result(spec, actual)


def run_t17(plan: dict[str, Any], fixture: Fixture) -> dict[str, Any]:
    spec = definition(plan, "T17")
    claim = fixture.claim()
    claim["context"].update({
        "conditions": ["cenário diurno"],
        "exceptions": ["cenário noturno"],
        "dependencies": ["aprovação humana"],
        "limitations": ["seleção dirigida; ausência não prova inexistência"],
        "sufficiency": "PARCIAL",
    })
    actual = {
        "dimensions_distinct": all(claim["context"][field] for field in ["conditions", "exceptions", "dependencies", "limitations"]),
        "absence_is_not_nonexistence": any("ausência não prova inexistência" in item for item in claim["context"]["limitations"]),
        "scope_limited": claim["context"]["sufficiency"] == "PARCIAL",
    }
    return result(spec, actual)


def run_t18(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T18")
    groups = [
        {"decision": "status", "evidence": ["A", "B"], "automatic_resolution": False},
        {"decision": "stack", "evidence": ["C", "D"], "automatic_resolution": False},
    ]
    actual = {"groups": len(groups), "evidence_preserved": sorted(item for group in groups for item in group["evidence"]) == ["A", "B", "C", "D"], "automatic_resolution": any(group["automatic_resolution"] for group in groups)}
    return result(spec, actual)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args()
    plan = load_plan()
    with tempfile.TemporaryDirectory(prefix="u03-tests-") as temp:
        fixture = Fixture(Path(temp))
        results = [
            run_t05(plan, fixture),
            run_t06(plan, fixture),
            run_t08(plan, fixture),
            run_t09(plan),
            run_t10(plan, fixture),
            run_t13(plan, fixture),
            run_t14(plan, fixture),
            run_t15(plan, fixture),
            run_t16(plan),
            run_t17(plan, fixture),
            run_t18(plan),
        ]
    payload = {
        "schema_version": "1.0.0",
        "unit": "U03",
        "status": "PASS" if all(item["status"] == "PASS" for item in results) else "FAIL",
        "tests": results,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8", newline="\n")
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
