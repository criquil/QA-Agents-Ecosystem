# QA-Agents-Ecosystem

**Ecosistema de QA cross-disciplina** — Orquestador + 4 expertos + COE + Stakeholders

---

## 🎯 Visión General

Este repositorio contiene un **ecosistema completo de agentes de QA** que trabajan coordinados para cubrir todo el ciclo de vida de testing: manual, automatización, API, performance y gobernanza.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        META (Orquestador)                           │
│  ┌─────────────┐    ┌─────────────┐                                 │
│  │   Coordi    │    │     Biz     │                                 │
│  │ Test Lead   │    │ Stakeholder │                                 │
│  │ Orchestrator│    │    Gate     │                                 │
│  └──────┬──────┘    └──────┬──────┘                                 │
└─────────┼──────────────────┼────────────────────────────────────────┘
          │                  │
    ┌─────┴─────┐    ┌───────┴───────┐    ┌─────────────┐
    │           │    │               │    │             │
    ▼           ▼    ▼               ▼    ▼             ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ AUTO   │ │  API   │ │ MANUAL │ │ PERF   │ │   COE  │ │  META  │
│  TLC   │ │  TLC   │ │  TLC   │ │  TLC   │ │ (Maru) │ │ (Biz)  │
│        │ │        │ │        │ │        │ │        │ │        │
│ Scripto│ │   APU  │ │  MANU  │ │ Perfie │ │        │ │        │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

---

## 👥 El Crew (Agentes)

| Área | Friendly Name | Agente Técnico | Repo | Entry Point |
|------|---------------|----------------|------|-------------|
| **Stakeholders** | **Biz** | `biz` | `meta/` (local) | `.opencode/agents/biz.md` |
| **Orquestador** | **Coordi** | `test-lead-orchestrator` | `meta/` | `.opencode/agents/test-lead-orchestrator.md` |
| **Performance Test** | **Perfie** | `ptlc-orchestrator` | `Intelligent_Performance_Test_Orchstrator/` | `.opencode/agents/ptlc-orchestrator.md` |
| **API Test** | **APU** | `api-tlc-orchestrator-api` | `API-TLC/` | `.opencode/agents/api-tlc-orchestrator-api.agent.md` |
| **Manual Test** | **MANU** | `manual-tlc-orchestrator-manual` | `MANUAL-TLC/` | `.opencode/agents/` |
| **Automation Test** | **Scripto** | `automation-qa-orchestrator` | `AUTO-TLC/` | `.opencode/agents/automation-qa-orchestrator.md` |
| **COE / Governance** | **Maru** | `maru` | `COE/` | `.opencode/agents/maru.md` |

---

## 🔄 Flujo de Trabajo Principal (Coordi Pipeline)

**Entry point obligatorio**: `test-lead-orchestrator` (Coordi) — todo request entra por aquí.

```
Phase 0  →  Gate de Stakeholders (Biz) + detectar dominio + crear plan.yaml
Phase 1  →  Delegar al experto + pedir políticas al COE (Maru)
Phase 2  →  Recibir entrega del experto
Phase 3  →  Activar validación del COE (Maru)
Phase 4  →  Resolver veredicto (PASSED / NEEDS_REVISION / BLOCKED)
Phase 5  →  Integrar → plan consolidado + reporte ejecutivo → Aceptación de Biz
```

### Reglas de Oro
- ✅ **Stakeholders siempre** — Phase 0 (brief) y Phase 5 (aceptación) son obligatorios
- ✅ **Delegación obligatoria** — `meta/` NO ejecuta pruebas; siempre delega a ≥1 experto
- ✅ **No operar** — Coordi no prueba, Maru no implementa, Biz no testa
- ✅ **Un `plan_id` maestro** en `meta/`; cada experto genera su `plan_id` interno vinculado
- ✅ **Approval Gate** — ninguna ejecución contra sistemas reales sin aprobación explícita

---

## 📁 Estructura del Repositorio

```
QA-Agents-Ecosystem/
├── meta/                                    # Orquestador principal (Coordi + Biz)
│   ├── .opencode/agents/                    # Agentes ejecutables
│   ├── .opencode/skills/                    # Skills de orquestación
│   ├── docs/governance/coe-reviewer.md      # Contrato de revisión COE
│   ├── docs/plan/{plan_id}/                 # Artefactos de plan maestro
│   ├── AGENTS.md                            # Guía persistente del ecosistema
│   ├── DESIGN_INTEGRATION_PLAN.md           # Diseño de integración
│   └── opencode.json                        # Config + routers cross-repo
│
├── COE/                                     # Center of Excellence (Maru)
│   ├── .opencode/agents/maru.md
│   ├── .opencode/skills/                    # 20+ skills de gobernanza
│   ├── docs/qa-governance/                  # Artefactos de gobernanza
│   ├── docs/qa-governance/_plantilla/       # Plantillas base
│   ├── AGENTS.md
│   └── opencode.json
│
├── AUTO-TLC/                                # Automation Test (Scripto)
│   ├── .opencode/agents/automation-qa-orchestrator.md
│   ├── .opencode/skills/                    # 17 skills (6 fases + 11 apoyo)
│   ├── docs/knowledge/Automation_QA/        # Knowledge base estructurado
│   ├── docs/templates/                      # tc_template.md, tc_example.md
│   ├── utils/validate_encoding.py
│   ├── automation-plans/{plan_id}/          # Estado de planes activos
│   ├── AGENTS.md
│   ├── PROJECT_STRUCTURE.md
│   └── opencode.json
│
├── API-TLC/                                 # API Test (APU)
│   ├── .opencode/agents/api-tlc-orchestrator-api.agent.md
│   ├── .opencode/skills/                    # 21 skills (6 fases + 15 apoyo)
│   ├── tests/{App}/{Env}/{Tool}/{plan_id}/  # Estado de planes (obligatorio)
│   ├── AGENTS.md
│   ├── PROJECT_STRUCTURE.md
│   └── opencode.json
│
├── MANUAL-TLC/                              # Manual Test (MANU)
│   ├── .opencode/agents/                    # Orchestrator + Playwright MCP
│   ├── .opencode/skills/                    # 42 skills (6 fases + 36 conocimiento)
│   ├── templates/                           # tc_template.md, bdd_template.md, tc_example.md
│   ├── PRJ-{proyecto}/{ambiente}/           # Estructura gobernada de artefactos
│   ├── AGENTS.md
│   └── opencode.json
│
└── Intelligent_Performance_Test_Orchstrator/ # Performance Test (Perfie)
    ├── .opencode/agents/ptlc-orchestrator.md
    ├── .opencode/skills/                    # Skills PTLC (6 fases + apoyo)
    ├── docs/                                # Documentación técnica (01-09)
    ├── docs/plan/{plan_id}/                 # Planes de performance
    ├── tests/performance/{tool}/            # Scripts generados
    ├── scripts/measure_tokens.py
    ├── AGENTS.md
    └── opencode.json
```

---

## 🚀 Cómo Usar

### Desde `meta/` (Punto de entrada recomendado)

```bash
cd meta
opencode run "Necesito testear la API de pagos del e-commerce ShopPolymer"
```

Coordi detectará el dominio (API), delegará a **APU** (API-TLC), pedirá políticas a **Maru** (COE), y cerrará con **Biz**.

### Directo a un experto (consultas puntuales)

```bash
# Automation
cd AUTO-TLC && opencode run "¿Cómo aplico Page Object Model en Playwright?"

# API
cd API-TLC && opencode run "Genera matriz de pruebas desde este OpenAPI"

# Manual
cd MANUAL-TLC && opencode run "Crea casos de prueba para login con BDD"

# Performance
cd Intelligent_Performance_Test_Orchstrator && opencode run "Diseña workload model para 1000 users"

# Governance
cd COE && opencode run "Audita el plan de automatización actual"
```

---

## 📚 Knowledge Bases

Cada experto mantiene su knowledge base estructurado:

| Repo | Knowledge Base | Estructura |
|------|----------------|------------|
| **AUTO-TLC** | `docs/knowledge/Automation_QA/` | 8 categorías (fundamentos, frameworks, estrategias, herramientas, CI/CD, mejores prácticas, referencia, rules) |
| **API-TLC** | Skills embebidas | 21 skills con knowledge integrado |
| **MANUAL-TLC** | `.opencode/skills/kb-*` | 26 skills autónomas numeradas (kb-00 a kb-06) |
| **Performance** | `.opencode/skills/` + `docs/` | Skills + 9 docs técnicos (visión, arquitectura, pipeline, agente, skills, KB, optimización, gobernanza, reproducción) |
| **COE** | `.opencode/skills/` | Skills de gobernanza por disciplina + métricas + herramientas |

---

## 🛠️ Skills Comunes (Patrón 3 Niveles)

```
Nivel 1: .opencode/skills/README.md          → Índice maestro
Nivel 2: .opencode/skills/<skill>/SKILL.md   → Reglas + punteros a detalle
Nivel 3: docs/.../NN_Tema.md                 → Contenido autoritativo
```

**Regla**: Leer Nivel 2 antes de editar Nivel 3. No duplicar: actualizar existente y dejar puntero en skill.

---

## 📋 Plantillas Obligatorias

| Repo | Plantillas | Ubicación |
|------|------------|-----------|
| **AUTO-TLC** | `tc_template.md`, `tc_example.md` | `docs/templates/` |
| **MANUAL-TLC** | `tc_template.md`, `bdd_template.md`, `tc_example.md` | `templates/` (root) |
| **COE** | `plan.yaml`, `qa-quality-plan.md`, `governance-checklist.md`, `audit-report.md`, `improvement-plan.md`, `context_envelope.json` | `docs/qa-governance/_plantilla/` |

---

## 🔗 Rutas Clave por Agente

### Meta (Coordi + Biz)
- `.opencode/agents/test-lead-orchestrator.md` — Entry point y pipeline
- `.opencode/agents/biz.md` — Gate de stakeholders
- `.opencode/skills/test-lead-stakeholder/SKILL.md` — Gates de stakeholders
- `docs/governance/coe-reviewer.md` — Contrato de revisión COE
- `opencode.json` — `default_agent`, routers cross-repo

### COE (Maru)
- `.opencode/agents/maru.md` — Entry point y pipeline de gobernanza
- `.opencode/skills/README.md` — Índice maestro de skills
- `docs/qa-governance/` — Artefactos de gobernanza

### AUTO-TLC (Scripto)
- `.opencode/agents/automation-qa-orchestrator.md` — Entry point y pipeline
- `.opencode/skills/README.md` — Índice de 17 skills
- `docs/knowledge/Automation_QA/MASTER-README.md` — Índice knowledge base
- `utils/validate_encoding.py` — Validación UTF-8

### API-TLC (APU)
- `.opencode/agents/api-tlc-orchestrator-api.agent.md` — Entry point
- `.opencode/skills/README.md` — Índice de 21 skills
- `PROJECT_STRUCTURE.md` — Estructura obligatoria `tests/{App}/{Env}/{Tool}/`

### MANUAL-TLC (MANU)
- `.opencode/agents/` — Orchestrator + Playwright MCP config
- `.opencode/skills/README.md` — Índice de 42 skills
- `templates/` — Plantillas obligatorias (read-only source)
- `manual-project-structure` skill — Gobierna estructura `PRJ-{proyecto}/`

### Performance (Perfie)
- `.opencode/agents/ptlc-orchestrator.md` — Entry point y pipeline PTLC
- `.opencode/skills/README.md` — Índice maestro
- `.opencode/skills/ptlc-roadmap-decisiones/PRD.yaml` — Requisitos producto
- `docs/01-vision-general.md` a `docs/09-guia-reproduccion-sistema-fases.md` — Docs técnicos

---

## ⚙️ Configuración Cross-Repo

El archivo `meta/opencode.json` define **routers `mode: all`** que permiten invocar agentes de otros repos desde `meta/`:

```json
{
  "agents": {
    "auto-tlc-router": { "mode": "all", "command": "opencode run --agent automation-qa-orchestrator --dir ../AUTO-TLC" },
    "api-tlc-router":  { "mode": "all", "command": "opencode run --agent api-tlc-orchestrator-api --dir ../API-TLC" },
    "manual-tlc-router": { "mode": "all", "command": "opencode run --agent manual-tlc-orchestrator-manual --dir ../MANUAL-TLC" },
    "perf-tlc-router": { "mode": "all", "command": "opencode run --agent ptlc-orchestrator --dir ../Intelligent_Performance_Test_Orchstrator" },
    "coe-router":      { "mode": "all", "command": "opencode run --agent maru --dir ../COE" }
  }
}
```

---

## 📖 Documentación Adicional

- [`meta/DESIGN_INTEGRATION_PLAN.md`](meta/DESIGN_INTEGRATION_PLAN.md) — Diseño completo del ecosistema
- [`meta/AGENTS.md`](meta/AGENTS.md) — Guía persistente del orquestador
- Cada `AGENTS.md` de cada repo — Guía específica del agente

---

## 🏷️ Convenciones

- **Idioma primario**: Español (términos técnicos en English)
- **Encoding**: UTF-8 obligatorio (validar con `python utils/validate_encoding.py` en AUTO-TLC)
- **Plan state**: Cada experto persiste en su estructura (`automation-plans/`, `tests/...`, `PRJ-...`, `docs/plan/`)
- **Context envelope**: JSON acumulado por fase (`context_envelope.json`) para evitar re-leer artefactos

---

## 🤝 Contribuir

1. Cada experto es autónomo: respeta su `AGENTS.md`, skills y ciclo de vida
2. No dupliques docs: actualiza en knowledge base y deja puntero en skill
3. Sigue el patrón 3 niveles para skills
4. Mantén los límites de tokens (agente ≤3.2K, SKILL.md ≤2K, detalle ≤6K)

---

*QA-Agents-Ecosystem — Orquestación cross-disciplina de testing. Platform: OpenCode.*