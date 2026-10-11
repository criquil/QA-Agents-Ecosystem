# Skills — AUTO-TLC

> Indice maestro de las skills del proyecto. **Nivel 1 de 3**: indice → `SKILL.md` → knowledge.
> Leer este archivo primero para saber que skill cargar; nunca leer el knowledge completo.

Las skills se dividen en **dos capas**. **Scripto** (`automation-qa-orchestrator`) carga las de fase en el orden del ciclo, y las de apoyo solo cuando la fase activa las necesita.

## Capa 1 — Skills de fase (ciclo AUTO-TLC)

Se invocan **una por fase, en orden estricto**. Nunca sin su skill.

| # | Skill | Que produce | Output |
|---|---|---|---|
| 1 | `auto-tlc-intake` | Requisitos + seleccion de stack (single) | `scope.md` |
| 2 | `auto-tlc-diagnostics` | Readiness, riesgos, MCP, datos | `diagnostics.md` |
| 3 | `auto-tlc-procedure-plan` | Piramide, escenarios, datos, orden | `procedure-plan.md` |
| 4 | `auto-tlc-test-plan` | Plan formal IEEE-829 | `automation-test-plan.md` |
| — | **APPROVAL GATE** | Confirmacion explicita del usuario | `plan.yaml` |
| 5 | `auto-tlc-execution` | Estructura + selectores + ejecucion | `selectors.md`, `tests/` |
| 6 | `auto-tlc-analysis` | Salud de suite, RCA, veredicto | `reports/` |

## Capa 2 — Skills de apoyo

Se cargan **solo cuando la fase activa las requiere**.

| Skill | Dominio | Carga en | Knowledge de apoyo |
|---|---|---|---|
| `auto-tlc-suite-health` | Targets, metricas, veredicto | 4, 6 | — |
| `automation-rules` | Reglas A1-A9 y gates | todas | `08-rules/` |
| `automation-foundations` | Que automatizar, piramide, stack | 1, 3 | `01-fundamentos/`, `02-frameworks/` |
| `automation-selectors` | Captura con DevTools MCP | 5 | `Strategy/Selectors_Strategy/` |
| `automation-pom` | Page Object Model | 5 | `Strategy/POM/` |
| `automation-data` | Datos externalizados | 3, 5 | `Strategy/Data_Parametrization/` |
| `automation-tagging` | Los 4 tags obligatorios | 3, 5 | `Strategy/Test_Categorization/` |
| `automation-scaffold` | Estructura base | 5 | `Strategy/Boilerplate/` |
| `automation-cicd` | Pipelines y filtros | 5 | `05-ci-cd/` |
| `automation-troubleshooting` | Diagnostico y flakiness | 5, 6 | `Strategy/Troubleshooting/` |
| `automation-assets` | Catalogo y memoria | 5, 6 | `06-mejores-practicas/` |

## Flujo completo

```
Fase 0  init y ruteo        -> crear plan.yaml desde .opencode/templates/
  1  auto-tlc-intake        + automation-foundations
  2  auto-tlc-diagnostics   + automation-rules        -> puede bloquear
  3  auto-tlc-procedure-plan + automation-foundations, automation-tagging
  4  auto-tlc-test-plan     + auto-tlc-suite-health   -> awaiting_approval
  ==  APPROVAL GATE  ==     -> aprobacion explicita
  5  auto-tlc-execution     + selectors, pom, data, scaffold, cicd
  6  auto-tlc-analysis      + auto-tlc-suite-health, troubleshooting, assets
```

## Consulta directa — sin abrir el ciclo

Para una consulta puntual que **no** pide ciclo completo, usar la skill de apoyo directo sin crear `plan_id`:

| El usuario pide | Cargar |
|---|---|
| "que conviene automatizar" | `automation-foundations` |
| "crea un Page Object de X" | `automation-rules` → `automation-selectors` → `automation-pom` |
| "los datos estan hardcodeados" | `automation-data` |
| "los tests no corren en CI" | `automation-tagging` → `automation-cicd` |
| "el test falla a veces" | `automation-troubleshooting` |
| "monta el proyecto desde cero" | `automation-rules` → `automation-foundations` → `automation-scaffold` |
| "ya existe esto?" | `automation-assets` |
| "que tan sana esta la suite?" | `auto-tlc-suite-health` |

## Conocimiento asociado

Nivel 3. **No cargar completo**: navegar por indice o por `grep`.

| Ruta | Contenido |
|---|---|
| `docs/knowledge/Automation_QA/MASTER-README.md` | Indice maestro del knowledge |
| `docs/knowledge/Automation_QA/01-fundamentos/` | Que es automatizacion, piramide, cuando automatizar |
| `docs/knowledge/Automation_QA/02-frameworks/` | Selenium, Cypress, Playwright, Appium |
| `docs/knowledge/Automation_QA/03-herramientas/` | Page Objects, test data, reporting |
| `docs/knowledge/Automation_QA/04-estrategias/` | Data-driven, keyword-driven, BDD |
| `docs/knowledge/Automation_QA/05-ci-cd/` | Pipelines, GitHub Actions, Docker |
| `docs/knowledge/Automation_QA/06-mejores-practicas/` | Flaky tests, paralelismo, mantenimiento |
| `docs/knowledge/Automation_QA/07-referencia/` | Glosario, comandos, recursos |
| `docs/knowledge/Automation_QA/08-rules/` | Reglas estrictas del dominio |
| `docs/knowledge/Automation_QA/Strategy/` | POM, Selectors, Data, Tags, Boilerplate, Troubleshooting |

Otros documentos del proyecto:

| Documento | Para que |
|---|---|
| `PROJECT_STRUCTURE.md` | Estructura obligatoria de carpetas |
| `AGENTS.md` | Entry point y reglas de operacion |
| `.opencode/templates/plan.yaml` | Plantilla del plan activo |
| `.opencode/templates/context_envelope.json` | Plantilla del contexto acumulado |

Templates de casos: `docs/templates/tc_template.md` y `docs/templates/tc_example.md`.

---

*Skills — Automation QA. Platform: OpenCode.*