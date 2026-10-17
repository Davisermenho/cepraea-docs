#!/usr/bin/env python3
"""Build and validate U03 claims from U02 extracted content using stdlib only."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.1.0"
EPISTEMIC_TYPES = {
    "DECISÃO_HUMANA",
    "REGRA_DOCUMENTADA",
    "EVIDÊNCIA_OBSERVADA",
    "PROPOSTA",
    "INFERÊNCIA",
    "HIPÓTESE",
    "NÃO_DOCUMENTADO",
}
RELATION_TYPES = {
    "IGUALDADE",
    "COMPLEMENTARIDADE",
    "CONTRADIÇÃO",
    "AUSÊNCIA_DE_EVIDÊNCIA",
    "RELAÇÃO_NÃO_DETERMINADA",
}
SUFFICIENCY_VALUES = {"SUFICIENTE_NO_ESCOPO", "PARCIAL", "INSUFICIENTE"}
RECOVERY_MAX_ATTEMPTS = 1


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = "".join(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n" for value in values)
    path.write_text(rendered, encoding="utf-8", newline="\n")


def normalize_evidence(value: str) -> str:
    """Only normalize Unicode, newline representation, and whitespace."""
    value = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n"))
    return re.sub(r"\s+", " ", value).strip()


def evidence_match(excerpt: str, container: str) -> str | None:
    if excerpt in container:
        return "EXACT"
    if normalize_evidence(excerpt) in normalize_evidence(container):
        return "NORMALIZED"
    return None


def diagnostic(
    record_id: str,
    stage: str,
    code: str,
    field: str,
    expected: Any,
    observed: Any,
    recoverable: bool,
) -> dict[str, Any]:
    return {
        "record_id": record_id,
        "stage": stage,
        "code": code,
        "field": field,
        "expected": expected,
        "observed": observed,
        "recoverable": recoverable,
    }


class U03Context:
    def __init__(self, manifest_path: Path, segments_path: Path, source_root: Path):
        self.manifest_path = manifest_path
        self.output_root = manifest_path.parent
        self.source_root = source_root
        manifest = load_json(manifest_path)
        self.manifest = manifest
        self.extractions = {item["source_path"]: item for item in manifest["extractions"]}
        self.segments = load_jsonl(segments_path)
        self.segments_by_id = {item["segment_id"]: item for item in self.segments}
        self.segments_by_source: dict[str, list[dict[str, Any]]] = {}
        for segment in self.segments:
            self.segments_by_source.setdefault(segment["source_path"], []).append(segment)
        self._texts: dict[str, str] = {}

    def extracted_text(self, source_path: str) -> str:
        if source_path not in self._texts:
            extraction = self.extractions[source_path]
            path = self.output_root / extraction["extracted_content_path"]
            self._texts[source_path] = path.read_text(encoding="utf-8")
        return self._texts[source_path]

    def current_source_hash(self, source_path: str) -> str | None:
        path = self.source_root / source_path
        return sha256_file(path) if path.is_file() else None


def locate_excerpt(text: str, excerpt: str) -> tuple[int, int, str]:
    start = text.find(excerpt)
    match = "EXACT"
    if start < 0:
        raise ValueError("EXCERPT_NOT_FOUND_EXACT")
    if text.find(excerpt, start + 1) >= 0:
        raise ValueError("EXCERPT_NOT_UNIQUE")
    end = start + len(excerpt)
    line_start = text.count("\n", 0, start) + 1
    line_end = text.count("\n", 0, max(start, end - 1)) + 1
    return line_start, line_end, match


def build_claim(
    blueprint: dict[str, Any],
    context: U03Context,
    locator_number: int,
    relation_ids: list[str],
) -> dict[str, Any]:
    source_path = blueprint["source_path"]
    extraction = context.extractions.get(source_path)
    if extraction is None:
        raise ValueError(f"SOURCE_NOT_IN_U02:{source_path}")
    excerpt = blueprint["literal_excerpt"]
    text = context.extracted_text(source_path)
    line_start, line_end, match = locate_excerpt(text, excerpt)
    matching_segments = [
        segment
        for segment in context.segments_by_source.get(source_path, [])
        if evidence_match(excerpt, segment["text"])
    ]
    segment_id = matching_segments[0]["segment_id"] if len(matching_segments) == 1 else None
    locator_id = f"LOC-U03-{locator_number:04d}"
    limitations = list(blueprint.get("limitations", []))
    if segment_id is None:
        limitations.append(
            "U02_SEGMENT_NOT_AVAILABLE: trecho validado diretamente no conteúdo extraído e registrado por linha."
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "claim_id": blueprint["claim_id"],
        "topic": blueprint["topic"],
        "source": {
            "path": source_path,
            "sha256": extraction["source_sha256"],
            "extraction_id": extraction["extraction_id"],
            "locator_id": locator_id,
            "segment_id": segment_id,
            "location": {"type": "lines", "start": line_start, "end": line_end},
            "literal_excerpt": excerpt,
            "evidence_match": match,
        },
        "proposed_statement": blueprint["proposed_statement"],
        "epistemic_type": blueprint["epistemic_type"],
        "authority_reference": blueprint.get("authority_reference"),
        "verification_status": "PENDENTE",
        "verification_results": [],
        "relations": sorted(relation_ids),
        "approval_reference": blueprint.get("approval_reference"),
        "context": {
            "used_locator_ids": [locator_id],
            "used_segment_ids": [segment_id] if segment_id else [],
            "conditions": blueprint.get("conditions", []),
            "exceptions": blueprint.get("exceptions", []),
            "dependencies": blueprint.get("dependencies", []),
            "limitations": limitations,
            "sufficiency": blueprint["sufficiency"],
        },
    }


def validate_structure(record: Any) -> list[dict[str, Any]]:
    record_id = record.get("claim_id", "UNKNOWN") if isinstance(record, dict) else "UNKNOWN"
    errors: list[dict[str, Any]] = []
    if not isinstance(record, dict):
        return [diagnostic(record_id, "SCHEMA", "INVALID_TYPE", "$", "object", type(record).__name__, False)]
    required = {
        "schema_version",
        "claim_id",
        "topic",
        "source",
        "proposed_statement",
        "epistemic_type",
        "authority_reference",
        "verification_status",
        "verification_results",
        "relations",
        "approval_reference",
        "context",
    }
    for field in sorted(required - set(record)):
        errors.append(diagnostic(record_id, "SCHEMA", "MISSING_REQUIRED_FIELD", field, "present", "missing", True))
    if errors:
        return errors
    if record["schema_version"] != SCHEMA_VERSION:
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_SCHEMA_VERSION", "schema_version", SCHEMA_VERSION, record["schema_version"], False))
    if not re.fullmatch(r"CLM-U03-[0-9]{4}", str(record["claim_id"])):
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_ID", "claim_id", "CLM-U03-NNNN", record["claim_id"], False))
    if record["epistemic_type"] not in EPISTEMIC_TYPES:
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_ENUM", "epistemic_type", sorted(EPISTEMIC_TYPES), record["epistemic_type"], True))
    if record["verification_status"] not in {"PENDENTE", "ACEITO", "REJEITADO"}:
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_ENUM", "verification_status", ["PENDENTE", "ACEITO", "REJEITADO"], record["verification_status"], True))
    source = record.get("source")
    source_required = {"path", "sha256", "extraction_id", "locator_id", "segment_id", "location", "literal_excerpt", "evidence_match"}
    if not isinstance(source, dict):
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_TYPE", "source", "object", type(source).__name__, False))
    else:
        for field in sorted(source_required - set(source)):
            errors.append(diagnostic(record_id, "SCHEMA", "MISSING_REQUIRED_FIELD", f"source.{field}", "present", "missing", True))
        sha = source.get("sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", str(sha)):
            errors.append(diagnostic(record_id, "SCHEMA", "INVALID_HASH", "source.sha256", "64 lowercase hex", sha, False))
        location = source.get("location")
        if not isinstance(location, dict) or set(location) != {"type", "start", "end"}:
            errors.append(diagnostic(record_id, "SCHEMA", "INVALID_LOCATION", "source.location", "type/start/end", location, True))
        elif location["type"] != "lines" or not isinstance(location["start"], int) or not isinstance(location["end"], int) or location["start"] < 1 or location["end"] < location["start"]:
            errors.append(diagnostic(record_id, "SCHEMA", "INVALID_LOCATION", "source.location", "valid 1-based line range", location, True))
    context = record.get("context")
    context_required = {"used_locator_ids", "used_segment_ids", "conditions", "exceptions", "dependencies", "limitations", "sufficiency"}
    if not isinstance(context, dict):
        errors.append(diagnostic(record_id, "SCHEMA", "INVALID_TYPE", "context", "object", type(context).__name__, False))
    else:
        for field in sorted(context_required - set(context)):
            errors.append(diagnostic(record_id, "SCHEMA", "MISSING_REQUIRED_FIELD", f"context.{field}", "present", "missing", True))
        if context.get("sufficiency") not in SUFFICIENCY_VALUES:
            errors.append(diagnostic(record_id, "SCHEMA", "INVALID_ENUM", "context.sufficiency", sorted(SUFFICIENCY_VALUES), context.get("sufficiency"), True))
    return errors


def validate_claim(record: dict[str, Any], context: U03Context, known_relations: set[str] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    validated = copy.deepcopy(record)
    record_id = record.get("claim_id", "UNKNOWN") if isinstance(record, dict) else "UNKNOWN"
    errors = validate_structure(record)
    results: list[dict[str, Any]] = [{"stage": "SCHEMA", "status": "PASS" if not errors else "FAIL"}]
    if errors:
        validated["verification_status"] = "REJEITADO"
        validated["verification_results"] = results
        return validated, errors

    source = record["source"]
    extraction = context.extractions.get(source["path"])
    reference_errors: list[dict[str, Any]] = []
    if extraction is None:
        reference_errors.append(diagnostic(record_id, "REFERENCES", "SOURCE_REFERENCE_NOT_FOUND", "source.path", "path in U02 manifest", source["path"], False))
    else:
        if source["sha256"] != extraction["source_sha256"]:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "SOURCE_HASH_MISMATCH", "source.sha256", extraction["source_sha256"], source["sha256"], False))
        current_hash = context.current_source_hash(source["path"])
        if current_hash != source["sha256"]:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "CURRENT_SOURCE_HASH_MISMATCH", "source.sha256", source["sha256"], current_hash, False))
        if source["extraction_id"] != extraction["extraction_id"]:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "EXTRACTION_REFERENCE_NOT_FOUND", "source.extraction_id", extraction["extraction_id"], source["extraction_id"], False))
    if source["segment_id"] is not None:
        segment = context.segments_by_id.get(source["segment_id"])
        if segment is None:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "SEGMENT_REFERENCE_NOT_FOUND", "source.segment_id", "existing U02 segment", source["segment_id"], False))
        elif segment["source_path"] != source["path"] or segment["extraction_id"] != source["extraction_id"]:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "SEGMENT_PROVENANCE_MISMATCH", "source.segment_id", f"{source['path']} / {source['extraction_id']}", f"{segment['source_path']} / {segment['extraction_id']}", False))
    if known_relations is not None:
        missing_relations = sorted(set(record["relations"]) - known_relations)
        if missing_relations:
            reference_errors.append(diagnostic(record_id, "REFERENCES", "RELATION_REFERENCE_NOT_FOUND", "relations", "known relation IDs", missing_relations, False))
    errors.extend(reference_errors)
    results.append({"stage": "REFERENCES", "status": "PASS" if not reference_errors else "FAIL"})

    evidence_errors: list[dict[str, Any]] = []
    if extraction is not None:
        text = context.extracted_text(source["path"])
        lines = text.splitlines(keepends=True)
        start = source["location"]["start"]
        end = source["location"]["end"]
        selected = "".join(lines[start - 1 : end]) if end <= len(lines) else ""
        match = evidence_match(source["literal_excerpt"], selected)
        if match is None:
            evidence_errors.append(diagnostic(record_id, "EVIDENCE", "EVIDENCE_MISMATCH", "source.literal_excerpt", "excerpt within declared line range", source["literal_excerpt"], True))
        elif match != source["evidence_match"]:
            evidence_errors.append(diagnostic(record_id, "EVIDENCE", "EVIDENCE_MATCH_MODE_MISMATCH", "source.evidence_match", match, source["evidence_match"], True))
        if source["segment_id"] is not None:
            segment = context.segments_by_id.get(source["segment_id"])
            if segment is not None and evidence_match(source["literal_excerpt"], segment["text"]) is None:
                evidence_errors.append(diagnostic(record_id, "EVIDENCE", "SEGMENT_EVIDENCE_MISMATCH", "source.segment_id", "segment contains excerpt", source["segment_id"], True))
    errors.extend(evidence_errors)
    results.append({"stage": "EVIDENCE", "status": "PASS" if not evidence_errors else "FAIL", "match": source["evidence_match"] if not evidence_errors else None})

    authority_errors: list[dict[str, Any]] = []
    if record["epistemic_type"] == "DECISÃO_HUMANA":
        reference = record.get("authority_reference") or {}
        if reference.get("verification") != "VERIFICADA_NO_CORPUS" or record.get("approval_reference") is None:
            authority_errors.append(diagnostic(record_id, "AUTHORITY", "UNVERIFIED_HUMAN_DECISION", "authority_reference", "verified authority plus approval reference", reference, False))
    errors.extend(authority_errors)
    results.append({"stage": "AUTHORITY", "status": "PASS" if not authority_errors else "FAIL", "automatic_approval": False})
    validated["verification_status"] = "ACEITO" if not errors else "REJEITADO"
    validated["verification_results"] = results
    return validated, errors


def process_records(
    raw_lines: list[str],
    context: U03Context,
    known_relations: set[str],
    corrections: dict[int, str] | None = None,
    max_attempts: int = RECOVERY_MAX_ATTEMPTS,
) -> dict[str, Any]:
    corrections = corrections or {}
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    attempts: list[dict[str, Any]] = []
    originals: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_lines):
        originals.append({"record_index": index, "sha256": sha256_bytes(raw.encode("utf-8")), "raw": raw})
        candidate_raw = raw
        attempt = 0
        while True:
            try:
                candidate = json.loads(candidate_raw)
                validated, record_errors = validate_claim(candidate, context, known_relations)
            except json.JSONDecodeError as error:
                candidate = {"claim_id": f"INVALID-INDEX-{index}"}
                validated = {"raw_record_index": index, "verification_status": "REJEITADO"}
                record_errors = [diagnostic(candidate["claim_id"], "SYNTAX", "INVALID_JSON", "$", "valid JSON", f"{error.msg} at line {error.lineno} column {error.colno}", True)]
            attempts.append({
                "record_index": index,
                "attempt": attempt,
                "input_sha256": sha256_bytes(candidate_raw.encode("utf-8")),
                "status": "PASS" if not record_errors else "FAIL",
                "error_codes": [item["code"] for item in record_errors],
            })
            diagnostics.extend(record_errors)
            if not record_errors:
                accepted.append(validated)
                break
            if attempt >= max_attempts or index not in corrections:
                rejected.append(validated)
                break
            attempt += 1
            candidate_raw = corrections[index]
    return {
        "accepted": accepted,
        "rejected": rejected,
        "diagnostics": diagnostics,
        "attempts": attempts,
        "originals": originals,
        "configuration": {"max_automatic_attempts": max_attempts, "finite_stop": True},
    }


def validate_relations(config: dict[str, Any], claim_ids: set[str]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    relation_ids: set[str] = set()
    for relation in config["relations"]:
        relation_id = relation.get("relation_id", "UNKNOWN")
        if relation_id in relation_ids:
            errors.append(diagnostic(relation_id, "RELATIONS", "DUPLICATE_RELATION_ID", "relation_id", "unique", relation_id, False))
        relation_ids.add(relation_id)
        if relation.get("type") not in RELATION_TYPES:
            errors.append(diagnostic(relation_id, "RELATIONS", "INVALID_RELATION_TYPE", "type", sorted(RELATION_TYPES), relation.get("type"), False))
        missing = sorted(set(relation.get("claim_ids", [])) - claim_ids)
        if missing:
            errors.append(diagnostic(relation_id, "RELATIONS", "CLAIM_REFERENCE_NOT_FOUND", "claim_ids", "accepted claim IDs", missing, False))
    for group in config["divergence_groups"]:
        missing_claims = sorted(set(group.get("claim_ids", [])) - claim_ids)
        missing_relations = sorted(set(group.get("relation_ids", [])) - relation_ids)
        if missing_claims:
            errors.append(diagnostic(group["divergence_id"], "DIVERGENCES", "CLAIM_REFERENCE_NOT_FOUND", "claim_ids", "accepted claim IDs", missing_claims, False))
        if missing_relations:
            errors.append(diagnostic(group["divergence_id"], "DIVERGENCES", "RELATION_REFERENCE_NOT_FOUND", "relation_ids", "known relation IDs", missing_relations, False))
        if group.get("automatic_resolution") is not False:
            errors.append(diagnostic(group["divergence_id"], "DIVERGENCES", "AUTOMATIC_RESOLUTION_FORBIDDEN", "automatic_resolution", False, group.get("automatic_resolution"), False))
    return errors


def build_consolidation_map(claim_ids: set[str]) -> dict[str, Any]:
    sections = [
        {
            "section": "governança_e_autoridade",
            "eligible_claim_ids": ["CLM-U03-0001", "CLM-U03-0002", "CLM-U03-0003", "CLM-U03-0022", "CLM-U03-0023"],
            "pending_claim_ids": ["CLM-U03-0004", "CLM-U03-0005", "CLM-U03-0006", "CLM-U03-0007"],
            "instruction": "Manter regras como documentadas; não declarar vigência da Constituição ou do índice sem decisão sobre DVG-U03-001."
        },
        {
            "section": "contexto_e_modelo_de_dominio",
            "eligible_claim_ids": ["CLM-U03-0025", "CLM-U03-0026", "CLM-U03-0027"],
            "pending_claim_ids": [],
            "instruction": "Apresentar como conteúdo documentado/proposto e preservar limites de observação e temporalidade."
        },
        {
            "section": "fluxo_d5",
            "eligible_claim_ids": ["CLM-U03-0014", "CLM-U03-0017"],
            "pending_claim_ids": ["CLM-U03-0015", "CLM-U03-0016"],
            "instruction": "Preservar condição normal e exceção pós-confirmação; tratar B-01/B-02 como transcrições até autenticação."
        },
        {
            "section": "arquitetura_tecnica",
            "eligible_claim_ids": [],
            "pending_claim_ids": ["CLM-U03-0018", "CLM-U03-0019", "CLM-U03-0020", "CLM-U03-0021"],
            "instruction": "Exibir alternativas e decisões abertas; não selecionar stack automaticamente."
        },
        {
            "section": "estado_de_implementacao",
            "eligible_claim_ids": ["CLM-U03-0008", "CLM-U03-0012", "CLM-U03-0013"],
            "pending_claim_ids": ["CLM-U03-0009", "CLM-U03-0010", "CLM-U03-0011"],
            "instruction": "Não consolidar estado operacional até resolver DVG-U03-002 com evidência observável."
        },
        {
            "section": "fontes_de_requisitos",
            "eligible_claim_ids": [],
            "pending_claim_ids": ["CLM-U03-0024"],
            "instruction": "Excluir placeholders do conjunto de requisitos substantivos; usar apenas como template."
        }
    ]
    for section in sections:
        section["eligible_claim_ids"] = [item for item in section["eligible_claim_ids"] if item in claim_ids]
        section["pending_claim_ids"] = [item for item in section["pending_claim_ids"] if item in claim_ids]
    return {
        "schema_version": "1.0.0",
        "unit": "U03",
        "status": "CANDIDATE_MAP_NOT_PUBLICATION",
        "publication_authorized": False,
        "sections": sections,
    }


def markdown_claims(claims: list[dict[str, Any]]) -> str:
    lines = [
        "# ENT-03 — Registro de evidências e afirmações",
        "",
        "Este índice é derivado dos registros JSONL validados. Classificação epistemológica não equivale a vigência.",
        "",
        "| ID | Tipo | Tema | Fonte | Localização | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for claim in claims:
        source = claim["source"]
        loc = source["location"]
        lines.append(f"| {claim['claim_id']} | {claim['epistemic_type']} | {claim['topic']} | `{source['path']}` | linhas {loc['start']}–{loc['end']}; {source['locator_id']}; {source['segment_id'] or 'sem segment_id U02'} | {claim['verification_status']} |")
    lines.extend(["", f"Total aceito: **{len(claims)}**.", ""])
    return "\n".join(lines)


def markdown_divergences(config: dict[str, Any]) -> str:
    lines = [
        "# ENT-04 — Divergências e decisões",
        "",
        "Nenhum conflito abaixo foi resolvido automaticamente.",
        "",
        "| ID | Questão | Prioridade | Estado | Pergunta encaminhada |",
        "| --- | --- | --- | --- | --- |",
    ]
    for group in config["divergence_groups"]:
        lines.append(f"| {group['divergence_id']} | {group['title']} | {group['priority']} | {group['status']} | {group['decision_question']} |")
    lines.extend(["", "## Relações", ""])
    for relation in config["relations"]:
        lines.append(f"- `{relation['relation_id']}` — **{relation['type']}** — {', '.join(relation['claim_ids'])}: {relation['rationale']}")
    lines.append("")
    return "\n".join(lines)


def markdown_map(consolidation_map: dict[str, Any]) -> str:
    lines = [
        "# ENT-05 — Mapa de consolidação",
        "",
        "Mapa para futura U04. Não é documento publicado nem autorização para publicação.",
        "",
        "| Seção candidata | Afirmações elegíveis | Pendentes | Instrução |",
        "| --- | --- | --- | --- |",
    ]
    for section in consolidation_map["sections"]:
        lines.append(f"| {section['section']} | {', '.join(section['eligible_claim_ids']) or '—'} | {', '.join(section['pending_claim_ids']) or '—'} | {section['instruction']} |")
    lines.append("")
    return "\n".join(lines)


def run_pipeline(
    manifest_path: Path,
    segments_path: Path,
    source_root: Path,
    blueprint_path: Path,
    relations_path: Path,
    output_root: Path,
) -> dict[str, Any]:
    generated = output_root / "generated"
    evidence = output_root / "evidence"
    generated.mkdir(parents=True, exist_ok=True)
    evidence.mkdir(parents=True, exist_ok=True)
    context = U03Context(manifest_path, segments_path, source_root)
    blueprint = load_json(blueprint_path)
    relation_config = load_json(relations_path)
    relations_for_claim: dict[str, list[str]] = {}
    for relation in relation_config["relations"]:
        for claim_id in relation["claim_ids"]:
            relations_for_claim.setdefault(claim_id, []).append(relation["relation_id"])
    originals = [
        build_claim(item, context, index, relations_for_claim.get(item["claim_id"], []))
        for index, item in enumerate(blueprint["claims"], start=1)
    ]
    original_path = evidence / "U03-agent-output-original.jsonl"
    write_jsonl(original_path, originals)
    raw_lines = original_path.read_text(encoding="utf-8").splitlines()
    known_relations = {item["relation_id"] for item in relation_config["relations"]}
    processed = process_records(raw_lines, context, known_relations, max_attempts=RECOVERY_MAX_ATTEMPTS)
    accepted_ids = {item["claim_id"] for item in processed["accepted"]}
    relation_errors = validate_relations(relation_config, accepted_ids)
    processed["diagnostics"].extend(relation_errors)
    if relation_errors:
        raise RuntimeError("Relation validation failed: " + ", ".join(item["code"] for item in relation_errors))
    ids = [item["claim_id"] for item in processed["accepted"]]
    duplicates = sorted(value for value, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise RuntimeError("Duplicate claim IDs: " + ", ".join(duplicates))

    write_jsonl(generated / "U03-claims-accepted.jsonl", processed["accepted"])
    write_jsonl(generated / "U03-claims-rejected.jsonl", processed["rejected"])
    write_json(generated / "U03-relations.json", {"schema_version": "1.0.0", "relations": relation_config["relations"]})
    write_json(generated / "U03-divergences-pending.json", {"schema_version": "1.0.0", "divergence_groups": relation_config["divergence_groups"]})
    write_json(evidence / "U03-validation-diagnostics.json", {
        "schema_version": "1.0.0",
        "unit": "U03",
        "configuration": processed["configuration"],
        "original_output_sha256": sha256_file(original_path),
        "record_attempts": processed["attempts"],
        "diagnostics": processed["diagnostics"],
        "accepted": len(processed["accepted"]),
        "rejected": len(processed["rejected"]),
    })
    locator_only = [item for item in processed["accepted"] if item["source"]["segment_id"] is None]
    sources_selected = sorted({item["source"]["path"] for item in processed["accepted"]})
    coverage = {
        "schema_version": "1.0.0",
        "unit": "U03",
        "corpus_document_coverage": {
            "u02_sources_processed": len(context.extractions),
            "u02_status_counts": dict(sorted(Counter(item["status"] for item in context.extractions.values()).items())),
        },
        "retrieval_coverage": {
            "sources_selected": len(sources_selected),
            "source_paths": sources_selected,
            "claims": len(processed["accepted"]),
            "u02_segments_used": len({sid for item in processed["accepted"] for sid in item["context"]["used_segment_ids"]}),
            "line_locators_used": len(processed["accepted"]),
            "locators_without_u02_segment": len(locator_only),
            "locator_only_claim_ids": [item["claim_id"] for item in locator_only],
        },
        "contextual_sufficiency": dict(sorted(Counter(item["context"]["sufficiency"] for item in processed["accepted"]).items())),
        "limitations": [
            "A seleção é dirigida aos documentos candidatos e divergências materiais identificadas; não afirma exaustividade semântica do corpus.",
            "Ausência em busca ou seleção não demonstra inexistência no corpus.",
            "B-01 e B-02 foram encontradas como transcrições no PRD; as fontes primárias referenciadas não foram autenticadas no corpus processado.",
            "Estado de runtime, Supabase, deploy e código externo ao corpus não foi observado nesta U03.",
        ] + ([
            "Há trechos validados diretamente no conteúdo extraído que não possuem segment_id U02; os respectivos locators estão explícitos.",
        ] if locator_only else []),
    }
    write_json(generated / "U03-context-coverage.json", coverage)
    consolidation_map = build_consolidation_map(accepted_ids)
    write_json(generated / "U03-consolidation-map.json", consolidation_map)

    write_jsonl(output_root / "ENT-03-registro-evidencias-afirmacoes.jsonl", processed["accepted"])
    (output_root / "ENT-03-registro-evidencias-afirmacoes.md").write_text(markdown_claims(processed["accepted"]), encoding="utf-8", newline="\n")
    write_json(output_root / "ENT-04-divergencias-decisoes.json", {"schema_version": "1.0.0", "relations": relation_config["relations"], "divergence_groups": relation_config["divergence_groups"]})
    (output_root / "ENT-04-divergencias-decisoes.md").write_text(markdown_divergences(relation_config), encoding="utf-8", newline="\n")
    write_json(output_root / "ENT-05-mapa-consolidacao.json", consolidation_map)
    (output_root / "ENT-05-mapa-consolidacao.md").write_text(markdown_map(consolidation_map), encoding="utf-8", newline="\n")

    output_hashes = {}
    for path in sorted(output_root.glob("ENT-*")):
        if path.is_file():
            output_hashes[path.name] = sha256_file(path)
    summary = {
        "schema_version": "1.0.0",
        "unit": "U03",
        "status": "PASS" if not processed["rejected"] and not processed["diagnostics"] else "FAIL",
        "claims_prepared": len(originals),
        "claims_accepted": len(processed["accepted"]),
        "claims_rejected": len(processed["rejected"]),
        "relations": len(relation_config["relations"]),
        "divergence_groups": len(relation_config["divergence_groups"]),
        "pending_human_groups": sum(1 for item in relation_config["divergence_groups"] if "HUMANA" in item["priority"] or "HUMANA" in item["status"]),
        "automatic_resolutions": sum(1 for item in relation_config["divergence_groups"] if item["automatic_resolution"]),
        "recovery_max_attempts": RECOVERY_MAX_ATTEMPTS,
        "locators_without_u02_segment": len(locator_only),
        "output_hashes": output_hashes,
    }
    write_json(evidence / "U03-run-summary.json", summary)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u02-manifest", required=True)
    parser.add_argument("--segments", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--blueprint", required=True)
    parser.add_argument("--relations", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    summary = run_pipeline(
        Path(args.u02_manifest).resolve(),
        Path(args.segments).resolve(),
        Path(args.source).resolve(),
        Path(args.blueprint).resolve(),
        Path(args.relations).resolve(),
        Path(args.output).resolve(),
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
