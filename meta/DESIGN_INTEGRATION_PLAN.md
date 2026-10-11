# Ecosistema de QA — Test Lead + 4 Experteros + COE

## 1. Propósito

Un **orquestador** (`Coordi`) coordina **4 agentes operativos** que cubren las áreas de expertise en QA, y un **COE revisor** (`Maru`) que vela por las buenas prácticas. Todo vive en un mismo ecosistema de trabajo, con estado compartido y diálogo entre pares.

---

## 2. Arquitectura

```
┌───────────────────────────────────────────────────────────────┐
│                     COORDI (Test Lead)                          │
│              Orquestador · Entry point único                   │
│   Detecta dominio · Delega tareas · Monitorea · Integra        │
└────────┬──────────────┬──────────────┬──────────────┬────────┘
         │              │              │              │
         ▼              ▼              ▼              ▼
   ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
   │  PERFIE   │  │    APU    │  │   MANU    │  │  SCRIPTO  │
   │ PTLC      │  │ API-TLC   │  │ MANUAL-TLC│  │ AUTO-TLC  │
   │Performance│  │ API Test  │  │ Manual    │  │Automation │
   └───────────┘  └───────────┘  └───────────┘  └───────────┘
         │              │              │              │
         └──────────────┴──────┬───────┴──────────────┘
                                ▼
                        ┌───────────────┐
                        │ MARU (COE)    │
                        │   Reviewer    │
                        │ No operativo  │
                        └───────────────┘
```

**Flujo**: `Coordi` delega → experto ejecuta → `Maru` valida → `Coordi` cierra la fase.

---

## 3. Agentes

### 3.1 COORDI — Orquestador (Test Lead)

| Campo | Valor |
|---|---|
| Nombre friendly | **Coordi** |
| Nombre técnico | `test-lead-orchestrator` |
| Ubicación | `C:\Users\crisq\Repo\meta` |
| Archivo | `.opencode/agents/test-lead-orchestrator.md` |
| Config | `opencode.json` → `"default_agent": "test-lead-orchestrator"` |

**Responsabilidades**:
- Entry point único de todo request del usuario.
- Detecta el dominio del request: `performance` / `api` / `manual` / `automation` / `hybrid`.
- Genera `plan_id` (`YYYYMMDD-nombre-sistema`) y crea el plan maestro.
- **Delega** la tarea al experto correspondiente.
- **Monitorea** el progreso y persiste el estado del plan.
- **Activa al COE** una vez que el experto entrega su trabajo.
- **Integra** los resultados validados en el plan y reporte ejecutivo.
- **Facilita el diálogo** entre expertos cuando hay dependencias cruzadas.

**NO** ejecuta pruebas, **NO** genera scripts, **NO** ejecuta fases de testing. Solo orquesta, delega y consolida.

**Workflow**:
```
Phase 0 → Detectar dominio + crear plan.yaml
Phase 1 → Delegar al experto + pedir políticas al COE
Phase 2 → Recibir entrega del experto
Phase 3 → Activar validación del COE (Maru)
Phase 4 → Según veredicto del COE: PASSED → avanzar | NEEDS_REVISION → devolver | BLOCKED → escalar
Phase 5 → Integrar y generar reporte ejecutivo
```

---

### 3.2 Expertos Operativos (4)

Todos son pares, cada uno con su propia área de expertise en QA. Cada uno tiene su repo, su agente, sus skills y su ciclo de vida propio. **Coordi no los implementa, los invoca.**

| Area | Friendly | Nombre técnico | Repo | Ciclo |
|---|---|---|---|---|
| Performance Test | **Perfie** | `ptlc-orchestrator` | `Intelligent_Performance_Test_Orchstrator` | 6 fases (PTLC) |
| API Test | **APU** | `api-tlc-orchestrator-api` | `API-TLC` | 6 fases (API-TLC) |
| Manual Test | **MANU** | `manual-tlc-orchestrator-manual` | `MANUAL-TLC` | 6 fases (MANUAL-TLC) |
| Automation Test | **Scripto** | `automation-qa-orchestrator` | `AUTO-TLC` | 6 fases (AUTO-TLC) + Approval Gate |

---

#### PERFIE — Performance Test (`ptlc-orchestrator`)

- **Área**: Performance / Load Testing.
- **Repo**: `C:\Users\crisq\Repo\Intelligent_Performance_Test_Orchstrator`
- **Entry point**: `opencode.json` → `default_agent: ptlc-orchestrator`
- **Conocimiento**: `.opencode/skills/` — índice maestro en `.opencode/skills/README.md`
- **Ciclo de 6 fases** (orden estricto):
  1. `ptlc-intake` — Requisitos + selección de herramienta
  2. `ptlc-diagnostics` — Diagnóstico técnico + readiness
  3. `ptlc-procedure-plan` — Tipos de prueba, escenarios, workload model
  4. `ptlc-test-plan` — Plan formal ISTQB/IEEE-829
  5. `ptlc-execution` — Scripts + ejecución
  6. `ptlc-analysis` — Métricas + RCA + reporte final
- **Skills de apoyo**: `ptlc-workload-modeling`, `ptlc-metricas-kpis`, `ptlc-herramientas`, `ptlc-scripting`, `ptlc-monitoreo`, `ptlc-analisis-bottlenecks`, `ptlc-mejores-practicas`, `ptlc-tipos-de-pruebas`, `ptlc-fundamentos`, `ptlc-arquitectura-mapas`, `ptlc-fases-del-ciclo`, `ptlc-roadmap-decisiones`.
- **Entregables**: `docs/plan/{plan_id}/plan.yaml`, `docs/performance-test-plan.md`, `tests/performance/{tool}/`, `docs/performance-test-report.md`.

---

#### APU — API Test (`api-tlc-orchestrator-api`)

- **Área**: API Testing.
- **Repo**: `C:\Users\crisq\Repo\API-TLC`
- **Entry point**: `opencode.json` → `default_agent: API-TLC-orchestrator-api`
- **Ciclo de 6 fases** (orden estricto):
  1. `api-tlc-intake-api` — Requisitos + selección de herramienta (single-tool)
  2. `api-tlc-diagnostics-api` — Diagnóstico técnico + readiness
  3. `api-tlc-procedure-plan-api` — Tipos de prueba, escenarios, test data
  4. `api-tlc-test-plan-api` — Plan formal ISTQB/IEEE-829
  5. `api-tlc-execution-api` — Scripts + ejecución
  6. `api-tlc-analysis-api` — Métricas + RCA + reporte final
- **Skills de apoyo**: `api-tool-selector`, `api-test-strategy`, `api-metrics-analysis`, `api-diagnostics-rca`, `restsharp-api-workflow`, `karate-api-workflow`, `playwright-api-workflow`, `rest-assured-api-workflow`.
- **Skills de conversión independientes**: `export-response-to-openapi`, `openapi-to-response-example`, `generate-api-test-matrix`, `develop-detailed-test-cases`, `export-test-cases-to-gherkin`, `generate-test-artifacts`, `generate-bruno-collection`, `import-collection`.
- **Herramientas**: RestSharp, Karate, Playwright, REST Assured (single-tool por defecto).
- **Entregables**: `tests/{ApplicationName}/{Environment}/{tool}/{plan_id}/plan.yaml`, `performance-test-plan.md`, `reports/` con `00_API-test-report.md` + `01_metrics-kpis-report.md` + `03_rca-report.md` + `05_executive-report.md`.

---

#### MANU — Manual Test (`manual-tlc-orchestrator-manual`)

- **Área**: Manual / Exploratory / UAT / Usability / Accessibility Testing.
- **Repo**: `C:\Users\crisq\Repo\MANUAL-TLC`
- **Herramienta de soporte única**: **Playwright MCP Server** (navegación real + captura de evidencia).
- **Ciclo de 6 fases** (orden estricto):
  1. `manual-tlc-intake-manual` — Requisitos + selección de herramienta
  2. `manual-tlc-diagnostics-manual` — Diagnóstico técnico + readiness
  3. `manual-tlc-procedure-plan-manual` — Tipos de prueba + test data strategy
  4. `manual-tlc-test-plan-manual` — Plan formal ISTQB/IEEE-829
  5. `manual-tlc-execution-manual` — Sesiones manuales asistidas por MCP (screenshots, snapshots, traces, video, console, network)
  6. `manual-tlc-analysis-manual` — Métricas + RCA + veredicto
- **Skills**: 6 de ciclo + 10 de dominio/herramienta + 26 autónomas (`kb-*`).
- **Tipos de prueba cubiertos**: Funcionales, Sistema, Regresión, Smoke, Sanity, Exploratorias (SBTM), UAT.
- **Entregables**: `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/plan.yaml`, `Test_Cases/TestScript/`, `Test_Cases/BDD/`, `Test_Results/{fecha}/Evidence/`, `Issues&Bugs/`, `Test_Results_Analisis_&_RCA/`.

---

#### SCRIPTO — Automation Test (`automation-qa-orchestrator`)

- **Área**: Automation QA / UI Automation Testing.
- **Identidad**: **Scripto**, el "GPS de la automatización de pruebas".
- **Repo**: `C:\Users\crisq\Repo\AUTO-TLC`
- **Entry point**: `AGENTS.md` (obligatorio) → agente `.opencode/agents/automation-qa-orchestrator.md`
- **Idioma**: español, términos técnicos en inglés.

**Reglas obligatorias** (críticas):
  - `NO BYPASS` — nunca escribe código sin pasar por su skill.
  - `automation-rules` primero — gates A1-A9; si falla → estado `BLOCKED`. Ninguna tarea es "demasiado simple" como para saltarse un gate.
  - Selectores **validados contra DOM real** con Chrome DevTools MCP (nunca inventados).
  - Sin datos hardcodeados — input y output esperado parametrizados vía `DataLoader`.
  - Tags obligatorios: `@project @environment @functionality @specific_case` — sin tags, el pipeline no ejecuta nada.
  - **Reuso antes que creación** — Page Objects, helpers y datasets existentes primero.
  - Lectura bajo demanda — cargar solo lo necesario y frenar.

**Ciclo AUTO-TLC — 6 fases** (cada fase se ejecuta bajo su skill):

| # | Skill | Output |
|---|---|---|
| 1 | `auto-tlc-intake` | `automation-plans/{plan_id}/scope.md` — Requisitos + selección de stack (single) |
| 2 | `auto-tlc-diagnostics` | `automation-plans/{plan_id}/diagnostics.md` — Readiness, riesgos, MCP, datos |
| 3 | `auto-tlc-procedure-plan` | `automation-plans/{plan_id}/procedure-plan.md` — Qué automatizar, pirámide, escenarios |
| 4 | `auto-tlc-test-plan` | `automation-plans/{plan_id}/automation-test-plan.md` — Plan formal IEEE-829 |
| — | **APPROVAL GATE** | Entre fase 4 y 5. Sin aprobación explícita del usuario, la fase 5 devuelve `blocked`. El silencio no es aprobación. |
| 5 | `auto-tlc-execution` | `automation-plans/{plan_id}/selectors.md` + `tests/` — Estructura + selectores + ejecución |
| 6 | `auto-tlc-analysis` | `automation-plans/{plan_id}/reports/reports_{stamp}_iter{N}/` — Salud de suite, RCA, veredicto |

**Bloqueos**: `readiness_score < 50` en fase 2 detiene el ciclo. Smoke rojo en fase 5 detiene la ejecución.

**Skills de apoyo** (se cargan solo cuando la fase activa las requiere):

| Skill | Dominio | Fases |
|---|---|---|
| `auto-tlc-suite-health` | Targets numéricos, métricas, veredicto | 4, 6 |
| `automation-rules` | Transversal — gates y reglas A1-A9 | todas |
| `automation-foundations` | Qué automatizar, pirámide, stack | 1, 3 |
| `automation-selectors` | Captura y validación de selectores | 5 |
| `automation-pom` | Page Object Model | 5 |
| `automation-data` | Parametrización de datos | 3, 5 |
| `automation-tagging` | Categorización y tags | 3, 5 |
| `automation-cicd` | Pipelines e integración | 5 |
| `automation-scaffold` | Generación de estructura | 5 |
| `automation-troubleshooting` | Diagnóstico y flakiness | 5, 6 |
| `automation-assets` | Catálogo, reuso y memoria | 5, 6 |

**Consulta directa**: si el usuario trae una consulta puntual y no pide un ciclo completo, se atiende con la skill de apoyo correspondiente, sin abrir fases ni crear `plan_id`.

**Protocolo de lectura**: cargar hasta alcanzar, y frenar. Presupuesto por tarea: consulta puntual → 1 skill; tarea acotada → 1 skill + sección de lectura; ciclo completo → 2-3 skills secuencialmente.

**Entregables**: `automation-plans/{plan_id}/plan.yaml` (plan activo) · `automation-plans/{plan_id}/context_envelope.json` (contexto acumulado) · `tests/` con estructura estándar `pages/`, `tests/`, `helpers/`, `data/` · `docs/templates/tc_template.md` con ID `TC-[ID]` · validación de encoding con `utils/validate_encoding.py`.

---

### 3.3 MARU — COE / Reviewer (NO OPERATIVO)

| Campo | Valor |
|---|---|
| Nombre friendly | **Maru** |
| Nombre técnico (agente) | `maru` (router en `meta/opencode.json`; canónico en `../COE/.opencode/agents/maru.md`) |
| Contrato | `meta/docs/governance/coe-reviewer.md` — **documento, no agente** |
| Tipo | **Reviewer** — no es agente operativo |

> **Por qué el contrato no está en `.opencode/agents/`:** OpenCode registra *todo* `.md` dentro de esa carpeta como agente ejecutable y visible en el selector. Un contrato de revisión es documentación; dejarlo ahí creaba un segundo agente COE (`coe-reviewer`) compitiendo con `maru` y degradado — con las mismas skills de gobernanza pero sin instrucción de cargar la definición canónica del COE.

**Responsabilidades** (tres funciones, todas de gobernanza):

1. **Definir buenas prácticas**
   - Cuando `Coordi` define una tarea para un experto, `Maru` emite las políticas y estándares aplicables a esa tarea.
   - Base normativa: ISTQB, IEEE-829, buenas prácticas de QA.

2. **Validar post-ejecución**
   - Una vez que el experto completa la tarea, `Maru` valida que el trabajo cumplió con las buenas prácticas definidas.
   - Emite veredicto de validación: `PASSED` / `NEEDS_REVISION` / `BLOCKED`.

3. **Sugerir mejoras**
   - Aporta recomendaciones técnicas para mejorar el ciclo de testing.
   - **No implementa** las mejoras: las propone.

**Lo que Maru NO hace**:
- ❌ No genera scripts.
- ❌ No ejecuta pruebas.
- ❌ No ejecuta fases de testing.
- ❌ No es un par operativo más del mapa de crew.

---

## 4. Estado Compartido

| Artefacto | Ubicación | Contenido |
|---|---|---|
| Plan maestro | `docs/plan/{plan_id}/plan.yaml` | Fases, delegaciones, gate de stakeholder, estado |
| Brief de negocio | `docs/plan/{plan_id}/stakeholder_brief.md` | Intake de `Biz` + veredicto de aceptación |
| Envelope de contexto | `docs/plan/{plan_id}/context_envelope.json` | Contexto acumulado por fase |
| Diálogo entre pares | `docs/plan/{plan_id}/discussion.md` | Intercambios entre expertos |
| Políticas del COE | `docs/plan/{plan_id}/coe_review.md` | Buenas prácticas definidas + veredictos |
| Plan consolidado | `docs/plan/{plan_id}/combined_test_plan.md` | Plan integrado de todos los expertos |
| Reporte ejecutivo | `docs/plan/{plan_id}/executive_report.md` | Reporte final consolidado |

---

## 5. Skills Nuevas (en `meta/.opencode/skills/`)

| Skill | Función |
|---|---|
| `test-lead-stakeholder` | Gates de stakeholders: activa a `Biz` para el intake de negocio (Phase 0) y la aceptación/rechazo (Phase 5). |
| `test-lead-delegation` | Lógica de delegación de `Coordi`: mapeo dominio → experto, creación de tareas. |
| `test-lead-discussion` | Diálogo estructurado entre expertos para dependencias cruzadas. |
| `test-lead-validation` | Activación del COE: checklist de buenas prácticas → veredicto. |
| `test-lead-integration` | Fusión de entregas validadas en plan consolidado + reporte ejecutivo. |

---

## 6. Secuencia de Implementación

1. `meta/opencode.json` → `default_agent: test-lead-orchestrator`
2. `meta/AGENTS.md` → guía persistente del ecosistema
3. `meta/.opencode/agents/test-lead-orchestrator.md` → identidad y workflow de `Coordi`
4. `meta/docs/governance/coe-reviewer.md` → contrato de revisión que `Coordi` aplica a `Maru`
5. `meta/.opencode/skills/test-lead-delegation/SKILL.md`
6. `meta/.opencode/skills/test-lead-discussion/SKILL.md`
7. `meta/.opencode/skills/test-lead-validation/SKILL.md`
8. `meta/.opencode/skills/test-lead-integration/SKILL.md`
9. `meta/.opencode/skills/README.md` → índice maestro

---

## 7. Reglas Globales

- **Idioma**: español (términos técnicos en inglés).
- **Presupuesto de tokens**: agente ≤3.200 · `SKILL.md` ≤2.000 · detalle ≤6.000.
- **Approval Gate**: el usuario debe aprobar explícitamente antes de cualquier ejecución que afecte sistemas reales.
- **Coordinación**: cada agente experto conserva su propio `AGENTS.md`, skills y convenciones. `meta/` solo orquesta y revisa.
- **Idioma y tono**: cada agente experto conserva su personalidad (APU, Scripto, etc.); `Coordi` y `Maru` también tienen identidad propia.

---

## 8. Preguntas Abiertas

- ¿Cuál es el mecanismo concreto de invocación entre repos? (MCP server, `subagent` de OpenCode, o lectura/escritura de estado compartido en disco)
- ¿Maru es un agente independiente con modelo propio o una skill cargada por `Coordi`?
- ¿Los expertos comparten `plan_id` o cada uno genera el suyo y `Coordi` los vincula?

---

## 9. Estado de Implementación

Secuencia del §6 ejecutada al 100 %:

| # | Artefacto | Estado |
|---|---|---|
| 1 | `opencode.json` → `default_agent: test-lead-orchestrator` | ✅ |
| 2 | `AGENTS.md` → guía persistente del ecosistema | ✅ |
| 3 | `.opencode/agents/test-lead-orchestrator.md` → Coordi | ✅ |
| 4 | `docs/governance/coe-reviewer.md` → contrato de revisión que aplica `Maru` | ✅ |
| 5 | `.opencode/skills/test-lead-delegation/SKILL.md` | ✅ |
| 6 | `.opencode/skills/test-lead-discussion/SKILL.md` | ✅ |
| 7 | `.opencode/skills/test-lead-validation/SKILL.md` | ✅ |
| 8 | `.opencode/skills/test-lead-integration/SKILL.md` | ✅ |
| 9 | `.opencode/skills/README.md` → índice maestro | ✅ |

### Respuestas a las Preguntas Abiertas (§8)

1. **Mecanismo de invocación → routers cross-repo + handoff por disco.** La restricción original ("los subagentes son locales al workspace") queda resuelta en `meta/opencode.json`: los 5 agentes del crew se declaran con `mode: all` (lanzables como subagentes desde `meta/` y seleccionables como agente principal), `skills` apunta a las carpetas `.opencode/skills` de cada repo y `permissions.external_directory` habilita el acceso a `C:/Users/crisq/Repo/*`. Cada router lee su definición canónica y su `AGENTS.md` en su repo antes de operar, así que no hay duplicación de conocimiento. Orden de invocación: router como subagente → `opencode run --agent <id>` desde su repo → handoff por disco (`delegations/{task_id}.md` → `deliveries/{task_id}.md`).
2. **Maru → agente reviewer, con cerebro externo.** El agente real es `maru` (repo `../COE`), invocado desde `meta/` por el router de `opencode.json`. En `meta/` vive solo el *contrato* de revisión en `docs/governance/coe-reviewer.md`: políticas, checklist, umbrales de veredicto — **como documento, no como agente** (ver §3.3). El conocimiento de gobernanza vive en `../COE` (agente `maru`, 14 skills), ya existente. Sin duplicación de conocimiento ni dos agentes COE compitiendo.
3. **`plan_id` → uno maestro + uno interno por experto.** `Coordi` genera el `plan_id` maestro; cada experto genera el suyo en su repo y lo vincula con `meta_plan_id` + `task_id` en la entrega. Así cada repo conserva su namespace y `Coordi` puede consolidar.

### Stakeholders (`Biz`) — decisión de diseño

- **Qué es:** el agente de stakeholders (negocio/cliente) del ecosistema, en `meta/.opencode/agents/biz.md`. No es proveedor de evidencia: fija el *qué* y el *por qué*; `Coordi` decide el *cómo* y a quién delega.
- **Obligatoriedad:** todo request QA abre con su gate de intake en Phase 0 (brief de negocio → `stakeholder_brief.md`) y cierra con su veredicto en Phase 5. **Sin brief no se delega; sin `ACCEPTED` no se cierra.** La regla vive en `AGENTS.md`, en el agente de `Coordi` y en la skill `test-lead-stakeholder`.
- **Naturaleza:** stakeholder obligatorio, no opcional. Distingue el cierre técnico (`PASSED` del COE) del cierre de negocio (`ACCEPTED` de `Biz`); son gates independientes.
- **Restricción:** un subagente no puede entrevistar al usuario. Si `Biz` corre como subagente, redacta el brief y deja las dudas en `open_questions` para que `Coordi` las traslade; la entrevista completa es posible cuando el usuario abre sesión directamente con `Biz` (`mode: all`).

### Nota de alcance

`meta/` orquesta, delega, valida e integra; **no ejecuta pruebas ni escribe código de test**. Cada experto conserva su repo, su `AGENTS.md`, sus skills y su ciclo de 6 fases.