#!/usr/bin/env python3
"""Execute predeclared U02 controlled tests."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import tempfile
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any, Callable


REPOSITORY = Path(__file__).resolve().parents[2]
PLAN_PATH = Path(__file__).with_name("test_cases.json")
MODULE_PATH = REPOSITORY / "scripts" / "u02_extract.py"


def load_module():
    spec = importlib.util.spec_from_file_location("u02_extract", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


U02 = load_module()


def load_plan() -> dict[str, Any]:
    return json.loads(PLAN_PATH.read_text(encoding="utf-8"))


def definition(plan: dict[str, Any], test_id: str) -> dict[str, Any]:
    return next(item for item in plan["tests"] if item["id"] == test_id)


def test_result(specification: dict[str, Any], actual: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": specification["id"],
        "name": specification["name"],
        "status": "PASS" if actual == specification["expected"] else "FAIL",
        "input": specification["input"],
        "expected": specification["expected"],
        "actual": actual,
    }


def source_record(path: Path, root: Path, format_name: str, number: int = 1) -> dict[str, Any]:
    return {
        "source_id": f"SRC-TEST-{number:04d}",
        "relative_path": path.relative_to(root).as_posix(),
        "format": format_name,
        "sha256": U02.sha256_file(path),
    }


def write_text_file(root: Path, relative: str, text: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path


def make_pdf(path: Path, marker: str) -> None:
    escaped = marker.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    stream = f"BT /F1 18 Tf 72 720 Td ({escaped}) Tj ET\n".encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"endstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    content = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(content))
        content.extend(f"{number} 0 obj\n".encode("ascii"))
        content.extend(obj)
        content.extend(b"\nendobj\n")
    xref = len(content)
    content.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    content.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        content.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    content.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode("ascii")
    )
    path.write_bytes(bytes(content))


def make_pptx(path: Path, marker: str) -> None:
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="xml" ContentType="application/xml"/>
</Types>"""
    presentation = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>"""
    slide = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:cSld><p:spTree><p:sp><p:txBody><a:p><a:r><a:t>{marker}</a:t></a:r></a:p></p:txBody></p:sp></p:spTree></p:cSld>
</p:sld>"""
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("ppt/presentation.xml", presentation)
        archive.writestr("ppt/slides/slide1.xml", slide)


def write_manifest(root: Path, specs: list[tuple[str, str]]) -> Path:
    records = [source_record(root / relative, root, format_name, number) for number, (relative, format_name) in enumerate(specs, start=1)]
    manifest = {
        "schema_version": "1.0.0",
        "unit": "U01",
        "source_root": str(root),
        "files": records,
    }
    path = root.parent / "manifest.json"
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def logical_hashes(output: Path) -> dict[str, str]:
    selected = [
        "U02-extraction-manifest.json",
        "U02-limitations.json",
        "U02-segmentation-validation.json",
        "U02-segments.jsonl",
        "U02-references.jsonl",
        "U02-format-summary.csv",
    ]
    result = {name: U02.sha256_file(output / name) for name in selected}
    for path in sorted((output / "extracted").rglob("*.txt")):
        result[path.relative_to(output).as_posix()] = U02.sha256_file(path)
    return result


def segments_for_text(root: Path, relative: str, text: str, number: int = 1) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    path = write_text_file(root, relative, text)
    extraction = U02.extract_source(path, source_record(path, root, "Markdown", number))
    return extraction, U02.build_segments([extraction])


def independent_partition_status(text: str, segments: list[dict[str, Any]]) -> str:
    ordered = sorted(segments, key=lambda item: item["location"]["unit_char_start"])
    ids = [item["segment_id"] for item in ordered]
    if not text:
        valid = not ordered
    else:
        intervals = [
            (item["location"]["unit_char_start"], item["location"]["unit_char_end"])
            for item in ordered
        ]
        valid = bool(ordered)
        valid = valid and intervals[0][0] == 0
        valid = valid and all(left[1] == right[0] for left, right in zip(intervals, intervals[1:]))
        valid = valid and intervals[-1][1] == len(text)
        valid = valid and "".join(item["text"] for item in ordered) == text
        valid = valid and all(end > start for start, end in intervals)
        valid = valid and all(len(item["text"]) <= U02.MAX_SEGMENT_CHARS for item in ordered)
    valid = valid and not [value for value, count in Counter(ids).items() if count > 1]
    return "PASS" if valid else "FAIL"


def run_partition_case(plan: dict[str, Any], test_id: str) -> dict[str, Any]:
    spec = definition(plan, test_id)
    text = spec["input"].get("text")
    if text is None:
        text = "x" * spec["input"]["long_prefix_chars"] + spec["input"]["suffix"]
    with tempfile.TemporaryDirectory(prefix=f"u02-{test_id.lower()}-") as temp:
        extraction, segments = segments_for_text(Path(temp), spec["input"]["path"], text)
        actual = {
            "partition_status": independent_partition_status(extraction["units"][0]["text"], segments),
            "segment_count": len(segments),
        }
        if "heading_paths" in spec["expected"]:
            actual["heading_paths"] = [item["heading_path"] for item in segments]
        if "maximum_segment_chars" in spec["expected"]:
            actual["maximum_segment_chars"] = max((len(item["text"]) for item in segments), default=0)
    return test_result(spec, actual)


def run_t27(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T27")
    statuses = []
    counts = []
    observed_maximum = 0
    with tempfile.TemporaryDirectory(prefix="u02-t27-") as temp:
        root = Path(temp)
        for number, length in enumerate(spec["input"]["lengths"], start=1):
            extraction, segments = segments_for_text(root, f"{spec['input']['path_prefix']}-{length}.md", "x" * length, number)
            statuses.append(independent_partition_status(extraction["units"][0]["text"], segments))
            counts.append(len(segments))
            observed_maximum = max(observed_maximum, *(len(item["text"]) for item in segments))
    actual = {
        "partition_status": "PASS" if all(item == "PASS" for item in statuses) else "FAIL",
        "segment_counts": counts,
        "maximum_segment_chars": observed_maximum,
    }
    return test_result(spec, actual)


def run_t28(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T28")
    with tempfile.TemporaryDirectory(prefix="u02-t28-") as temp:
        root = Path(temp)
        extraction, first = segments_for_text(root, spec["input"]["path"], spec["input"]["text"])
        _, second = segments_for_text(root, spec["input"]["path"], spec["input"]["text"])
        actual = {
            "partition_status": independent_partition_status(extraction["units"][0]["text"], first),
            "identical_records": first == second,
            "identical_ids": [item["segment_id"] for item in first] == [item["segment_id"] for item in second],
        }
    return test_result(spec, actual)


def run_t29(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T29")
    with tempfile.TemporaryDirectory(prefix="u02-t29-") as temp:
        root = Path(temp)
        stable_path = write_text_file(root, spec["input"]["stable_path"], spec["input"]["stable_text"])
        inserted_path = write_text_file(root, spec["input"]["inserted_path"], spec["input"]["inserted_text"])
        stable_extraction = U02.extract_source(stable_path, source_record(stable_path, root, "Markdown", 2))
        inserted_extraction = U02.extract_source(inserted_path, source_record(inserted_path, root, "Markdown", 1))
        alone = U02.build_segments([stable_extraction])
        after_insertion = [item for item in U02.build_segments([inserted_extraction, stable_extraction]) if item["source_path"] == spec["input"]["stable_path"]]
        ids = [item["segment_id"] for item in alone]
        actual = {
            "partition_status": independent_partition_status(stable_extraction["units"][0]["text"], alone),
            "stable_source_ids_unchanged": ids == [item["segment_id"] for item in after_insertion],
            "deterministic_id_format": bool(ids)
            and all(re.fullmatch(r"SEG-[0-9a-f]{64}", value) for value in ids),
        }
    return test_result(spec, actual)


def run_t30(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T30")
    with tempfile.TemporaryDirectory(prefix="u02-t30-") as temp:
        extraction, segments = segments_for_text(Path(temp), spec["input"]["path"], spec["input"]["text"])
        locations = [item["location"] for item in segments]
        actual = {
            "partition_status": independent_partition_status(extraction["units"][0]["text"], segments),
            "offset_unit": locations[0].get("offset_unit") if locations else None,
            "half_open_intervals": bool(locations) and all(item.get("interval_convention") == "HALF_OPEN_START_INCLUSIVE_END_EXCLUSIVE" for item in locations),
            "character_and_byte_lengths_differ": len(spec["input"]["text"]) != len(spec["input"]["text"].encode("utf-8")),
        }
    return test_result(spec, actual)


def run_t05(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T05")
    with tempfile.TemporaryDirectory(prefix="u02-t05-") as temp:
        root = Path(temp)
        path = write_text_file(root, spec["input"]["path"], spec["input"]["text"])
        extraction = U02.extract_source(path, source_record(path, root, "Markdown"))
        segment = U02.build_segments([extraction])[0]
        actual = U02.validate_segment(segment, extraction)
    return test_result(spec, actual)


def run_t06(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T06")
    with tempfile.TemporaryDirectory(prefix="u02-t06-") as temp:
        root = Path(temp)
        path = write_text_file(root, spec["input"]["path"], spec["input"]["text"])
        extraction = U02.extract_source(path, source_record(path, root, "Markdown"))
        segment = U02.build_segments([extraction])[0]
        segment["text"] = "Conteudo adulterado."
        actual = U02.validate_segment(segment, extraction)
    return test_result(spec, actual)


def run_t07(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T07")
    with tempfile.TemporaryDirectory(prefix="u02-t07-") as temp:
        root = Path(temp)
        path = write_text_file(root, spec["input"]["path"], spec["input"]["text"])
        extraction = U02.extract_source(path, source_record(path, root, "JSON"))
        actual = {
            "status": extraction["status"],
            "raw_text_preserved": extraction["rendered_text"] == spec["input"]["text"],
            "limitation_code": extraction["limitations"][0]["code"],
        }
    return test_result(spec, actual)


def run_t08(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T08")
    with tempfile.TemporaryDirectory(prefix="u02-t08-") as temp:
        root = Path(temp)
        path = write_text_file(root, spec["input"]["path"], spec["input"]["text"])
        extraction = U02.extract_source(path, source_record(path, root, "Markdown"))
        actual = {"authority_status": extraction["authority_status"]}
    return test_result(spec, actual)


def run_t10(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T10")
    required = ["segment_id", "source_path", "source_sha256", "extraction_id", "location", "text", "text_sha256"]
    with tempfile.TemporaryDirectory(prefix="u02-t10-") as temp:
        root = Path(temp)
        path = write_text_file(root, spec["input"]["path"], spec["input"]["text"])
        extraction = U02.extract_source(path, source_record(path, root, "Markdown"))
        segments = U02.build_segments([extraction])
        missing = sorted({field for segment in segments for field in required if field not in segment})
        actual = {
            "all_segments_traceable": bool(segments) and all(U02.validate_segment(segment, extraction)["valid"] for segment in segments),
            "required_fields_missing": missing,
        }
    return test_result(spec, actual)


def run_t13(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T13")
    with tempfile.TemporaryDirectory(prefix="u02-t13-") as temp:
        base = Path(temp)
        root = base / "source"
        output = base / "output"
        root.mkdir()
        formats = {"a.md": "Markdown", "b.json": "JSON"}
        for relative, text in spec["input"]["files"].items():
            write_text_file(root, relative, text)
        manifest = write_manifest(root, list(formats.items()))
        U02.run_pipeline(manifest, root, output)
        first = logical_hashes(output)
        U02.run_pipeline(manifest, root, output)
        second = logical_hashes(output)
        segments = [json.loads(line) for line in (output / "U02-segments.jsonl").read_text(encoding="utf-8").splitlines()]
        ids = [item["segment_id"] for item in segments]
        duplicates = sorted({value for value in ids if ids.count(value) > 1})
        actual = {"logical_outputs_equivalent": first == second, "duplicate_segment_ids": duplicates}
    return test_result(spec, actual)


def run_t14(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T14")
    with tempfile.TemporaryDirectory(prefix="u02-t14-") as temp:
        base = Path(temp)
        root = base / "source"
        output = base / "output"
        root.mkdir()
        output.mkdir()
        for relative, text in spec["input"]["files"].items():
            write_text_file(root, relative, text)
        manifest = write_manifest(root, [("a.txt", "Plain text")])
        (output / "U02-segments.jsonl").write_text('{"partial":true', encoding="utf-8")
        U02.run_pipeline(manifest, root, output)
        records = [json.loads(line) for line in (output / "U02-segments.jsonl").read_text(encoding="utf-8").splitlines()]
        actual = {
            "rerun_complete": (output / "U02-retrieval-index.sqlite").is_file() and len(records) == 1,
            "partial_record_retained": any("partial" in item for item in records),
        }
    return test_result(spec, actual)


def run_t17(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T17")
    with tempfile.TemporaryDirectory(prefix="u02-t17-") as temp:
        base = Path(temp)
        root = base / "source"
        output = base / "output"
        root.mkdir()
        specs: list[tuple[str, str]] = []
        for relative, text in spec["input"]["files"].items():
            write_text_file(root, relative, text)
            specs.append((relative, "Markdown"))
        manifest = write_manifest(root, specs)
        U02.run_pipeline(manifest, root, output)
        segments = [json.loads(line) for line in (output / "U02-segments.jsonl").read_text(encoding="utf-8").splitlines()]
        refs = [json.loads(line) for line in (output / "U02-references.jsonl").read_text(encoding="utf-8").splitlines()]
        search = U02.search_index(output / "U02-retrieval-index.sqlite", spec["input"]["query"], include_related=True)
        actual = {
            "source_locations_preserved": all(item["source_sha256"] and item["location"].get("line_start") for item in segments),
            "explicit_reference_target": next(item["target_path"] for item in refs if item["reference_type"] == "EXPLICIT_MARKDOWN_LINK"),
            "related_exception_retrieved": any("manutencao" in item["text"] for item in search["related_results"]),
            "absence_is_not_proof_of_absence": search["coverage"]["absence_is_not_proof_of_absence"],
            "inventoried_sources": search["coverage"]["inventoried_sources"],
            "processed_sources": search["coverage"]["processed_sources"],
        }
    return test_result(spec, actual)


def run_t19(plan: dict[str, Any]) -> dict[str, Any]:
    spec = definition(plan, "T19")
    with tempfile.TemporaryDirectory(prefix="u02-t19-") as temp:
        root = Path(temp)
        samples = [
            ("sample.md", "Markdown", "# MARKDOWN_CONTROL\n"),
            ("sample.txt", "Plain text", "TEXT_CONTROL\n"),
            ("sample-noext", "Plain text (detected)", "NOEXT_CONTROL\n"),
            ("sample.sql", "SQL", "SELECT 1 AS SQL_CONTROL;\n"),
            ("sample.json", "JSON", '{"marker":"JSON_CONTROL"}\n'),
            ("sample.yaml", "YAML", "marker: YAML_CONTROL\n"),
        ]
        records: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
        for number, (relative, format_name, text) in enumerate(samples, start=1):
            path = write_text_file(root, relative, text)
            record = source_record(path, root, format_name, number)
            records.append((format_name, U02.extract_source(path, record), record))
        pdf_path = root / "sample.pdf"
        make_pdf(pdf_path, "PDF_CONTROL")
        pdf_record = source_record(pdf_path, root, "PDF", 7)
        records.append(("PDF", U02.extract_source(pdf_path, pdf_record), pdf_record))
        pptx_path = root / "sample.pptx"
        make_pptx(pptx_path, "PPTX_CONTROL")
        pptx_record = source_record(pptx_path, root, "PowerPoint Open XML", 8)
        records.append(("PowerPoint Open XML", U02.extract_source(pptx_path, pptx_record), pptx_record))
        markers = spec["input"]["known_markers"]
        all_segments = U02.build_segments([item[1] for item in records])
        actual = {
            "all_formats_exercised": sorted(item[0] for item in records) == sorted(spec["input"]["formats"]),
            "markers_recovered": all(markers[name] in "\n".join(unit["text"] for unit in extraction["units"]) for name, extraction, _ in records),
            "locations_present": bool(all_segments) and all(segment["location"] for segment in all_segments),
            "losses_or_limitations_explicit": all(extraction["status"] == "COMPLETE" or bool(extraction["limitations"]) for _, extraction, _ in records),
        }
    return test_result(spec, actual)


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--output")
    args = cli.parse_args()
    plan = load_plan()
    runners: list[Callable[[dict[str, Any]], dict[str, Any]]] = [
        run_t05,
        run_t06,
        run_t07,
        run_t08,
        run_t10,
        run_t13,
        run_t14,
        run_t17,
        run_t19,
        lambda plan: run_partition_case(plan, "T20"),
        lambda plan: run_partition_case(plan, "T21"),
        lambda plan: run_partition_case(plan, "T22"),
        lambda plan: run_partition_case(plan, "T23"),
        lambda plan: run_partition_case(plan, "T24"),
        lambda plan: run_partition_case(plan, "T25"),
        lambda plan: run_partition_case(plan, "T26"),
        run_t27,
        run_t28,
        run_t29,
        run_t30,
    ]
    results = [runner(plan) for runner in runners]
    report = {
        "schema_version": "1.0.0",
        "unit": "U02",
        "plan": str(PLAN_PATH.relative_to(REPOSITORY)),
        "all_passed": all(item["status"] == "PASS" for item in results),
        "results": results,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8", newline="\n")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
