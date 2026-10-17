#!/usr/bin/env python3
"""Independently cross-validate U03 deliverables against U02 and the corpus."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from u03_reconcile import U03Context, load_json, load_jsonl, sha256_file, validate_claim, validate_relations


def logical_original(record: dict) -> dict:
    value = json.loads(json.dumps(record, ensure_ascii=False))
    value["verification_status"] = "PENDENTE"
    value["verification_results"] = []
    return value


def verify(
    manifest_path: Path,
    segments_path: Path,
    source_root: Path,
    output_root: Path,
    baseline_summary_path: Path | None = None,
) -> dict:
    context = U03Context(manifest_path, segments_path, source_root)
    accepted = load_jsonl(output_root / "generated/U03-claims-accepted.jsonl")
    rejected = load_jsonl(output_root / "generated/U03-claims-rejected.jsonl")
    originals = load_jsonl(output_root / "evidence/U03-agent-output-original.jsonl")
    relation_doc = load_json(output_root / "generated/U03-relations.json")
    divergence_doc = load_json(output_root / "generated/U03-divergences-pending.json")
    coverage = load_json(output_root / "generated/U03-context-coverage.json")
    consolidation = load_json(output_root / "generated/U03-consolidation-map.json")
    diagnostics = load_json(output_root / "evidence/U03-validation-diagnostics.json")
    current_summary = load_json(output_root / "evidence/U03-run-summary.json")
    relation_ids = {item["relation_id"] for item in relation_doc["relations"]}
    errors: list[str] = []
    validation_diagnostics = []
    for claim in accepted:
        validated, claim_errors = validate_claim(claim, context, relation_ids)
        if claim_errors or validated["verification_status"] != "ACEITO":
            validation_diagnostics.extend(claim_errors)
    if validation_diagnostics:
        errors.append(f"ACCEPTED_CLAIMS_INVALID:{len(validation_diagnostics)}")
    ids = [item["claim_id"] for item in accepted]
    duplicate_ids = sorted(value for value, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        errors.append("DUPLICATE_CLAIM_IDS:" + ",".join(duplicate_ids))
    relation_config = {
        "relations": relation_doc["relations"],
        "divergence_groups": divergence_doc["divergence_groups"],
    }
    relation_errors = validate_relations(relation_config, set(ids))
    if relation_errors:
        errors.append(f"INVALID_RELATIONS_OR_GROUPS:{len(relation_errors)}")
    if rejected:
        errors.append(f"PRODUCTION_REJECTED_RECORDS:{len(rejected)}")
    if diagnostics["diagnostics"]:
        errors.append(f"PRODUCTION_DIAGNOSTICS:{len(diagnostics['diagnostics'])}")
    if len(originals) != len(accepted) + len(rejected):
        errors.append("ORIGINAL_RECORD_COUNT_MISMATCH")
    accepted_by_id = {item["claim_id"]: item for item in accepted}
    for original in originals:
        accepted_record = accepted_by_id.get(original["claim_id"])
        if accepted_record is not None and original != logical_original(accepted_record):
            errors.append(f"ORIGINAL_NOT_PRESERVED:{original['claim_id']}")
    ent03 = load_jsonl(output_root / "ENT-03-registro-evidencias-afirmacoes.jsonl")
    if ent03 != accepted:
        errors.append("ENT03_ACCEPTED_RECORD_MISMATCH")
    if coverage["retrieval_coverage"]["claims"] != len(accepted):
        errors.append("COVERAGE_CLAIM_COUNT_MISMATCH")
    mapped_ids = {
        claim_id
        for section in consolidation["sections"]
        for field in ("eligible_claim_ids", "pending_claim_ids")
        for claim_id in section[field]
    }
    missing_map = sorted(set(ids) - mapped_ids)
    if missing_map:
        errors.append("CONSOLIDATION_MAP_MISSING:" + ",".join(missing_map))
    if consolidation["publication_authorized"] is not False:
        errors.append("PUBLICATION_WAS_AUTHORIZED")
    automatic_resolutions = [item["divergence_id"] for item in divergence_doc["divergence_groups"] if item["automatic_resolution"]]
    if automatic_resolutions:
        errors.append("AUTOMATIC_DIVERGENCE_RESOLUTION:" + ",".join(automatic_resolutions))
    unhandled_groups = [
        item["divergence_id"]
        for item in divergence_doc["divergence_groups"]
        if not (item["status"].startswith("ENCAMINHADA") or item["status"].startswith("RESOLVIDA"))
    ]
    if unhandled_groups:
        errors.append("UNHANDLED_MATERIAL_DIVERGENCE:" + ",".join(unhandled_groups))
    invalid_human = [
        item["claim_id"]
        for item in accepted
        if item["epistemic_type"] == "DECISÃO_HUMANA"
        and ((item.get("authority_reference") or {}).get("verification") != "VERIFICADA_NO_CORPUS" or item.get("approval_reference") is None)
    ]
    if invalid_human:
        errors.append("UNVERIFIED_HUMAN_DECISION_ACCEPTED:" + ",".join(invalid_human))
    output_files = sorted(path.name for path in output_root.glob("ENT-*") if path.is_file())
    output_hashes = {name: sha256_file(output_root / name) for name in output_files}
    reexecution_equivalent = None
    if baseline_summary_path is not None:
        baseline_summary = load_json(baseline_summary_path)
        reexecution_equivalent = (
            baseline_summary.get("output_hashes") == current_summary.get("output_hashes")
            and baseline_summary.get("claims_accepted") == current_summary.get("claims_accepted")
            and baseline_summary.get("claims_rejected") == current_summary.get("claims_rejected")
            and baseline_summary.get("relations") == current_summary.get("relations")
            and baseline_summary.get("divergence_groups") == current_summary.get("divergence_groups")
        )
        if not reexecution_equivalent:
            errors.append("REAL_REEXECUTION_OUTPUT_MISMATCH")
    return {
        "schema_version": "1.0.0",
        "unit": "U03",
        "status": "PASS" if not errors else "FAIL",
        "checks": {
            "accepted_claims": len(accepted),
            "rejected_claims": len(rejected),
            "original_records": len(originals),
            "duplicate_claim_ids": duplicate_ids,
            "relations": len(relation_doc["relations"]),
            "divergence_groups": len(divergence_doc["divergence_groups"]),
            "automatic_resolutions": automatic_resolutions,
            "unhandled_divergence_groups": unhandled_groups,
            "unverified_human_decisions_accepted": invalid_human,
            "mapped_claims": len(mapped_ids),
            "locators_without_u02_segment": coverage["retrieval_coverage"]["locators_without_u02_segment"],
            "production_recovery_limit": diagnostics["configuration"]["max_automatic_attempts"],
            "real_reexecution_equivalent": reexecution_equivalent,
            "publication_authorized": consolidation["publication_authorized"],
            "deliverables": output_hashes,
            "validation_diagnostics": validation_diagnostics,
            "relation_diagnostics": relation_errors,
        },
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u02-manifest", required=True)
    parser.add_argument("--segments", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--u03", required=True)
    parser.add_argument("--baseline-summary")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = verify(
        Path(args.u02_manifest).resolve(),
        Path(args.segments).resolve(),
        Path(args.source).resolve(),
        Path(args.u03).resolve(),
        Path(args.baseline_summary).resolve() if args.baseline_summary else None,
    )
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8", newline="\n")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
