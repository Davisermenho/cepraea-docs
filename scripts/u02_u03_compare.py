#!/usr/bin/env python3
"""Compare historical and corrected U02/U03 outputs deterministically."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def segment_key(segment: dict[str, Any]) -> tuple[Any, ...]:
    location = segment["location"]
    return (
        segment["source_path"],
        location["unit_id"],
        location["unit_char_start"],
        location["unit_char_end"],
        segment["text_sha256"],
    )


def coverage(manifest: dict[str, Any], segments: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for segment in segments:
        grouped[(segment["source_path"], segment["location"]["unit_id"])].append(segment)
    failed_units: list[dict[str, Any]] = []
    total_gap_chars = 0
    total_overlap_chars = 0
    unit_count = 0
    for extraction in manifest["extractions"]:
        for unit in extraction["units"]:
            unit_count += 1
            text = unit["text"]
            ordered = sorted(
                grouped.get((extraction["source_path"], unit["unit_id"]), []),
                key=lambda item: (
                    item["location"]["unit_char_start"],
                    item["location"]["unit_char_end"],
                ),
            )
            cursor = 0
            gaps = 0
            overlaps = 0
            for segment in ordered:
                start = segment["location"]["unit_char_start"]
                end = segment["location"]["unit_char_end"]
                if start > cursor:
                    gaps += start - cursor
                elif start < cursor:
                    overlaps += cursor - start
                cursor = max(cursor, end)
            if cursor < len(text):
                gaps += len(text) - cursor
            reconstructed = "".join(item["text"] for item in ordered)
            exact = reconstructed == text
            total_gap_chars += gaps
            total_overlap_chars += overlaps
            if gaps or overlaps or not exact:
                failed_units.append(
                    {
                        "source_path": extraction["source_path"],
                        "unit_id": unit["unit_id"],
                        "text_length_characters": len(text),
                        "gap_characters": gaps,
                        "overlap_characters": overlaps,
                        "exact_reconstruction": exact,
                    }
                )
    return {
        "units": unit_count,
        "failed_units": len(failed_units),
        "gap_characters": total_gap_chars,
        "overlap_characters": total_overlap_chars,
        "details": failed_units,
    }


def reference_key(reference: dict[str, Any]) -> tuple[Any, ...]:
    return (
        reference["source_path"],
        reference["reference_type"],
        reference.get("literal_target"),
        reference["target_path"],
        reference["resolution_status"],
    )


def counter_delta(
    old: Counter[tuple[Any, ...]],
    new: Counter[tuple[Any, ...]],
    increase: bool,
) -> list[dict[str, Any]]:
    values = []
    keys = set(old) | set(new)
    selected = [
        key for key in keys
        if (new[key] > old[key] if increase else new[key] < old[key])
    ]
    for key in sorted(selected):
        values.append(
            {
                "source_path": key[0],
                "reference_type": key[1],
                "literal_target": key[2],
                "target_path": key[3],
                "resolution_status": key[4],
                "old_count": old[key],
                "new_count": new[key],
                "delta": new[key] - old[key],
            }
        )
    return values


def compare(args: argparse.Namespace) -> dict[str, Any]:
    old_u02 = Path(args.old_u02)
    new_u02 = Path(args.new_u02)
    old_u03 = Path(args.old_u03)
    new_u03 = Path(args.new_u03)
    old_manifest = load_json(old_u02 / "U02-extraction-manifest.json")
    new_manifest = load_json(new_u02 / "U02-extraction-manifest.json")
    old_segments = load_jsonl(old_u02 / "U02-segments.jsonl")
    new_segments = load_jsonl(new_u02 / "U02-segments.jsonl")
    old_references = load_jsonl(old_u02 / "U02-references.jsonl")
    new_references = load_jsonl(new_u02 / "U02-references.jsonl")
    old_claims = load_jsonl(old_u03 / "generated/U03-claims-accepted.jsonl")
    new_claims = load_jsonl(new_u03 / "generated/U03-claims-accepted.jsonl")

    old_content_hashes = {
        item["source_path"]: item["extracted_content_sha256"] for item in old_manifest["extractions"]
    }
    new_content_hashes = {
        item["source_path"]: item["extracted_content_sha256"] for item in new_manifest["extractions"]
    }
    content_hash_changes = sorted(
        path
        for path in set(old_content_hashes) | set(new_content_hashes)
        if old_content_hashes.get(path) != new_content_hashes.get(path)
    )

    old_keys = {segment_key(item): item["segment_id"] for item in old_segments}
    new_keys = {segment_key(item): item["segment_id"] for item in new_segments}
    exact_keys = set(old_keys) & set(new_keys)
    old_only = set(old_keys) - set(new_keys)
    new_only = set(new_keys) - set(old_keys)
    changed_sources = sorted({key[0] for key in old_only | new_only})
    old_coverage = coverage(old_manifest, old_segments)
    new_coverage = coverage(new_manifest, new_segments)

    old_reference_counter = Counter(reference_key(item) for item in old_references)
    new_reference_counter = Counter(reference_key(item) for item in new_references)
    increased_references = counter_delta(old_reference_counter, new_reference_counter, True)
    decreased_references = counter_delta(old_reference_counter, new_reference_counter, False)

    old_claims_by_id = {item["claim_id"]: item for item in old_claims}
    new_claims_by_id = {item["claim_id"]: item for item in new_claims}
    claim_ids_changed = sorted(set(old_claims_by_id) ^ set(new_claims_by_id))
    affected_claims: list[dict[str, Any]] = []
    locator_only_resolved: list[str] = []
    old_segment_ids = {item["segment_id"] for item in old_segments}
    stale_segment_ids_reused: list[str] = []
    for claim_id in sorted(set(old_claims_by_id) & set(new_claims_by_id)):
        old = old_claims_by_id[claim_id]
        new = new_claims_by_id[claim_id]
        old_source = old["source"]
        new_source = new["source"]
        reasons = []
        if old_source["extraction_id"] != new_source["extraction_id"]:
            reasons.append("EXTRACTION_VERSION_REFERENCE_CHANGED")
        if old_source["segment_id"] != new_source["segment_id"]:
            reasons.append("SEGMENT_REFERENCE_CHANGED")
        if old_source["segment_id"] is None and new_source["segment_id"] is not None:
            reasons.append("PREVIOUS_LOCATOR_ONLY_NOW_SEGMENTED")
            locator_only_resolved.append(claim_id)
        if reasons:
            affected_claims.append(
                {
                    "claim_id": claim_id,
                    "reasons": reasons,
                    "old_extraction_id": old_source["extraction_id"],
                    "new_extraction_id": new_source["extraction_id"],
                    "old_segment_id": old_source["segment_id"],
                    "new_segment_id": new_source["segment_id"],
                }
            )
        if new_source["segment_id"] in old_segment_ids:
            stale_segment_ids_reused.append(claim_id)

    new_u03_summary = load_json(new_u03 / "evidence/U03-run-summary.json")
    passed = (
        not content_hash_changes
        and new_coverage["failed_units"] == 0
        and new_coverage["gap_characters"] == 0
        and new_coverage["overlap_characters"] == 0
        and not claim_ids_changed
        and not stale_segment_ids_reused
        and new_u03_summary["locators_without_u02_segment"] == 0
        and new_u03_summary["status"] == "PASS"
    )
    return {
        "schema_version": "1.0.0",
        "status": "PASS" if passed else "FAIL",
        "u02": {
            "old_extraction_version": old_manifest["extraction_version"],
            "new_extraction_version": new_manifest["extraction_version"],
            "source_count": len(new_manifest["extractions"]),
            "extracted_content_hash_changes": content_hash_changes,
            "old_segment_count": len(old_segments),
            "new_segment_count": len(new_segments),
            "logically_unchanged_segments_with_new_ids": len(exact_keys),
            "old_only_logical_segments": len(old_only),
            "new_only_logical_segments": len(new_only),
            "sources_with_segmentation_changes": changed_sources,
            "old_partition_coverage": old_coverage,
            "new_partition_coverage": new_coverage,
        },
        "references": {
            "old_count": len(old_references),
            "new_count": len(new_references),
            "semantic_key_multiplicity_increases": increased_references,
            "semantic_key_multiplicity_decreases": decreased_references,
        },
        "u03": {
            "old_claim_count": len(old_claims),
            "new_claim_count": len(new_claims),
            "claim_id_set_changes": claim_ids_changed,
            "affected_claim_count": len(affected_claims),
            "affected_claims": affected_claims,
            "locator_only_resolved_claim_ids": locator_only_resolved,
            "stale_old_segment_ids_reused_by_claims": stale_segment_ids_reused,
            "new_locators_without_segment": new_u03_summary["locators_without_u02_segment"],
            "new_run_status": new_u03_summary["status"],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-u02", required=True)
    parser.add_argument("--new-u02", required=True)
    parser.add_argument("--old-u03", required=True)
    parser.add_argument("--new-u03", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = compare(args)
    write_json(Path(args.output), result)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
