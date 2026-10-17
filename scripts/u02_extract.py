#!/usr/bin/env python3
"""U02 deterministic extraction, segmentation and retrieval indexing.

The corpus is read-only. Outputs are written below an explicitly separate
directory. No document label is interpreted as authority.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import os
import posixpath
import re
import sqlite3
import subprocess
import sys
import urllib.parse
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from xml.etree import ElementTree


SCHEMA_VERSION = "1.1.0"
EXTRACTION_VERSION = "1.1.0"
MAX_SEGMENT_CHARS = 12_000
OFFSET_UNIT = "UNICODE_CODE_POINT"
INTERVAL_CONVENTION = "HALF_OPEN_START_INCLUSIVE_END_EXCLUSIVE"

TEXT_FORMATS = {
    "Markdown",
    "Plain text",
    "Plain text (detected)",
    "SQL",
    "JSON",
    "YAML",
}

EXTRACTORS = {
    "Markdown": "python-text-markdown-v1",
    "Plain text": "python-text-v1",
    "Plain text (detected)": "python-text-v1",
    "SQL": "python-text-sql-v1",
    "JSON": "python-json-raw-v1",
    "YAML": "python-yaml-text-v1",
    "PDF": "poppler-pdftotext-layout-v1",
    "PowerPoint Open XML": "python-ooxml-pptx-v1",
}

CONTEXT_PATTERNS = {
    "CONDITION_CANDIDATE": re.compile(r"\b(se|quando|condi(?:ç|c)[aã]o|aplica-se|aplicavel)\b", re.I),
    "EXCEPTION_CANDIDATE": re.compile(r"\b(exceto|exce(?:ç|c)[aã]o|salvo|ressalva)\b", re.I),
    "DEPENDENCY_CANDIDATE": re.compile(r"\b(depende|dependencia|requer|pre-requisito|pré-requisito)\b", re.I),
    "DEFINITION_CANDIDATE": re.compile(r"\b(define|definicao|defini(?:ç|c)[aã]o|significa|entende-se)\b", re.I),
    "DECISION_CHANGE_CANDIDATE": re.compile(r"\b(substitui|revoga|revogado|obsoleto|supersede)\b", re.I),
}


def json_dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extraction_id(record: dict[str, Any]) -> str:
    extractor = EXTRACTORS.get(record["format"], "unsupported-v1")
    stable = f"{record['source_id']}\0{record['sha256']}\0{extractor}\0{EXTRACTION_VERSION}"
    return "EXT-" + sha256_text(stable)[:20]


def limitation(code: str, detail: str, blocking: bool = False) -> dict[str, Any]:
    return {"code": code, "detail": detail, "blocking": blocking}


def text_result(path: Path, record: dict[str, Any]) -> dict[str, Any]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    limitations: list[dict[str, Any]] = []
    status = "COMPLETE"
    format_name = record["format"]
    structure = "lines"
    if format_name == "Markdown":
        structure = "markdown_headings_and_lines"
    elif format_name == "SQL":
        structure = "sql_text_and_lines"
    elif format_name == "JSON":
        structure = "json_and_lines"
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            status = "PARTIAL"
            limitations.append(
                limitation(
                    "JSON_SYNTAX_ERROR",
                    f"Raw UTF-8 text preserved; structured JSON parsing failed at line {exc.lineno}, column {exc.colno}: {exc.msg}",
                )
            )
            structure = "raw_text_fallback_lines"
    elif format_name == "YAML":
        status = "PARTIAL"
        structure = "raw_yaml_text_and_lines"
        limitations.append(
            limitation(
                "YAML_STRUCTURE_NOT_PARSED",
                "UTF-8 content and line locations preserved; YAML mapping/sequence tree was not parsed because no YAML dependency is available.",
            )
        )
    return {
        "status": status,
        "structure": structure,
        "units": [{"unit_id": "unit-1", "kind": "document", "ordinal": 1, "text": text}],
        "rendered_text": text,
        "limitations": limitations,
        "technical": {"encoding": "UTF-8", "byte_fidelity": sha256_bytes(raw) == sha256_text(text)},
    }


def poppler_version() -> str:
    completed = subprocess.run(
        ["pdftotext", "-v"], capture_output=True, text=True, timeout=10, check=False
    )
    output = (completed.stderr or completed.stdout).splitlines()
    return output[0].strip() if output else "pdftotext version unknown"


def pdf_result(path: Path, record: dict[str, Any]) -> dict[str, Any]:
    info = subprocess.run(
        ["pdfinfo", str(path)], capture_output=True, text=True, timeout=120, check=False
    )
    converted = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"],
        capture_output=True,
        timeout=300,
        check=False,
    )
    limitations = [
        limitation(
            "PDF_TEXT_LAYER_ONLY",
            "Text layer and page breaks were extracted; images, drawing semantics and exact visual layout were not OCRed or interpreted.",
        )
    ]
    if info.returncode != 0 or converted.returncode != 0:
        detail = (
            f"pdfinfo rc={info.returncode}: {info.stderr.strip()}; "
            f"pdftotext rc={converted.returncode}: {converted.stderr.decode('utf-8', errors='replace').strip()}"
        )
        return {
            "status": "FAILED",
            "structure": "pdf",
            "units": [],
            "rendered_text": "",
            "limitations": [limitation("PDF_EXTRACTION_ERROR", detail, True)],
            "technical": {"poppler": poppler_version()},
        }
    pages_match = re.search(r"^Pages:\s+(\d+)\s*$", info.stdout, re.MULTILINE)
    expected_pages = int(pages_match.group(1)) if pages_match else None
    text = converted.stdout.decode("utf-8", errors="replace")
    page_texts = text.split("\f")
    if page_texts and page_texts[-1] == "":
        page_texts.pop()
    if expected_pages is not None:
        if len(page_texts) < expected_pages:
            page_texts.extend([""] * (expected_pages - len(page_texts)))
        elif len(page_texts) > expected_pages:
            limitations.append(
                limitation(
                    "PDF_PAGE_COUNT_MISMATCH",
                    f"pdfinfo reported {expected_pages} pages while pdftotext produced {len(page_texts)} page blocks.",
                )
            )
    units = [
        {"unit_id": f"page-{number}", "kind": "page", "ordinal": number, "text": page_text}
        for number, page_text in enumerate(page_texts, start=1)
    ]
    empty_pages = [unit["ordinal"] for unit in units if not unit["text"].strip()]
    if empty_pages:
        limitations.append(
            limitation(
                "PDF_PAGES_WITHOUT_TEXT",
                "No text layer recovered for pages: " + ", ".join(map(str, empty_pages)),
            )
        )
    rendered = "".join(f"=== PAGE {unit['ordinal']} ===\n{unit['text']}\n" for unit in units)
    return {
        "status": "PARTIAL",
        "structure": "pdf_pages",
        "units": units,
        "rendered_text": rendered,
        "limitations": limitations,
        "technical": {
            "poppler": poppler_version(),
            "pdfinfo_page_count": expected_pages,
            "extracted_page_blocks": len(units),
        },
    }


def xml_paragraphs(xml_bytes: bytes) -> list[str]:
    root = ElementTree.fromstring(xml_bytes)
    paragraphs: list[str] = []
    for element in root.iter():
        if not element.tag.endswith("}p"):
            continue
        texts = [child.text or "" for child in element.iter() if child.tag.endswith("}t")]
        joined = "".join(texts).strip()
        if joined:
            paragraphs.append(joined)
    return paragraphs


def numbered_members(names: Iterable[str], pattern: re.Pattern[str]) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    for name in names:
        match = pattern.fullmatch(name)
        if match:
            result.append((int(match.group(1)), name))
    return sorted(result)


def pptx_result(path: Path, record: dict[str, Any]) -> dict[str, Any]:
    slide_pattern = re.compile(r"ppt/slides/slide(\d+)\.xml")
    notes_pattern = re.compile(r"ppt/notesSlides/notesSlide(\d+)\.xml")
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            slide_members = numbered_members(names, slide_pattern)
            note_members = dict(numbered_members(names, notes_pattern))
            units: list[dict[str, Any]] = []
            for number, member in slide_members:
                paragraphs = xml_paragraphs(archive.read(member))
                units.append(
                    {
                        "unit_id": f"slide-{number}",
                        "kind": "slide",
                        "ordinal": number,
                        "text": "\n".join(paragraphs),
                    }
                )
                note_member = note_members.get(number)
                if note_member:
                    notes = xml_paragraphs(archive.read(note_member))
                    # Numeric-only placeholders are slide numbers, not authored notes.
                    notes = [value for value in notes if not value.isdigit()]
                    if notes:
                        units.append(
                            {
                                "unit_id": f"slide-{number}-notes",
                                "kind": "slide_notes",
                                "ordinal": number,
                                "text": "\n".join(notes),
                            }
                        )
            media_count = sum(name.startswith("ppt/media/") for name in names)
            limitations = [
                limitation(
                    "PPTX_VISUAL_CONTENT_NOT_INTERPRETED",
                    f"Recovered OOXML text for slides/notes; {media_count} media assets plus layout, animation, chart and visual meaning were not interpreted.",
                )
            ]
            empty_slides = [
                unit["ordinal"]
                for unit in units
                if unit["kind"] == "slide" and not unit["text"].strip()
            ]
            if empty_slides:
                limitations.append(
                    limitation(
                        "PPTX_SLIDES_WITHOUT_TEXT",
                        "No OOXML text recovered for slides: " + ", ".join(map(str, empty_slides)),
                    )
                )
            rendered_parts = []
            for unit in units:
                marker = "SLIDE" if unit["kind"] == "slide" else "SLIDE NOTES"
                rendered_parts.append(f"=== {marker} {unit['ordinal']} ===\n{unit['text']}\n")
            return {
                "status": "PARTIAL",
                "structure": "pptx_slides_and_notes",
                "units": units,
                "rendered_text": "".join(rendered_parts),
                "limitations": limitations,
                "technical": {
                    "slide_count": len(slide_members),
                    "notes_part_count": len(note_members),
                    "media_asset_count": media_count,
                },
            }
    except (OSError, zipfile.BadZipFile, ElementTree.ParseError) as exc:
        return {
            "status": "FAILED",
            "structure": "pptx",
            "units": [],
            "rendered_text": "",
            "limitations": [limitation("PPTX_EXTRACTION_ERROR", f"{type(exc).__name__}: {exc}", True)],
            "technical": {},
        }


def extract_source(path: Path, record: dict[str, Any]) -> dict[str, Any]:
    extractor = EXTRACTORS.get(record["format"])
    base = {
        "extraction_id": extraction_id(record),
        "extraction_version": EXTRACTION_VERSION,
        "source_id": record["source_id"],
        "source_path": record["relative_path"],
        "source_sha256": record["sha256"],
        "format": record["format"],
        "extractor_id": extractor,
        "authority_status": "NOT_ASSESSED_U02",
    }
    actual_hash = sha256_file(path)
    if actual_hash != record["sha256"]:
        return base | {
            "status": "FAILED",
            "structure": "not_extracted",
            "units": [],
            "rendered_text": "",
            "limitations": [
                limitation(
                    "SOURCE_HASH_MISMATCH",
                    f"Manifest={record['sha256']} actual={actual_hash}",
                    True,
                )
            ],
            "technical": {},
        }
    try:
        if record["format"] in TEXT_FORMATS:
            extracted = text_result(path, record)
        elif record["format"] == "PDF":
            extracted = pdf_result(path, record)
        elif record["format"] == "PowerPoint Open XML":
            extracted = pptx_result(path, record)
        else:
            extracted = {
                "status": "FAILED",
                "structure": "unsupported",
                "units": [],
                "rendered_text": "",
                "limitations": [
                    limitation("UNSUPPORTED_FORMAT", f"No extractor for {record['format']}", True)
                ],
                "technical": {},
            }
    except (OSError, UnicodeError) as exc:
        extracted = {
            "status": "FAILED",
            "structure": "extraction_error",
            "units": [],
            "rendered_text": "",
            "limitations": [limitation("EXTRACTION_ERROR", f"{type(exc).__name__}: {exc}", True)],
            "technical": {},
        }
    return base | extracted


def line_starts(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))
    return starts


def line_column(starts: list[int], offset: int) -> tuple[int, int]:
    index = bisect.bisect_right(starts, offset) - 1
    return index + 1, offset - starts[index] + 1


def split_span(text: str, start: int, end: int, maximum: int) -> list[tuple[int, int]]:
    if maximum <= 0:
        raise ValueError("maximum segment size must be positive")
    if start < 0 or end < start or end > len(text):
        raise ValueError(f"invalid span [{start}, {end}) for text length {len(text)}")
    spans: list[tuple[int, int]] = []
    cursor = start
    while end - cursor > maximum:
        candidate = text.rfind("\n", cursor, cursor + maximum)
        if candidate <= cursor:
            candidate = cursor + maximum
        else:
            candidate += 1
        spans.append((cursor, candidate))
        cursor = candidate
    if cursor < end:
        spans.append((cursor, end))
    return spans


def generic_spans(text: str) -> list[tuple[int, int, list[str]]]:
    if not text:
        return []
    # Blank-line separators belong to the preceding block. The resulting raw
    # blocks are therefore a complete, non-overlapping partition of the text.
    blocks: list[tuple[int, int]] = []
    cursor = 0
    for separator in re.finditer(r"\n[ \t]*\n+", text):
        end = separator.end()
        blocks.append((cursor, end))
        cursor = end
    if cursor < len(text):
        blocks.append((cursor, len(text)))
    if not blocks:
        blocks = [(0, len(text))]
    combined: list[tuple[int, int, list[str]]] = []
    current_start: int | None = None
    current_end = 0
    for start, end in blocks:
        if current_start is None:
            current_start, current_end = start, end
        elif end - current_start <= MAX_SEGMENT_CHARS:
            current_end = end
        else:
            for left, right in split_span(text, current_start, current_end, MAX_SEGMENT_CHARS):
                combined.append((left, right, []))
            current_start, current_end = start, end
    if current_start is not None:
        for left, right in split_span(text, current_start, current_end, MAX_SEGMENT_CHARS):
            combined.append((left, right, []))
    return combined


def markdown_spans(text: str) -> list[tuple[int, int, list[str]]]:
    if not text:
        return []
    lines = text.splitlines(keepends=True)
    headings: list[str] = []
    heading_records: list[tuple[int, list[str]]] = []
    offset = 0
    fence_character: str | None = None
    fence_length = 0
    for line in lines:
        content = line.rstrip("\r\n")
        fence = re.match(r"^[ ]{0,3}(`{3,}|~{3,})(.*)$", content)
        if fence:
            marker = fence.group(1)
            remainder = fence.group(2)
            if fence_character is None:
                fence_character = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_character and len(marker) >= fence_length and not remainder.strip():
                fence_character = None
                fence_length = 0
            offset += len(line)
            continue
        match = None
        if fence_character is None:
            match = re.match(r"^[ \t]{0,3}(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", content)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headings = headings[: level - 1]
            while len(headings) < level - 1:
                headings.append("")
            headings.append(title)
            heading_records.append((offset, list(headings)))
        offset += len(line)
    if not heading_records:
        return generic_spans(text)

    sections: list[tuple[int, int, list[str]]] = []
    first_heading_offset = heading_records[0][0]
    if first_heading_offset > 0:
        sections.append((0, first_heading_offset, []))
    for index, (start, heading_path) in enumerate(heading_records):
        end = heading_records[index + 1][0] if index + 1 < len(heading_records) else len(text)
        sections.append((start, end, heading_path))

    result: list[tuple[int, int, list[str]]] = []
    for start, end, heading in sections:
        for left, right in split_span(text, start, end, MAX_SEGMENT_CHARS):
            result.append((left, right, heading))
    return result


def context_markers(text: str) -> list[str]:
    return sorted(name for name, pattern in CONTEXT_PATTERNS.items() if pattern.search(text))


def segment_identifier(
    extraction: dict[str, Any],
    unit: dict[str, Any],
    start: int,
    end: int,
    segment_text: str,
) -> str:
    identity = {
        "source_id": extraction["source_id"],
        "source_path": extraction["source_path"],
        "source_sha256": extraction["source_sha256"],
        "extraction_id": extraction["extraction_id"],
        "unit_id": unit["unit_id"],
        "unit_kind": unit["kind"],
        "unit_ordinal": unit["ordinal"],
        "unit_char_start": start,
        "unit_char_end": end,
        "text_sha256": sha256_text(segment_text),
    }
    stable = json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "SEG-" + sha256_text(stable)


def build_segments(extractions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    segments: list[dict[str, Any]] = []
    for extraction in extractions:
        for unit in extraction["units"]:
            text = unit["text"]
            spans = (
                markdown_spans(text)
                if extraction["format"] == "Markdown" and unit["kind"] == "document"
                else generic_spans(text)
            )
            starts = line_starts(text)
            for start, end, heading_path in spans:
                segment_text = text[start:end]
                line_start, column_start = line_column(starts, start)
                line_end, column_end = line_column(starts, max(start, end - 1))
                location: dict[str, Any] = {
                    "kind": "line_range",
                    "unit_id": unit["unit_id"],
                    "unit_kind": unit["kind"],
                    "unit_ordinal": unit["ordinal"],
                    "line_start": line_start,
                    "column_start": column_start,
                    "line_end": line_end,
                    "column_end": column_end,
                    "unit_char_start": start,
                    "unit_char_end": end,
                    "offset_unit": OFFSET_UNIT,
                    "interval_convention": INTERVAL_CONVENTION,
                }
                if unit["kind"] == "page":
                    location["page"] = unit["ordinal"]
                elif unit["kind"] in {"slide", "slide_notes"}:
                    location["slide"] = unit["ordinal"]
                    location["component"] = unit["kind"]
                segments.append(
                    {
                        "schema_version": SCHEMA_VERSION,
                        "segment_id": segment_identifier(extraction, unit, start, end, segment_text),
                        "source_id": extraction["source_id"],
                        "source_path": extraction["source_path"],
                        "source_sha256": extraction["source_sha256"],
                        "extraction_id": extraction["extraction_id"],
                        "extraction_version": extraction["extraction_version"],
                        "extractor_id": extraction["extractor_id"],
                        "extraction_status": extraction["status"],
                        "location": location,
                        "heading_path": heading_path,
                        "text": segment_text,
                        "text_sha256": sha256_text(segment_text),
                        "context_markers": context_markers(segment_text),
                        "context_marker_status": "LEXICAL_CANDIDATES_NOT_SEMANTICALLY_VALIDATED",
                        "authority_status": "NOT_ASSESSED_U02",
                    }
                )
    return segments


def validate_unit_partition(
    unit: dict[str, Any],
    segments: list[dict[str, Any]],
    maximum: int = MAX_SEGMENT_CHARS,
) -> dict[str, Any]:
    """Validate a character-based, half-open, exact partition of one unit."""
    text = unit["text"]
    ordered = sorted(
        segments,
        key=lambda item: (
            item.get("location", {}).get("unit_char_start", -1),
            item.get("location", {}).get("unit_char_end", -1),
            item.get("segment_id", ""),
        ),
    )
    diagnostics: list[str] = []
    ids = [item.get("segment_id") for item in ordered]
    duplicate_ids = sorted(value for value, count in Counter(ids).items() if value is not None and count > 1)
    if duplicate_ids:
        diagnostics.append("DUPLICATE_SEGMENT_IDS")

    if not text:
        if ordered:
            diagnostics.append("EMPTY_UNIT_HAS_SEGMENTS")
        reconstructed = "".join(str(item.get("text", "")) for item in ordered)
        return {
            "status": "PASS" if not diagnostics and reconstructed == text else "FAIL",
            "unit_id": unit["unit_id"],
            "text_length_characters": 0,
            "segment_count": len(ordered),
            "first_interval_starts_at_zero": not ordered,
            "adjacent_intervals": True,
            "last_interval_ends_at_text_length": not ordered,
            "exact_reconstruction": reconstructed == text,
            "unique_segment_ids": not duplicate_ids,
            "maximum_segment_chars_respected": True,
            "offset_unit": OFFSET_UNIT,
            "interval_convention": INTERVAL_CONVENTION,
            "diagnostics": diagnostics,
        }

    if not ordered:
        diagnostics.append("NONEMPTY_UNIT_WITHOUT_SEGMENTS")
    intervals: list[tuple[int, int]] = []
    conventions_valid = True
    size_valid = True
    for segment in ordered:
        location = segment.get("location", {})
        start = location.get("unit_char_start")
        end = location.get("unit_char_end")
        if not isinstance(start, int) or not isinstance(end, int) or not (0 <= start < end <= len(text)):
            diagnostics.append("INVALID_INTERVAL")
            continue
        intervals.append((start, end))
        conventions_valid = conventions_valid and location.get("offset_unit") == OFFSET_UNIT
        conventions_valid = conventions_valid and location.get("interval_convention") == INTERVAL_CONVENTION
        size_valid = size_valid and end - start <= maximum and len(segment.get("text", "")) <= maximum
    first_zero = bool(intervals) and intervals[0][0] == 0
    adjacent = len(intervals) == len(ordered) and all(
        left[1] == right[0] for left, right in zip(intervals, intervals[1:])
    )
    last_at_end = bool(intervals) and intervals[-1][1] == len(text)
    reconstructed = "".join(str(item.get("text", "")) for item in ordered)
    exact = reconstructed == text
    if not first_zero:
        diagnostics.append("FIRST_INTERVAL_NOT_ZERO")
    if not adjacent:
        diagnostics.append("INTERVAL_GAP_OR_OVERLAP")
    if not last_at_end:
        diagnostics.append("LAST_INTERVAL_NOT_TEXT_LENGTH")
    if not exact:
        diagnostics.append("RECONSTRUCTION_MISMATCH")
    if not conventions_valid:
        diagnostics.append("OFFSET_CONVENTION_MISMATCH")
    if not size_valid:
        diagnostics.append("MAXIMUM_SEGMENT_CHARS_EXCEEDED")
    return {
        "status": "PASS" if not diagnostics else "FAIL",
        "unit_id": unit["unit_id"],
        "text_length_characters": len(text),
        "segment_count": len(ordered),
        "first_interval_starts_at_zero": first_zero,
        "adjacent_intervals": adjacent,
        "last_interval_ends_at_text_length": last_at_end,
        "exact_reconstruction": exact,
        "unique_segment_ids": not duplicate_ids,
        "maximum_segment_chars_respected": size_valid,
        "offset_unit": OFFSET_UNIT if conventions_valid else "INVALID_OR_MIXED",
        "interval_convention": INTERVAL_CONVENTION if conventions_valid else "INVALID_OR_MIXED",
        "diagnostics": diagnostics,
    }


def validate_all_partitions(
    extractions: list[dict[str, Any]], segments: list[dict[str, Any]]
) -> dict[str, Any]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for segment in segments:
        key = (segment["extraction_id"], segment["location"]["unit_id"])
        grouped.setdefault(key, []).append(segment)
    results: list[dict[str, Any]] = []
    expected_keys: set[tuple[str, str]] = set()
    for extraction in extractions:
        for unit in extraction["units"]:
            key = (extraction["extraction_id"], unit["unit_id"])
            expected_keys.add(key)
            result = validate_unit_partition(unit, grouped.get(key, []))
            results.append(
                {
                    "source_path": extraction["source_path"],
                    "extraction_id": extraction["extraction_id"],
                    **result,
                }
            )
    orphan_keys = sorted(set(grouped) - expected_keys)
    global_ids = [item["segment_id"] for item in segments]
    duplicate_global_ids = sorted(value for value, count in Counter(global_ids).items() if count > 1)
    failed = [item for item in results if item["status"] != "PASS"]
    status = "PASS" if not failed and not orphan_keys and not duplicate_global_ids else "FAIL"
    return {
        "schema_version": SCHEMA_VERSION,
        "unit": "U02",
        "status": status,
        "offset_unit": OFFSET_UNIT,
        "interval_convention": INTERVAL_CONVENTION,
        "maximum_segment_chars": MAX_SEGMENT_CHARS,
        "summary": {
            "units_validated": len(results),
            "nonempty_units": sum(item["text_length_characters"] > 0 for item in results),
            "empty_units": sum(item["text_length_characters"] == 0 for item in results),
            "segments_validated": len(segments),
            "failed_units": len(failed),
            "orphan_segment_groups": len(orphan_keys),
            "duplicate_segment_ids": duplicate_global_ids,
        },
        "orphan_segment_groups": [list(item) for item in orphan_keys],
        "results": results,
    }


def validate_segment(segment: dict[str, Any], extraction: dict[str, Any]) -> dict[str, Any]:
    required = [
        "segment_id",
        "source_path",
        "source_sha256",
        "extraction_id",
        "location",
        "text",
        "text_sha256",
    ]
    missing = [field for field in required if field not in segment]
    if missing:
        return {"valid": False, "diagnostics": ["MISSING_FIELDS:" + ",".join(missing)]}
    if sha256_text(segment["text"]) != segment["text_sha256"]:
        return {"valid": False, "diagnostics": ["SEGMENT_TEXT_SHA256_MISMATCH"]}
    diagnostics: list[str] = []
    if segment["source_path"] != extraction["source_path"]:
        diagnostics.append("SOURCE_PATH_MISMATCH")
    if segment["source_sha256"] != extraction["source_sha256"]:
        diagnostics.append("SOURCE_SHA256_MISMATCH")
    if segment["extraction_id"] != extraction["extraction_id"]:
        diagnostics.append("EXTRACTION_ID_MISMATCH")
    location = segment["location"]
    unit = next(
        (item for item in extraction["units"] if item["unit_id"] == location.get("unit_id")),
        None,
    )
    if unit is None:
        diagnostics.append("UNIT_NOT_FOUND")
    else:
        start = location.get("unit_char_start")
        end = location.get("unit_char_end")
        if location.get("offset_unit") != OFFSET_UNIT or location.get("interval_convention") != INTERVAL_CONVENTION:
            diagnostics.append("OFFSET_CONVENTION_MISMATCH")
        if not isinstance(start, int) or not isinstance(end, int) or not (0 <= start < end <= len(unit["text"])) or unit["text"][start:end] != segment["text"]:
            diagnostics.append("LOCATION_TEXT_MISMATCH")
        elif segment["segment_id"] != segment_identifier(extraction, unit, start, end, segment["text"]):
            diagnostics.append("SEGMENT_ID_MISMATCH")
    return {"valid": not diagnostics, "diagnostics": diagnostics}


def build_references(segments: list[dict[str, Any]], source_paths: set[str]) -> list[dict[str, Any]]:
    references: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    markdown_link = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    basenames = sorted(
        ((PurePosixPath(path).name, path) for path in source_paths),
        key=lambda item: (-len(item[0]), item[0]),
    )
    for segment in segments:
        text = segment["text"]
        source_path = segment["source_path"]
        for match in markdown_link.finditer(text):
            raw_target = match.group(1).strip().split()[0].strip("<>")
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            decoded = urllib.parse.unquote(raw_target.split("#", 1)[0])
            target = posixpath.normpath(posixpath.join(posixpath.dirname(source_path), decoded))
            key = (segment["segment_id"], "EXPLICIT_MARKDOWN_LINK", target)
            if key in seen:
                continue
            seen.add(key)
            references.append(
                {
                    "reference_id": f"REF-{len(references) + 1:08d}",
                    "segment_id": segment["segment_id"],
                    "source_path": source_path,
                    "location": segment["location"],
                    "reference_type": "EXPLICIT_MARKDOWN_LINK",
                    "literal_target": raw_target,
                    "target_path": target,
                    "resolution_status": "RESOLVED" if target in source_paths else "UNRESOLVED",
                }
            )
        for basename, target_path in basenames:
            if target_path == source_path or len(basename) < 6 or basename not in text:
                continue
            key = (segment["segment_id"], "EXPLICIT_FILENAME_MENTION", target_path)
            if key in seen:
                continue
            seen.add(key)
            references.append(
                {
                    "reference_id": f"REF-{len(references) + 1:08d}",
                    "segment_id": segment["segment_id"],
                    "source_path": source_path,
                    "location": segment["location"],
                    "reference_type": "EXPLICIT_FILENAME_MENTION",
                    "literal_target": basename,
                    "target_path": target_path,
                    "resolution_status": "RESOLVED",
                }
            )
    return references


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    os.replace(temporary, path)


def build_sqlite_index(
    path: Path,
    segments: list[dict[str, Any]],
    references: list[dict[str, Any]],
    inventoried_sources: int,
    processed_sources: int,
) -> None:
    temporary = path.with_name(path.name + ".tmp")
    if temporary.exists():
        temporary.unlink()
    connection = sqlite3.connect(temporary)
    try:
        connection.executescript(
            """
            PRAGMA journal_mode=OFF;
            PRAGMA synchronous=OFF;
            CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE segments (
                segment_id TEXT PRIMARY KEY,
                source_path TEXT NOT NULL,
                source_sha256 TEXT NOT NULL,
                extraction_id TEXT NOT NULL,
                location_json TEXT NOT NULL,
                heading_path TEXT NOT NULL,
                context_markers TEXT NOT NULL,
                text TEXT NOT NULL
            );
            CREATE VIRTUAL TABLE segment_fts USING fts5(
                segment_id UNINDEXED,
                text,
                heading_path,
                tokenize='unicode61 remove_diacritics 2'
            );
            CREATE TABLE refs (
                reference_id TEXT PRIMARY KEY,
                segment_id TEXT NOT NULL,
                source_path TEXT NOT NULL,
                target_path TEXT NOT NULL,
                reference_type TEXT NOT NULL,
                resolution_status TEXT NOT NULL
            );
            """
        )
        metadata = {
            "schema_version": SCHEMA_VERSION,
            "extraction_version": EXTRACTION_VERSION,
            "inventoried_sources": str(inventoried_sources),
            "processed_sources": str(processed_sources),
            "absence_is_not_proof_of_absence": "true",
            "offset_unit": OFFSET_UNIT,
            "interval_convention": INTERVAL_CONVENTION,
        }
        connection.executemany("INSERT INTO metadata VALUES (?, ?)", sorted(metadata.items()))
        for segment in segments:
            heading = " > ".join(segment["heading_path"])
            markers = ",".join(segment["context_markers"])
            connection.execute(
                "INSERT INTO segments VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    segment["segment_id"],
                    segment["source_path"],
                    segment["source_sha256"],
                    segment["extraction_id"],
                    json.dumps(segment["location"], ensure_ascii=False, separators=(",", ":")),
                    heading,
                    markers,
                    segment["text"],
                ),
            )
            connection.execute(
                "INSERT INTO segment_fts VALUES (?, ?, ?)",
                (segment["segment_id"], segment["text"], heading),
            )
        connection.executemany(
            "INSERT INTO refs VALUES (?, ?, ?, ?, ?, ?)",
            [
                (
                    ref["reference_id"],
                    ref["segment_id"],
                    ref["source_path"],
                    ref["target_path"],
                    ref["reference_type"],
                    ref["resolution_status"],
                )
                for ref in references
            ],
        )
        connection.commit()
    finally:
        connection.close()
    os.replace(temporary, path)


def fts_expression(query: str) -> str:
    tokens = re.findall(r"[^\W_]+", query, flags=re.UNICODE)
    return " AND ".join('"' + token.replace('"', '""') + '"' for token in tokens)


def search_index(index_path: Path, query: str, limit: int = 10, include_related: bool = True) -> dict[str, Any]:
    expression = fts_expression(query)
    connection = sqlite3.connect(index_path)
    connection.row_factory = sqlite3.Row
    try:
        metadata = dict(connection.execute("SELECT key, value FROM metadata"))
        rows: list[sqlite3.Row] = []
        if expression:
            rows = list(
                connection.execute(
                    """
                    SELECT s.*, bm25(segment_fts) AS score
                    FROM segment_fts JOIN segments s USING(segment_id)
                    WHERE segment_fts MATCH ?
                    ORDER BY score, s.segment_id
                    LIMIT ?
                    """,
                    (expression, limit),
                )
            )
        results = [
            {
                "segment_id": row["segment_id"],
                "source_path": row["source_path"],
                "source_sha256": row["source_sha256"],
                "extraction_id": row["extraction_id"],
                "location": json.loads(row["location_json"]),
                "heading_path": row["heading_path"].split(" > ") if row["heading_path"] else [],
                "context_markers": row["context_markers"].split(",") if row["context_markers"] else [],
                "text": row["text"],
                "score": row["score"],
            }
            for row in rows
        ]
        related_results: list[dict[str, Any]] = []
        if include_related and results:
            placeholders = ",".join("?" for _ in results)
            matched_ids = [result["segment_id"] for result in results]
            targets = [
                row[0]
                for row in connection.execute(
                    f"SELECT DISTINCT target_path FROM refs WHERE resolution_status='RESOLVED' AND segment_id IN ({placeholders}) ORDER BY target_path",
                    matched_ids,
                )
            ]
            for target in targets:
                for row in connection.execute(
                    "SELECT * FROM segments WHERE source_path=? ORDER BY segment_id LIMIT 3", (target,)
                ):
                    related_results.append(
                        {
                            "segment_id": row["segment_id"],
                            "source_path": row["source_path"],
                            "source_sha256": row["source_sha256"],
                            "extraction_id": row["extraction_id"],
                            "location": json.loads(row["location_json"]),
                            "heading_path": row["heading_path"].split(" > ") if row["heading_path"] else [],
                            "context_markers": row["context_markers"].split(",") if row["context_markers"] else [],
                            "text": row["text"],
                            "retrieval_reason": "EXPLICIT_REFERENCE_EXPANSION",
                        }
                    )
        retrieved_sources = sorted({item["source_path"] for item in results + related_results})
        return {
            "query": query,
            "results": results,
            "related_results": related_results,
            "coverage": {
                "inventoried_sources": int(metadata["inventoried_sources"]),
                "processed_sources": int(metadata["processed_sources"]),
                "retrieved_sources": len(retrieved_sources),
                "retrieved_source_paths": retrieved_sources,
                "retrieved_segments": len(results) + len(related_results),
                "absence_is_not_proof_of_absence": metadata["absence_is_not_proof_of_absence"] == "true",
                "sufficiency_context": "NOT_ASSESSED_BY_RETRIEVAL",
            },
        }
    finally:
        connection.close()


def safe_extracted_path(output: Path, source_path: str) -> Path:
    pure = PurePosixPath(source_path)
    if pure.is_absolute() or ".." in pure.parts:
        raise ValueError(f"Unsafe source path in manifest: {source_path}")
    return output / "extracted" / (source_path + ".txt")


def run_pipeline(manifest_path: Path, source_root: Path, output: Path) -> dict[str, Any]:
    source_root = source_root.resolve()
    output = output.resolve()
    if output == source_root or source_root in output.parents:
        raise ValueError("Output must be outside the source corpus")
    with manifest_path.open(encoding="utf-8") as handle:
        source_manifest = json.load(handle)
    records = sorted(source_manifest["files"], key=lambda item: item["relative_path"])
    output.mkdir(parents=True, exist_ok=True)
    extractions: list[dict[str, Any]] = []
    for record in records:
        path = source_root / record["relative_path"]
        extracted = extract_source(path, record)
        extracted_path = safe_extracted_path(output, record["relative_path"])
        write_text_atomic(extracted_path, extracted["rendered_text"])
        extracted["extracted_content_path"] = extracted_path.relative_to(output).as_posix()
        extracted["extracted_content_sha256"] = sha256_text(extracted["rendered_text"])
        extracted["unit_count"] = len(extracted["units"])
        extractions.append(extracted)

    segments = build_segments(extractions)
    partition_validation = validate_all_partitions(extractions, segments)
    if partition_validation["status"] != "PASS":
        raise ValueError(
            "Segmentation partition validation failed: "
            + json.dumps(partition_validation["summary"], ensure_ascii=False, sort_keys=True)
        )
    segment_counts = Counter(segment["source_path"] for segment in segments)
    for extracted in extractions:
        extracted["segment_count"] = segment_counts[extracted["source_path"]]
        extracted.pop("rendered_text", None)

    source_paths = {record["relative_path"] for record in records}
    references = build_references(segments, source_paths)
    status_counts = Counter(item["status"] for item in extractions)
    limitations = [
        {
            "source_id": item["source_id"],
            "source_path": item["source_path"],
            "extraction_id": item["extraction_id"],
            "status": item["status"],
            "limitations": item["limitations"],
        }
        for item in extractions
        if item["limitations"]
    ]
    extraction_manifest = {
        "schema_version": SCHEMA_VERSION,
        "unit": "U02",
        "source_manifest": str(manifest_path.resolve()),
        "source_manifest_sha256": sha256_file(manifest_path),
        "source_root": str(source_root),
        "extraction_version": EXTRACTION_VERSION,
        "extractor_registry": EXTRACTORS,
        "segmentation": {
            "max_segment_chars": MAX_SEGMENT_CHARS,
            "strategy": "Integral character partition; Markdown heading sections outside fenced code; otherwise paragraph/block boundaries; hard split only above maximum.",
            "offset_unit": OFFSET_UNIT,
            "interval_convention": INTERVAL_CONVENTION,
            "partition_validation": partition_validation["status"],
        },
        "retrieval": {
            "type": "SQLite FTS5 plus explicit reference expansion",
            "absence_is_not_proof_of_absence": True,
            "sufficiency_context": "NOT_ASSESSED_BY_RETRIEVAL",
        },
        "summary": {
            "inventoried_sources": len(records),
            "processed_sources": len(extractions),
            "complete_sources": status_counts["COMPLETE"],
            "partial_sources": status_counts["PARTIAL"],
            "failed_sources": status_counts["FAILED"],
            "segment_count": len(segments),
            "reference_count": len(references),
            "sources_with_limitations": len(limitations),
            "formats": dict(sorted(Counter(item["format"] for item in extractions).items())),
        },
        "extractions": extractions,
    }
    json_dump(output / "U02-extraction-manifest.json", extraction_manifest)
    json_dump(output / "U02-segmentation-validation.json", partition_validation)
    json_dump(
        output / "U02-limitations.json",
        {"schema_version": SCHEMA_VERSION, "unit": "U02", "records": limitations},
    )
    write_jsonl(output / "U02-segments.jsonl", segments)
    write_jsonl(output / "U02-references.jsonl", references)
    build_sqlite_index(
        output / "U02-retrieval-index.sqlite",
        segments,
        references,
        len(records),
        len(extractions),
    )
    with (output / "U02-format-summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["format", "source_count", "extractor_id"])
        for format_name, count in sorted(Counter(item["format"] for item in extractions).items()):
            writer.writerow([format_name, count, EXTRACTORS.get(format_name, "UNSUPPORTED")])
    return extraction_manifest


def command_run(args: argparse.Namespace) -> int:
    manifest = run_pipeline(Path(args.manifest), Path(args.source), Path(args.output))
    summary = manifest["summary"]
    print("U02 EXTRACTION COMPLETE")
    for key, value in summary.items():
        print(f"{key}={json.dumps(value, ensure_ascii=False, sort_keys=True) if isinstance(value, dict) else value}")
    return 0 if summary["failed_sources"] == 0 else 1


def command_search(args: argparse.Namespace) -> int:
    result = search_index(Path(args.index), args.query, args.limit, not args.no_related)
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        write_text_atomic(Path(args.output), rendered + "\n")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("--manifest", required=True)
    run.add_argument("--source", required=True)
    run.add_argument("--output", required=True)
    run.set_defaults(func=command_run)
    search = commands.add_parser("search")
    search.add_argument("--index", required=True)
    search.add_argument("--query", required=True)
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--no-related", action="store_true")
    search.add_argument("--output")
    search.set_defaults(func=command_search)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError, sqlite3.Error) as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
