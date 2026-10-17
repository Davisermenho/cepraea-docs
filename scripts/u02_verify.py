#!/usr/bin/env python3
"""Cross-validate U02 outputs against the U01 manifest and current corpus."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

from u02_extract import validate_all_partitions, sha256_file, validate_segment


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def verify(u01_path: Path, u02_path: Path, source_root: Path) -> dict:
    u01 = load_json(u01_path)
    u02 = load_json(u02_path)
    output_root = u02_path.parent
    segments = load_jsonl(output_root / "U02-segments.jsonl")
    references = load_jsonl(output_root / "U02-references.jsonl")
    errors: list[str] = []

    u01_records = {item["relative_path"]: item for item in u01["files"]}
    extractions = {item["source_path"]: item for item in u02["extractions"]}
    if set(u01_records) != set(extractions):
        errors.append("SOURCE_COVERAGE_MISMATCH")

    for source_path, extraction in extractions.items():
        source = source_root / source_path
        if not source.is_file() or sha256_file(source) != extraction["source_sha256"]:
            errors.append(f"SOURCE_HASH_MISMATCH:{source_path}")
        extracted_path = output_root / extraction["extracted_content_path"]
        if not extracted_path.is_file() or sha256_file(extracted_path) != extraction["extracted_content_sha256"]:
            errors.append(f"EXTRACTED_CONTENT_HASH_MISMATCH:{source_path}")
        if extraction["status"] == "PARTIAL" and not extraction["limitations"]:
            errors.append(f"PARTIAL_WITHOUT_LIMITATION:{source_path}")
        if extraction["authority_status"] != "NOT_ASSESSED_U02":
            errors.append(f"AUTHORITY_WAS_ASSESSED:{source_path}")

    ids = [item["segment_id"] for item in segments]
    duplicate_ids = sorted(value for value, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        errors.append("DUPLICATE_SEGMENT_IDS:" + ",".join(duplicate_ids))

    invalid_segments = []
    for segment in segments:
        extraction = extractions.get(segment["source_path"])
        if extraction is None:
            invalid_segments.append({"segment_id": segment["segment_id"], "diagnostics": ["EXTRACTION_NOT_FOUND"]})
            continue
        validation = validate_segment(segment, extraction)
        if not validation["valid"]:
            invalid_segments.append({"segment_id": segment["segment_id"], **validation})
    if invalid_segments:
        errors.append(f"INVALID_SEGMENTS:{len(invalid_segments)}")

    partition_validation = validate_all_partitions(list(extractions.values()), segments)
    if partition_validation["status"] != "PASS":
        errors.append("SEGMENTATION_PARTITION_FAILED")
    persisted_partition_path = output_root / "U02-segmentation-validation.json"
    persisted_partition = load_json(persisted_partition_path) if persisted_partition_path.is_file() else None
    if persisted_partition != partition_validation:
        errors.append("SEGMENTATION_VALIDATION_RECORD_MISMATCH")

    resolved_bad_targets = [
        item["reference_id"]
        for item in references
        if item["resolution_status"] == "RESOLVED" and item["target_path"] not in extractions
    ]
    if resolved_bad_targets:
        errors.append("RESOLVED_REFERENCE_TARGET_MISSING:" + ",".join(resolved_bad_targets[:10]))

    index_path = output_root / "U02-retrieval-index.sqlite"
    connection = sqlite3.connect(index_path)
    try:
        indexed_segments = connection.execute("SELECT count(*) FROM segments").fetchone()[0]
        fts_segments = connection.execute("SELECT count(*) FROM segment_fts").fetchone()[0]
        indexed_references = connection.execute("SELECT count(*) FROM refs").fetchone()[0]
    finally:
        connection.close()
    if indexed_segments != len(segments) or fts_segments != len(segments):
        errors.append("INDEX_SEGMENT_COUNT_MISMATCH")
    if indexed_references != len(references):
        errors.append("INDEX_REFERENCE_COUNT_MISMATCH")

    statuses = Counter(item["status"] for item in extractions.values())
    limitation_codes = Counter(
        entry["code"]
        for extraction in extractions.values()
        for entry in extraction["limitations"]
    )
    return {
        "schema_version": "1.0.0",
        "unit": "U02",
        "status": "PASS" if not errors else "FAIL",
        "checks": {
            "u01_sources": len(u01_records),
            "u02_sources": len(extractions),
            "current_source_hashes_verified": len(extractions),
            "extracted_content_hashes_verified": len(extractions),
            "segments_validated": len(segments),
            "invalid_segments": invalid_segments[:20],
            "duplicate_segment_ids": duplicate_ids,
            "segmentation_partition": partition_validation["summary"],
            "offset_unit": partition_validation["offset_unit"],
            "interval_convention": partition_validation["interval_convention"],
            "references_validated": len(references),
            "sqlite_segment_rows": indexed_segments,
            "sqlite_fts_rows": fts_segments,
            "sqlite_reference_rows": indexed_references,
            "status_counts": dict(sorted(statuses.items())),
            "limitation_codes": dict(sorted(limitation_codes.items())),
        },
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u01-manifest", required=True)
    parser.add_argument("--u02-manifest", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = verify(Path(args.u01_manifest), Path(args.u02_manifest), Path(args.source).resolve())
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8", newline="\n")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
