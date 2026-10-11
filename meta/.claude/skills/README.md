# Test Lead Skills Pack — Índice Maestro

> **Este archivo es el punto de entrada único del knowledge base de orquestación.** Aquí viven los procedimientos de `Coordi` (orquestación), los gates de `Biz` (stakeholders) y el contrato de `Maru` (gobernanza). El conocimiento técnico de cada disciplina vive en el repo de su experto.
> **Para agentes AI:** usar este índice para navegar; leer el `SKILL.md` de la skill que corresponda y, de ahí, el contrato de handoff (`docs/plan/{plan_id}/`).

---

## 🏗️ Arquitectura

- **Entry point obligatorio:** `test-lead-orchestrator` (Coordi, en `.claude/agents/test-lead-orchestrator.md`) — todo request entra por él. Orquesta 6 fases (gate de negocio → detección → delegación → entrega → validación → veredicto → aceptación).
- **Crew:** 1 stakeholder (**Biz**) + 4 expertos operativos (Perfie, APU, MANU, Scripto) + 1 COE reviewer (Maru). Cada experto es autónomo en su repo: aquí no se reimplementa su conocimiento.
- **Stakeholders siempre:** `Biz` interviene en los dos extremos — brief de negocio en Phase 0 (sin brief no se delega) y aceptación en Phase 5 (sin `ACCEPTED` no se cierra).
- **Invocación cross-repo:** los expertos están en otras carpetas pero son invocables desde `meta/` vía subagentes router en `.claude/agents/` que leen su repo hermano por ruta relativa. Orden: router como subagente → `claude --agent` con el cwd en su repo → handoff por disco.

---

## 🤖 Skills del Pipeline (5)

Cada skill es el procedimiento completo de una función de `Coordi` (lecturas obligatorias, workflow, formato de salida y reglas). Se cargan una por fase, nunca todas.

| Skill | Fase | Rol |
|-------|------|-----|
| [test-lead-stakeholder](test-lead-stakeholder/SKILL.md) | 0 y 5 | Activa a `Biz`: brief de negocio (intake) y aceptación/rechazo del plan consolidado |
| [test-lead-delegation](test-lead-delegation/SKILL.md) | 1 | Mapea dominio → experto y escribe el contrato de tarea (handoff) |
| [test-lead-discussion](test-lead-discussion/SKILL.md) | 2 | Diálogo entre expertos ante dependencias cruzadas |
| [test-lead-validation](test-lead-validation/SKILL.md) | 3-4 | Activa al COE y resuelve el veredicto (PASSED / NEEDS_REVISION / BLOCKED) |
| [test-lead-integration](test-lead-integration/SKILL.md) | 5 | Fusiona entregas validadas y genera el reporte ejecutivo |

## 🧭 Agentes de `meta/` (2)

> Todo `.md` dentro de `.claude/agents/` es registrado por Claude Code como **agente ejecutable**. Los contratos y documentos viven fuera, en `docs/`.

| Agente | Friendly | Tipo | Rol |
|--------|----------|------|-----|
| [test-lead-orchestrator](../agents/test-lead-orchestrator.md) | **Coordi** | `primary` | Orquestador · entry point único · delega, monitorea, integra |
| [biz](../agents/biz.md) | **Biz** | `all` | Stakeholders · fija el qué y el porqué · prioriza y acepta |

## 🧑‍🤝‍🧑 Expertos (invocados cross-repo, no implementados aquí)

| Área | Friendly | Agente | Repo | Ciclo |
|---|---|---|---|---|
| Performance | **Perfie** | `ptlc-orchestrator` | `../Intelligent_Performance_Test_Orchstrator` | 6 fases (PTLC) |
| API | **APU** | `API-TLC-orchestrator-api` | `../API-TLC` | 6 fases (API-TLC) |
| Manual | **MANU** | `MANUAL-TLC-orchestrator-manual` | `../MANUAL-TLC` | 6 fases (MANUAL-TLC) |
| Automation | **Scripto** | `automation-qa-orchestrator` | `../AUTO-TLC` | 6 fases (AUTO-TLC) + Approval Gate |
| COE | **Maru** | `maru` | `../COE` | Emisión de políticas + validación |

---

## 🔍 Lookup Rápido por Necesidad

| Necesito... | Ir a |
|-------------|------|
| Definir el objetivo de negocio antes de delegar | [test-lead-stakeholder](test-lead-stakeholder/SKILL.md) Gate 1 |
| Saber a qué experto delegar | [test-lead-delegation](test-lead-delegation/SKILL.md) |
| Escribir / emitir un contrato de tarea | [test-lead-delegation](test-lead-delegation/SKILL.md) |
| Invocar a un experto que vive en otro repo | `../agents/test-lead-orchestrator.md` §`<invocation>` |
| Resolver una dependencia entre disciplinas | [test-lead-discussion](test-lead-discussion/SKILL.md) |
| Validar una entrega / emitir veredicto | [test-lead-validation](test-lead-validation/SKILL.md) |
| Consolidar plan + reporte ejecutivo | [test-lead-integration](test-lead-integration/SKILL.md) |
| Cerrar el plan (aceptación de negocio) | [test-lead-stakeholder](test-lead-stakeholder/SKILL.md) Gate 2 |
| Políticas y checklist de buenas prácticas | Agente `maru` (router) + contrato `docs/governance/coe-reviewer.md` |

## 🔄 Ciclo de vida del estado (resumible)

```
plan.yaml  ──►  stakeholder_brief.md  ──►  delegations/{task_id}.md  ──►  deliveries/{task_id}.md
   ▲                                                        │
   │                                             validation/{task_id}.json
   │                                                        │
   └──────────  combined_test_plan.md  ◄──────────────────────────────────┘
                 executive_report.md  ──►  ACCEPTED / REJECTED (Biz)
```

## 📄 Entregables (bajo `docs/plan/{plan_id}/`)

- `plan.yaml` — plan maestro: fases, delegaciones, gate de stakeholder, veredictos, estado
- `stakeholder_brief.md` — brief de negocio de `Biz` + veredicto de aceptación
- `context_envelope.json` — contexto acumulado por fase (no releer lo ya sintetizado)
- `discussion.md` — diálogo entre pares: issues abiertos y decisiones resueltas
- `coe_review.md` — políticas emitidas por el COE + historial de veredictos
- `delegations/` · `deliveries/` · `validation/` — handoff de tareas
- `combined_test_plan.md` — plan integrado de todas las disciplinas
- `executive_report.md` — reporte ejecutivo final

## 📏 Límites de tamaño

`agents/*.md` ≤3.200 tokens · `SKILL.md` ≤2.000 · `CLAUDE.md` ≤1.400. Al agregar una sección, revisar que el archivo no exceda su límite.

---

*Skills de orquestación y gobernanza del ecosistema de QA — el conocimiento de cada disciplina vive en el repo de su experto.*
