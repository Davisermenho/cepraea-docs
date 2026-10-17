#!/usr/bin/env python3
"""Deterministically verify U04 candidates, traceability and publication guards."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from u04_consolidate import load_json, load_jsonl, sha256_file


def verify(
    u04_root: Path,
    claims_path: Path,
    decision_registry_path: Path,
    decision_record_path: Path,
    technical_path: Path,
    source_root: Path,
    u01_manifest_path: Path,
) -> dict:
    generated = u04_root / "generated"
    errors: list[str] = []
    manifest_path = generated / "U04-run-manifest.json"
    if not manifest_path.is_file():
        return {"schema_version": "1.0.0", "unit": "U04", "status": "FAIL", "checks": {}, "errors": ["COMPLETE_MANIFEST_MISSING"]}
    manifest = load_json(manifest_path)
    required = set(manifest["files"])
    actual = {p.name for p in generated.iterdir() if p.is_file() and p.name != manifest_path.name}
    if required != actual:
        errors.append("DELIVERABLE_SET_MISMATCH")
    hash_mismatches = sorted(name for name, digest in manifest["files"].items() if not (generated / name).is_file() or sha256_file(generated / name) != digest)
    if hash_mismatches:
        errors.append("DELIVERABLE_HASH_MISMATCH:" + ",".join(hash_mismatches))
    if manifest.get("status") != "COMPLETE":
        errors.append("RUN_NOT_COMPLETE")
    if manifest.get("publication_authorized") is not False:
        errors.append("PUBLICATION_AUTHORIZED_WITHOUT_A3")

    decisions = load_json(decision_registry_path)
    if sha256_file(decision_record_path) != decisions.get("record_sha256"):
        errors.append("DECISION_RECORD_HASH_MISMATCH")
    if decisions.get("approval_level") != "A2" or decisions.get("scope_limits", {}).get("a3_granted") is not False:
        errors.append("APPROVAL_SCOPE_INVALID")
    claims = load_jsonl(claims_path)
    claim_ids = {item["claim_id"] for item in claims}
    decision_ids = {item["decision_id"] for item in decisions["decisions"]}
    evidence_ids = {"OBS-U04-REPO-001", "OBS-U04-SUPABASE-001"}

    trace = load_json(generated / "ENT-07-mapa-origem-destino.json")
    statement_ids = [item["statement_id"] for item in trace["statements"]]
    duplicate_statement_ids = sorted(value for value, count in Counter(statement_ids).items() if count > 1)
    duplicate_normative_texts = sorted(value for value, count in Counter(item["text"] for item in trace["statements"]).items() if count > 1)
    if duplicate_statement_ids:
        errors.append("DUPLICATE_STATEMENT_IDS")
    if duplicate_normative_texts:
        errors.append("DUPLICATE_NORMATIVE_TEXTS")
    missing_basis = sorted({ref for item in trace["statements"] for ref in item["basis_references"] if ref not in claim_ids | decision_ids | evidence_ids})
    empty_basis = sorted(item["statement_id"] for item in trace["statements"] if not item["basis_references"])
    if missing_basis or empty_basis:
        errors.append("TRACEABILITY_INCOMPLETE")
    if trace.get("publication_authorized") is not False:
        errors.append("TRACEABILITY_MAP_AUTHORIZED_PUBLICATION")

    approval = load_json(generated / "approval-registry.json")
    approval_errors = []
    for entry in approval["entries"]:
        path = source_root / entry["path"]
        if entry["approval_status"] != "AGUARDANDO_APROVACAO" or entry["approved_by"] is not None or entry["effective_date"] is not None or entry["normative_precedence_active"] is not False:
            approval_errors.append(entry["document_id"] + ":FALSE_APPROVAL")
        if not path.is_file() or sha256_file(path) != entry["sha256"]:
            approval_errors.append(entry["document_id"] + ":HASH_MISMATCH")
    if approval_errors:
        errors.append("APPROVAL_REGISTRY_INVALID:" + ",".join(approval_errors))

    candidates = sorted(generated.glob("ENT-06*.md"))
    candidate_guard_errors = []
    for path in candidates:
        text = path.read_text(encoding="utf-8")
        if "`CANDIDATO_NAO_APROVADO`" not in text or "Publicação oficial autorizada: `NÃO`" not in text:
            candidate_guard_errors.append(path.name)
    if len(candidates) != 3 or candidate_guard_errors:
        errors.append("CANDIDATE_PUBLICATION_GUARD_INVALID")

    pending = load_json(generated / "ENT-08-pendencias-revisao.json")
    pending_subjects = {item["subject"] for item in pending["items"]}
    required_pending = {"Aprovação das versões documentais", "Arquitetura definitiva", "Viabilidade do orçamento", "Implementação e infraestrutura alvo", "Publicação oficial A3"}
    if not required_pending.issubset(pending_subjects) or any(not item["status"].startswith("PENDENTE") for item in pending["items"]):
        errors.append("REQUIRED_PENDING_DECISIONS_NOT_PRESERVED")

    technical = load_json(technical_path)
    if technical["repository"]["technical_state"] != "VALIDADO_ESTATICAMENTE" or technical["supabase"]["status"] != "INACTIVE" or technical["supabase"]["database_introspection"] != "NOT_VERIFIED_CONNECTION_TIMEOUT" or technical["supabase"]["mutations_performed"] is not False:
        errors.append("TECHNICAL_EVIDENCE_BOUNDARY_INVALID")

    inventory = load_json(u01_manifest_path)
    changed, missing = [], []
    for item in inventory["files"]:
        path = source_root / item["relative_path"]
        if not path.is_file():
            missing.append(item["relative_path"])
        elif sha256_file(path) != item["sha256"]:
            changed.append(item["relative_path"])
    current_files = {str(p.relative_to(source_root)) for p in source_root.rglob("*") if p.is_file()}
    inventoried = {item["relative_path"] for item in inventory["files"]}
    unexpected = sorted(current_files - inventoried)
    if changed or missing or unexpected:
        errors.append("CORPUS_NOT_PRESERVED")

    return {
        "schema_version": "1.0.0",
        "unit": "U04",
        "status": "PASS" if not errors else "FAIL",
        "checks": {
            "deliverables": sorted(required),
            "hash_mismatches": hash_mismatches,
            "candidate_documents": len(candidates),
            "statements": len(statement_ids),
            "duplicate_statement_ids": duplicate_statement_ids,
            "duplicate_normative_texts": duplicate_normative_texts,
            "missing_basis_references": missing_basis,
            "statements_without_basis": empty_basis,
            "approval_registry_errors": approval_errors,
            "candidate_guard_errors": candidate_guard_errors,
            "pending_items": len(pending["items"]),
            "publication_authorized": False,
            "a3_granted": False,
            "corpus_files_checked": len(inventory["files"]),
            "corpus_changed": changed,
            "corpus_missing": missing,
            "corpus_unexpected": unexpected,
            "technical_evidence_sha256": sha256_file(technical_path),
        },
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u04", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--decision-registry", required=True)
    parser.add_argument("--decision-record", required=True)
    parser.add_argument("--technical-evidence", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--u01-manifest", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = verify(Path(args.u04), Path(args.claims), Path(args.decision_registry), Path(args.decision_record), Path(args.technical_evidence), Path(args.source), Path(args.u01_manifest))
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8", newline="\n")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
