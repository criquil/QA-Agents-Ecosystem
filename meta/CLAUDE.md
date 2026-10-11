# meta — Ecosistema de QA (Coordi + Biz)

Guía persistente para agentes Claude Code — Ecosistema de QA (Stakeholder + Coordi + 4 expertos + COE).

---

## Qué es

**Ecosistema de QA cross-disciplina**: un orquestador (**Coordi**, Test Lead) delega en 4 expertos — **Perfie** (performance), **APU** (API), **MANU** (manual), **Scripto** (automation) — activa al COE (**Maru**) como reviewer de gobernanza tras cada entrega, y abre/cierra cada ciclo con **Biz** (stakeholders).

`meta/` **NO ejecuta pruebas ni escribe código de test**: solo orquesta, delega, valida e integra. Cada experto conserva su repo, `CLAUDE.md`, skills y ciclo de vida.

**Idioma primario: español** en documentación, output y navegación (términos técnicos en English).

---

## Entry point

**`test-lead-orchestrator` (Coordi) es el entry point obligatorio** de todo request (agente en `.claude/agents/`). Todo entra por él:

1. Phase 0 · **Gate de stakeholders (Biz)** + detectar dominio + crear `plan.yaml`
2. Phase 1 · Delegar al experto + pedir políticas al COE
3. Phase 2 · Recibir entrega del experto
4. Phase 3 · Activar validación del COE
5. Phase 4 · Resolver veredicto (PASSED → avanzar · NEEDS_REVISION → devolver · BLOCKED → escalar)
6. Phase 5 · Integrar → plan consolidado + reporte ejecutivo → **aceptación de Biz**

Fuera del ciclo QA (consultas de tooling, preguntas generales) → responder directamente o resolver con los subagentes `general-purpose`/`Explore`.

---

## Crew

| Área | Friendly | Agente (entry point del repo) | Repo |
|---|---|---|---|
| Stakeholders | **Biz** | `biz` (gate de negocio) | local |
| Performance Test | **Perfie** | `ptlc-orchestrator` | `../Intelligent_Performance_Test_Orchstrator` |
| API Test | **APU** | `API-TLC-orchestrator-api` | `../API-TLC` |
| Manual Test | **MANU** | `MANUAL-TLC-orchestrator-manual` | `../MANUAL-TLC` |
| Automation Test | **Scripto** | `automation-qa-orchestrator` | `../AUTO-TLC` |
| COE / Reviewer | **Maru** | `maru` (independiente) | `../COE` |

En `meta/` viven el **agente de stakeholders** (`biz.md`) y el **contrato de revisión** (`docs/governance/coe-reviewer.md`), sin duplicar cerebros. Ojo: todo `.md` en `.claude/agents/` es un agente ejecutable — los contratos van en `docs/`.

---

## Reglas obligatorias

- **Stakeholders siempre** — todo request QA abre con el gate de `Biz` (brief de negocio) en Phase 0 y cierra con su aceptación en Phase 5. Sin brief no se delega; sin `ACCEPTED` no se cierra.
- **Delegación obligatoria** — ninguna tarea QA se resuelve en `meta/`: siempre va a ≥1 experto del crew según el dominio detectado.
- **No operar** — `Coordi` no ejecuta pruebas ni genera scripts; `Maru` no implementa, solo define políticas y valida; `Biz` no prueba, solo prioriza y acepta.
- **Un `plan_id` maestro** en `meta/`; cada experto genera su `plan_id` interno y lo vincula con `meta_plan_id` + `task_id`.
- **Invocación cross-repo** — los expertos viven en otras carpetas pero son invocables desde `meta/` (subagentes router en `.claude/agents/` que leen su repo por ruta relativa). Orden: router como subagente → `claude --agent` con el cwd en su repo → handoff por disco.
- **`<pre_execution>`** — toda skill de `meta/` con esa sección DEBE leer lo que lista antes de producir output.
- **3 niveles** — `.claude/skills/README.md` (índice maestro) → `SKILL.md` de la skill → detalle autoritativo. Leer el Nivel 2 antes de editar un Nivel 3.
- **Approval Gate** — ninguna fase de ejecución contra sistemas reales sin aprobación explícita del usuario. El silencio no es aprobación.
- **Idioma y tono** — cada experto conserva su personalidad; `Coordi`, `Maru` y `Biz` tienen identidad propia.

---

## Estado Compartido

Todo bajo `docs/plan/{plan_id}/`:

| Artefacto | Contenido |
|---|---|
| `plan.yaml` | Plan maestro: fases, delegación, gate de stakeholder, estado |
| `stakeholder_brief.md` | Brief de negocio de `Biz` + veredicto de aceptación |
| `context_envelope.json` | Contexto acumulado por fase |
| `discussion.md` | Diálogo entre pares (dependencias cruzadas) |
| `coe_review.md` | Políticas del COE + veredictos |
| `combined_test_plan.md` | Plan integrado de todos los expertos |
| `executive_report.md` | Reporte ejecutivo final |
| `delegations/{task_id}.md` | Contrato de tarea enviado al experto |
| `deliveries/{task_id}.md` | Entrega del experto |
| `validation/{task_id}.json` | Veredicto del COE |

---

## Presupuesto de tokens

- **Índice antes que documento**: dudas → `SKILL.md`/índice; detalle → sección con `grep -n "^## "` + `Read` por offset/limit.
- **Límites**: agente ≤3.200 · `SKILL.md` ≤2.000 · `CLAUDE.md` ≤1.400 tokens. Al agregar sección, revisar el límite.
- **Envelope acumulado**: cada fase persiste su bloque; las siguientes lo cargan y no releen lo ya sintetizado.

---

## Entregables

- `docs/plan/{plan_id}/plan.yaml` — plan activo (workflows resumibles)
- `docs/plan/{plan_id}/stakeholder_brief.md` — brief de negocio + aceptación
- `docs/plan/{plan_id}/combined_test_plan.md` — plan consolidado de las disciplinas
- `docs/plan/{plan_id}/executive_report.md` — reporte ejecutivo con veredicto

---

## Rutas clave

- `.claude/agents/test-lead-orchestrator.md` — entry point y pipeline de Coordi
- `.claude/agents/biz.md` — agente de stakeholders (gate de entrada y salida)
- `docs/governance/coe-reviewer.md` — contrato de revisión del COE (aplicado por `maru`)
- `.claude/skills/test-lead-stakeholder/SKILL.md` — gates de stakeholders
- `.claude/skills/README.md` — índice maestro de skills
- `.claude/settings.json` — permisos y acceso a repos hermanos
- `DESIGN_INTEGRATION_PLAN.md` — diseño del ecosistema