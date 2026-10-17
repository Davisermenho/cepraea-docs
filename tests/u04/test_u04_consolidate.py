#!/usr/bin/env python3
"""Execute U04 acceptance tests whose expected results were predeclared."""

from __future__ import annotations

import importlib.util
import argparse
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PLAN = json.loads(Path(__file__).with_name("test_cases.json").read_text(encoding="utf-8"))


def load_module():
    path = ROOT / "scripts/u04_consolidate.py"
    spec = importlib.util.spec_from_file_location("u04_consolidate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U04 = load_module()
BASE = ROOT / "artifacts/PRO-CEPRAEA-DOC-CONS-001"
CLAIMS = BASE / "U03-v2/ENT-03-registro-evidencias-afirmacoes.jsonl"
REGISTRY = BASE / "U04/input/decision-registry.json"
RECORD = BASE / "U04/input/DECISOES-RESPONSAVEL-2026-10-17.md"
TECHNICAL = BASE / "U04/input/technical-inspection.json"
SOURCE = ROOT / "docs/reconciliação"


def spec(test_id: str) -> dict:
    return next(item for item in PLAN["tests"] if item["id"] == test_id)


def record(test_id: str, actual: dict) -> dict:
    item = spec(test_id)
    return {"id": test_id, "name": item["name"], "input": item["input"], "expected": item["expected"], "actual": actual, "status": "PASS" if actual == item["expected"] else "FAIL"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args()
    outputs = U04.build_outputs(CLAIMS, REGISTRY, RECORD, TECHNICAL, SOURCE)
    approval = json.loads(outputs["approval-registry.json"])
    results = [record("T08", {
        "all_waiting_approval": all(x["approval_status"] == "AGUARDANDO_APROVACAO" for x in approval["entries"]),
        "precedence_inactive": all(x["normative_precedence_active"] is False for x in approval["entries"]),
    })]
    pending = json.loads(outputs["ENT-08-pendencias-revisao.json"])["items"]
    subjects = {x["subject"] for x in pending}
    results.append(record("T09", {
        "architecture_pending": "Arquitetura definitiva" in subjects,
        "target_verification_pending": "Implementação e infraestrutura alvo" in subjects,
    }))
    trace = json.loads(outputs["ENT-07-mapa-origem-destino.json"])
    claims = {x["claim_id"] for x in U04.load_jsonl(CLAIMS)}
    decisions = {x["decision_id"] for x in U04.load_json(REGISTRY)["decisions"]}
    known = claims | decisions | {"OBS-U04-REPO-001", "OBS-U04-SUPABASE-001"}
    results.append(record("T10", {
        "statements": len(trace["statements"]),
        "missing_basis": sorted({r for x in trace["statements"] for r in x["basis_references"] if r not in known}),
        "without_basis": sorted(x["statement_id"] for x in trace["statements"] if not x["basis_references"]),
    }))
    candidate_texts = [value for name, value in outputs.items() if name.startswith("ENT-06")]
    results.append(record("T11", {
        "publication_authorized": trace["publication_authorized"],
        "all_candidate_only": all("`CANDIDATO_NAO_APROVADO`" in value and "Publicação oficial autorizada: `NÃO`" in value for value in candidate_texts),
    }))
    second = U04.build_outputs(CLAIMS, REGISTRY, RECORD, TECHNICAL, SOURCE)
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        first_publish = U04.publish(outputs, root)
        repeat_publish = U04.publish(second, root)
        ids = [x["statement_id"] for x in trace["statements"]]
        results.append(record("T13", {
            "outputs_equivalent": outputs == second,
            "duplicate_statement_ids": sorted({x for x in ids if ids.count(x) > 1}),
            "existing_output_accepted_only_if_equivalent": first_publish["status"] == "PASS" and repeat_publish.get("equivalent_existing") is True,
        }))
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        interrupted = U04.publish(outputs, root, simulate_interrupt=True)
        absent = not (root / "generated/U04-run-manifest.json").exists()
        interrupted_not_published = interrupted["published"] is False and not (root / "generated").exists()
        clean = U04.publish(outputs, root)
        results.append(record("T14", {
            "interrupted_not_published": interrupted_not_published,
            "complete_manifest_absent": absent,
            "clean_rerun_passes": clean["status"] == "PASS" and (root / "generated/U04-run-manifest.json").is_file(),
        }))
    result = {"schema_version": "1.0.0", "unit": "U04", "status": "PASS" if all(x["status"] == "PASS" for x in results) else "FAIL", "passed": sum(x["status"] == "PASS" for x in results), "total": len(results), "results": results}
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8", newline="\n")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
