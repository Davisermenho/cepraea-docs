#!/usr/bin/env python3
"""Generate U04 candidate documents from verified U03 claims and authorized decisions."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0.0"
CANDIDATE_STATUS = "CANDIDATO_NAO_APROVADO"


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


def render_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def version_from_document(path: Path) -> str:
    head = path.read_text(encoding="utf-8")[:2000]
    match = re.search(r"(?im)^VERSAO:\s*(v\d+\.\d+\.\d+)\s*$", head)
    if not match:
        raise ValueError(f"VERSION_NOT_FOUND:{path}")
    return match.group(1)


def build_outputs(
    claims_path: Path,
    decisions_path: Path,
    decision_record_path: Path,
    technical_path: Path,
    source_root: Path,
) -> dict[str, str]:
    claims = load_jsonl(claims_path)
    claims_by_id = {item["claim_id"]: item for item in claims}
    if len(claims_by_id) != len(claims):
        raise ValueError("DUPLICATE_U03_CLAIM_IDS")
    decisions = load_json(decisions_path)
    if sha256_file(decision_record_path) != decisions["record_sha256"]:
        raise ValueError("DECISION_RECORD_HASH_MISMATCH")
    if decisions.get("publication_authorized") is not False or decisions["scope_limits"].get("a3_granted") is not False:
        raise ValueError("PUBLICATION_MUST_REMAIN_UNAUTHORIZED")
    decision_ids = {item["decision_id"] for item in decisions["decisions"]}
    technical = load_json(technical_path)

    constitution = source_root / "[ATIVO] Constituição_do_Projeto.md"
    current_index = source_root / "[ATIVO] 20-CURRENT-STATE-INDEX.md"
    approval_registry = {
        "schema_version": SCHEMA_VERSION,
        "registry_type": "REGISTRO_UNICO_DE_APROVACAO",
        "generated_from": "DEC-U04-001",
        "entries": [
            {
                "document_id": "CONSTITUICAO_DO_PROJETO",
                "path": constitution.name,
                "version": version_from_document(constitution),
                "sha256": sha256_file(constitution),
                "approval_status": "AGUARDANDO_APROVACAO",
                "approved_by": None,
                "effective_date": None,
                "normative_precedence_active": False,
            },
            {
                "document_id": "CURRENT_STATE_INDEX",
                "path": current_index.name,
                "version": version_from_document(current_index),
                "sha256": sha256_file(current_index),
                "approval_status": "AGUARDANDO_APROVACAO",
                "approved_by": None,
                "effective_date": None,
                "normative_precedence_active": False,
            },
        ],
    }

    statements = [
        ("STM-U04-001", "governanca", "Nenhum rótulo ou nome de arquivo confere aprovação.", ["DEC-U04-001", "CLM-U03-0002", "CLM-U03-0023"]),
        ("STM-U04-002", "governanca", "A precedência da Constituição somente nasce após aprovação formal da versão exata.", ["DEC-U04-001", "CLM-U03-0004", "CLM-U03-0006"]),
        ("STM-U04-003", "governanca", "O registro único exige identificador, versão, SHA-256, responsável e data de vigência.", ["DEC-U04-001"]),
        ("STM-U04-004", "produto", "Em D-5, cancelamento automático aplica-se somente a sessão PUBLICADO nas condições do checkpoint.", ["DEC-U04-002", "CLM-U03-0014"]),
        ("STM-U04-005", "produto", "Cancelamento é terminal e a identidade da sessão não pode ser reutilizada.", ["DEC-U04-002"]),
        ("STM-U04-006", "produto", "Depois de CONFIRMADO, perda de quórum não cancela automaticamente; decide o treinador.", ["DEC-U04-002", "CLM-U03-0017"]),
        ("STM-U04-007", "produto", "O produto é mobile-first e distribuído como PWA.", ["DEC-U04-003"]),
        ("STM-U04-008", "produto", "Treinador e atleta exigem autenticação e permissões adequadas.", ["DEC-U04-003"]),
        ("STM-U04-009", "produto", "R$ 50 mensais é referência sujeita a verificação de viabilidade.", ["DEC-U04-003"]),
        ("STM-U04-010", "produto", "Operação conectada é a referência; offline completo e push dependem de necessidade demonstrada.", ["DEC-U04-003", "CLM-U03-0020"]),
        ("STM-U04-011", "tecnico", "A arquitetura definitiva permanece sem aprovação e deve considerar simplicidade, manutenção individual e reuso.", ["DEC-U04-003", "CLM-U03-0018", "CLM-U03-0019", "CLM-U03-0021"]),
        ("STM-U04-012", "tecnico", "Estados técnicos distintos exigem evidência compatível e não são promovidos por declaração.", ["DEC-U04-004", "CLM-U03-0010", "CLM-U03-0011", "CLM-U03-0012", "CLM-U03-0013"]),
        ("STM-U04-013", "tecnico", "React/Vite/PWA está observado no commit inspecionado, sem aprovação arquitetural nem prova de execução.", ["DEC-U04-003", "OBS-U04-REPO-001"]),
        ("STM-U04-014", "tecnico", "O projeto Supabase existe e está INACTIVE; esquema, migrações e prontidão não foram verificados.", ["DEC-U04-004", "OBS-U04-SUPABASE-001"]),
    ]
    evidence_ids = {"OBS-U04-REPO-001", "OBS-U04-SUPABASE-001"}
    missing_refs = sorted({ref for _, _, _, refs in statements for ref in refs if ref not in claims_by_id and ref not in decision_ids and ref not in evidence_ids})
    if missing_refs:
        raise ValueError("UNKNOWN_TRACEABILITY_REFERENCES:" + ",".join(missing_refs))

    map_doc = {
        "schema_version": SCHEMA_VERSION,
        "unit": "U04",
        "publication_authorized": False,
        "statements": [
            {"statement_id": sid, "destination": destination, "text": text, "basis_references": refs}
            for sid, destination, text, refs in statements
        ],
        "source_inputs": {
            "u03_claims": {"path": str(claims_path), "sha256": sha256_file(claims_path)},
            "decision_registry": {"path": str(decisions_path), "sha256": sha256_file(decisions_path)},
            "decision_record": {"path": str(decision_record_path), "sha256": sha256_file(decision_record_path)},
            "technical_inspection": {"path": str(technical_path), "sha256": sha256_file(technical_path)},
        },
    }
    pending = {
        "schema_version": SCHEMA_VERSION,
        "publication_authorized": False,
        "items": [
            {"pending_id": "PEND-U04-001", "subject": "Aprovação das versões documentais", "required_authority": "RESPONSAVEL_PELO_PROJETO", "condition": "Identificar e aprovar formalmente versão e SHA-256; preencher responsável e data de vigência.", "status": "PENDENTE_DECISAO_HUMANA"},
            {"pending_id": "PEND-U04-002", "subject": "Arquitetura definitiva", "required_authority": "RESPONSAVEL_PELO_PROJETO", "condition": "Comparar custo operacional verificável e aderência; selecionar explicitamente uma arquitetura.", "status": "PENDENTE_DECISAO_HUMANA"},
            {"pending_id": "PEND-U04-003", "subject": "Viabilidade do orçamento", "required_authority": "RESPONSAVEL_PELO_PROJETO", "condition": "Obter custos atuais dos componentes e demonstrar cenário dentro ou fora da referência de R$ 50/mês.", "status": "PENDENTE_VERIFICACAO"},
            {"pending_id": "PEND-U04-004", "subject": "Implementação e infraestrutura alvo", "required_authority": "EVIDENCIA_TECNICA_E_RESPONSAVEL", "condition": "Disponibilizar alvo ativo e verificar commit, esquema, migrações, testes e comportamento no alvo sem inferência.", "status": "PENDENTE_VERIFICACAO"},
            {"pending_id": "PEND-U04-005", "subject": "Publicação oficial A3", "required_authority": "RESPONSAVEL_PELO_PROJETO", "condition": "Aprovar os hashes exatos dos candidatos após U05.", "status": "PENDENTE_DECISAO_HUMANA"},
        ],
    }

    header = f"Status: `{CANDIDATE_STATUS}`  \nUnidade: `U04`  \nPublicação oficial autorizada: `NÃO`\n"
    governance = f"""# ENT-06A — Governança e autoridade (candidato)\n\n{header}\n## Regra consolidada\n\n- Nenhum nome, conteúdo ou rótulo `[ATIVO]` aprova ou torna vigente um documento.\n- O Current State Index registra e permite consultar estados; ele não aprova documentos.\n- A Constituição somente terá precedência normativa após aprovação formal da versão exata.\n- Aprovação exige registro único com identificador, versão, SHA-256, responsável e data de vigência.\n- Não existe vigência retroativa presumida.\n\n## Estado das versões examinadas\n\n| Documento | Versão | SHA-256 | Estado | Precedência ativa |\n| --- | --- | --- | --- | --- |\n| Constituição do Projeto | {approval_registry['entries'][0]['version']} | `{approval_registry['entries'][0]['sha256']}` | `AGUARDANDO_APROVACAO` | não |\n| Current State Index | {approval_registry['entries'][1]['version']} | `{approval_registry['entries'][1]['sha256']}` | `AGUARDANDO_APROVACAO` | não |\n\n## Rastreabilidade\n\nDecisão humana: `DEC-U04-001`. Evidências U03: `CLM-U03-0002`, `CLM-U03-0004`, `CLM-U03-0006`, `CLM-U03-0023`. Afirmações: `STM-U04-001` a `STM-U04-003`.\n"""
    product = f"""# ENT-06B — Requisitos de produto e fluxo D-5 (candidato)\n\n{header}\n## Fluxo D-5 ratificado\n\n- No checkpoint D-5, o cancelamento automático aplica-se exclusivamente a sessões em `PUBLICADO`, observadas as condições do checkpoint.\n- O cancelamento é terminal; a identidade da sessão cancelada não pode ser reutilizada.\n- Depois de `CONFIRMADO`, perda de quórum não causa cancelamento automático. O treinador decide manter ou cancelar.\n- Formulações anteriores incompatíveis ficam substituídas somente nesse escopo.\n\n## Requisitos do produto\n\n- Uso prioritariamente móvel, como PWA.\n- Perfis de treinador e atleta, com autenticação e permissões adequadas.\n- Orçamento operacional de referência próximo de R$ 50/mês, ainda sujeito a verificação de viabilidade.\n- Operação conectada como referência inicial. Offline completo e notificações push não são obrigatórios sem necessidade funcional demonstrada.\n\n## Rastreabilidade\n\nDecisões humanas: `DEC-U04-002`, `DEC-U04-003`. Evidências U03: `CLM-U03-0014`, `CLM-U03-0017`, `CLM-U03-0020`. Afirmações: `STM-U04-004` a `STM-U04-010`.\n"""
    repo = technical["repository"]
    supabase = technical["supabase"]
    technical_doc = f"""# ENT-06C — Arquitetura e estado técnico (candidato)\n\n{header}\n## Critérios e decisão ainda aberta\n\nA arquitetura deve privilegiar simplicidade operacional, manutenção por uma pessoa e reuso do código existente. Nem Next.js/Vercel nem React/Vite está aprovado como arquitetura definitiva.\n\n## Comparação sustentada pela inspeção\n\n| Alternativa | Evidência atual | Reuso | Limite demonstrado |\n| --- | --- | --- | --- |\n| React/Vite/PWA | Observada no commit `{repo['commit_sha']}` | Alto, porque é a base existente | Não executada localmente nesta atividade; custo e implantação não verificados |\n| Next.js | Não observado como base do commit inspecionado | Exigiria mudança cuja necessidade não foi demonstrada | Sem evidência suficiente para selecionar ou estimar custo de migração |\n| Vercel | `vercel.json` e URL declarada existem | Compatível com a base observada | Configuração não comprova implantação nem aprovação definitiva |\n| Supabase | Projeto `{supabase['project_ref']}` existe com estado `{supabase['status']}` | Cliente e configuração local observados | Banco e migrações não verificados por timeout |\n\nA inspeção favorece o reuso de React/Vite como alternativa de menor mudança, mas isso é uma recomendação candidata, não escolha arquitetural aprovada. A decisão depende de custo atual e verificação executável.\n\n## Estado técnico demonstrável\n\n- Arquivos selecionados do repositório: `VALIDADO_ESTATICAMENTE`, limitado ao conteúdo observado no commit.\n- Execução local do produto: não demonstrada nesta atividade.\n- Projeto Supabase: existência observada; prontidão e esquema não verificados. O estado `INACTIVE` impede alegar `VERIFICADO_NO_ALVO`.\n- Nenhuma implantação, migração ou alteração de produção foi executada.\n\n## Rastreabilidade\n\nDecisões humanas: `DEC-U04-003`, `DEC-U04-004`. Evidências: `OBS-U04-REPO-001`, `OBS-U04-SUPABASE-001`; U03 `CLM-U03-0018` a `CLM-U03-0021` e `CLM-U03-0010` a `CLM-U03-0013`. Afirmações: `STM-U04-011` a `STM-U04-014`.\n"""
    map_md = "# ENT-07 — Mapa de origem e destino\n\nStatus: `CANDIDATO_NAO_APROVADO`.\n\n| Afirmação | Destino | Fundamentos |\n| --- | --- | --- |\n" + "".join(f"| {sid} | {dest} | {', '.join(refs)} |\n" for sid, dest, _, refs in statements)
    pending_md = "# ENT-08 — Pendências de revisão\n\nNenhuma pendência abaixo está aprovada ou resolvida por inferência.\n\n| Pendência | Assunto | Estado | Condição de resolução |\n| --- | --- | --- | --- |\n" + "".join(f"| {item['pending_id']} | {item['subject']} | `{item['status']}` | {item['condition']} |\n" for item in pending["items"])

    return {
        "ENT-06A-governanca-autoridade.candidato.md": governance,
        "ENT-06B-requisitos-produto-d5.candidato.md": product,
        "ENT-06C-arquitetura-estado-tecnico.candidato.md": technical_doc,
        "ENT-07-mapa-origem-destino.json": render_json(map_doc),
        "ENT-07-mapa-origem-destino.md": map_md,
        "ENT-08-pendencias-revisao.json": render_json(pending),
        "ENT-08-pendencias-revisao.md": pending_md,
        "approval-registry.json": render_json(approval_registry),
    }


def publish(outputs: dict[str, str], output_root: Path, simulate_interrupt: bool = False) -> dict[str, Any]:
    output_root.mkdir(parents=True, exist_ok=True)
    target = output_root / "generated"
    stage = Path(tempfile.mkdtemp(prefix=".u04-stage-", dir=output_root))
    try:
        for index, (name, content) in enumerate(sorted(outputs.items())):
            (stage / name).write_text(content, encoding="utf-8", newline="\n")
            if simulate_interrupt and index == 0:
                return {"status": "INTERRUPTED", "published": False, "files_written_to_stage": 1}
        hashes = {name: sha256_file(stage / name) for name in sorted(outputs)}
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "unit": "U04",
            "status": "COMPLETE",
            "candidate_status": CANDIDATE_STATUS,
            "publication_authorized": False,
            "files": hashes,
        }
        (stage / "U04-run-manifest.json").write_text(render_json(manifest), encoding="utf-8", newline="\n")
        if target.exists():
            existing = {p.name: sha256_file(p) for p in target.iterdir() if p.is_file() and p.name != "U04-run-manifest.json"}
            if existing != hashes:
                raise ValueError("NON_EQUIVALENT_EXISTING_OUTPUT")
            return {"status": "PASS", "published": True, "equivalent_existing": True, "files": hashes}
        os.replace(stage, target)
        stage = None
        return {"status": "PASS", "published": True, "equivalent_existing": False, "files": hashes}
    finally:
        if stage is not None and stage.exists():
            shutil.rmtree(stage)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--decision-registry", required=True)
    parser.add_argument("--decision-record", required=True)
    parser.add_argument("--technical-evidence", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--simulate-interrupt", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs(Path(args.claims), Path(args.decision_registry), Path(args.decision_record), Path(args.technical_evidence), Path(args.source))
    result = publish(outputs, Path(args.output), args.simulate_interrupt)
    print(render_json(result), end="")
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
