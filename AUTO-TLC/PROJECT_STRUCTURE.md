# Estructura Obligatoria — AUTO-TLC

Estructura de carpetas del **Automation Test Life Cycle**. Los planes viven en `automation-plans/`; el codigo generado vive en `tests/`.

---

## Estructura Completa

```
automation-plans/
└── {plan_id}/                        ← plan_id = YYYYMMDD-{app}-{short-name}
    ├── plan.yaml                     ← estado del plan, workflows resumibles
    ├── context_envelope.json         ← contexto acumulado entre fases
    ├── scope.md                      ← Fase 1: alcance + stack seleccionado
    ├── diagnostics.md                ← Fase 2: readiness, riesgos, brechas
    ├── procedure-plan.md             ← Fase 3: escenarios, piramide, orden
    ├── automation-test-plan.md       ← Fase 4: plan formal IEEE-829/ISTQB
    ├── selectors.md                  ← tabla de selectores validados (MCP)
    └── reports/
        └── reports_{YYYYMMDD-HHMMSS}_iter{N}/
            ├── 00_automation-test-report.md
            ├── 01_suite-health-report.md
            ├── 02_results-analysis-report.md
            ├── 03_rca-report.md
            ├── 04_final-verdict-report.md
            └── 05_executive-report.md

tests/
└── {ApplicationName}/                ← PascalCase. Ej: PortalWeb, ServicioUsuarios
    └── {Environment}/                ← dev | qa | staging | uat | prod
        └── {stack}/                  ← {Framework}-{Lenguaje}. Ej: Playwright-TS
            └── {project_name}/       ← nombre del proyecto de automatizacion
                ├── scripts/          ← Page Objects, tests, specs
                ├── data/             ← datos de prueba externalizados
                ├── fixtures/         ← configuracion (globals, config, auth)
                └── reports/          ← artefactos crudos de ejecucion
```

---

## Descripcion por Nivel

### `automation-plans/{plan_id}/`

Agrupa todo el estado documental de un ciclo. Es la **unidad de reanudacion**: si el contexto se pierde, se releen estos archivos.

| Archivo | Contenido | Escrito por |
|---|---|---|
| `plan.yaml` | Las 6 fases con su estado | Orquestador, tras cada fase |
| `context_envelope.json` | Sintesis acumulada de fases previas | Orquestador, tras cada fase |
| `scope.md` | Inventario de automatizacion + stack | Fase 1 |
| `diagnostics.md` | Readiness, riesgos, brechas | Fase 2 |
| `procedure-plan.md` | Escenarios, piramide, orden, estrategia de datos | Fase 3 |
| `automation-test-plan.md` | Plan formal IEEE-829 | Fase 4 |
| `selectors.md` | Selectores capturados con DevTools MCP | Fase 5 |
| `reports/` | Reportes numerados de cada ejecucion | Fase 6 |

**Formato de `plan_id`**: `YYYYMMDD-{app}-{short-name}`
Ejemplos: `20261011-portal-web-regresion`, `20261011-simpsonsapi-login`

### `tests/{ApplicationName}/{Environment}/{stack}/{project_name}/`

Codigo generado. Un cambio de entorno o de stack **nunca** reutiliza la carpeta del anterior.

| Subcarpeta | Contenido | Regla |
|---|---|---|
| `scripts/` | Page Objects, tests, specs | Estructura POM estandar |
| `data/` | `config.yaml`, `users.json`, `messages.json`, `forms.json`, `cases/` | Sin datos hardcodeados |
| `fixtures/` | Config de ejecucion, auth, globals | Sin secretos reales versionados |
| `reports/` | Artefactos crudos: JSON, JUnit, screenshots, traces | Versionado opcional |

### Valores permitidos

| Nivel | Valores | Nota |
|---|---|---|
| `{ApplicationName}` | PascalCase, sin espacios | `PortalWeb`, `ServicioUsuarios` |
| `{Environment}` | `dev` `qa` `staging` `uat` `prod` | Lista cerrada. No mezclar |
| `{stack}` | `{Framework}-{Lenguaje}` | `Playwright-TS`, `Selenium-Python`, `Cypress-TS`, `Playwright-Python`, `Selenium-Java`, `Appium-JS` |
| `{project_name}` | kebab-case | `portal-web-regresion` |

**Regla de stack**: una sola combinacion por plan. Cambiar de stack es un plan nuevo, no una migracion dentro del mismo.

---

## Reportes — Orden Obligatorio

| Archivo | Descripcion |
|---|---|
| `00_automation-test-report.md` | Reporte general de la ejecucion |
| `01_suite-health-report.md` | Salud de suite: flakiness, duracion, cobertura |
| `02_results-analysis-report.md` | Analisis detallado de resultados |
| `03_rca-report.md` | Root Cause Analysis de fallos |
| `04_final-verdict-report.md` | Veredicto: PASSED / CONDITIONAL / FAILED |
| `05_executive-report.md` | Reporte ejecutivo para stakeholders |

---

## Prohibiciones

| Regla | Explicacion |
|---|---|
| **NO mezclar entornos** | `qa` y `prod` tienen carpetas separadas |
| **NO mezclar stacks** | Un `{stack}` solo contiene esa combinacion |
| **NO desordenar reportes** | Siempre `00` a `05` |
| **NO planes en `docs/`** | `docs/` es solo knowledge y templates |
| **NO secretos en `fixtures/`** | Se inyectan por variable de entorno o gestor |
| **NO datos hardcodeados en `scripts/`** | Todo sale de `data/` |

---

## Ejemplo Real

```
automation-plans/
└── 20261011-portal-web-regresion/
    ├── plan.yaml
    ├── context_envelope.json
    ├── scope.md
    ├── diagnostics.md
    ├── procedure-plan.md
    ├── automation-test-plan.md
    ├── selectors.md
    └── reports/
        └── reports_20261011_093000_iter1/
            ├── 00_automation-test-report.md
            ├── 01_suite-health-report.md
            ├── 02_results-analysis-report.md
            ├── 03_rca-report.md
            ├── 04_final-verdict-report.md
            └── 05_executive-report.md

tests/
└── PortalWeb/
    └── qa/
        └── Playwright-TS/
            └── portal-web-regresion/
                ├── scripts/
                │   ├── BasePage.ts
                │   ├── LoginPage.ts
                │   └── test_login.spec.ts
                ├── data/
                │   ├── config.yaml
                │   ├── users.json
                │   └── cases/TC_001.json
                ├── fixtures/
                │   └── auth.json
                └── reports/
                    └── results.json

            └── UAT/                    ← otro entorno, mismo stack
                └── ...
```

---

## Relacion con los Entregables

| Entregable | Ubicacion |
|---|---|
| Plan activo | `automation-plans/{plan_id}/plan.yaml` |
| Contexto acumulado | `automation-plans/{plan_id}/context_envelope.json` |
| Alcance y stack | `automation-plans/{plan_id}/scope.md` |
| Diagnostico | `automation-plans/{plan_id}/diagnostics.md` |
| Plan de procedimiento | `automation-plans/{plan_id}/procedure-plan.md` |
| Plan formal | `automation-plans/{plan_id}/automation-test-plan.md` |
| Selectores validados | `automation-plans/{plan_id}/selectors.md` |
| Codigo generado | `tests/{ApplicationName}/{Environment}/{stack}/{project_name}/scripts/` |
| Datos de prueba | `tests/{ApplicationName}/{Environment}/{stack}/{project_name}/data/` |
| Reporte final | `automation-plans/{plan_id}/reports/reports_{stamp}_iter{N}/04_final-verdict-report.md` |

---

*Estructura v1.0 — Automation Test Life Cycle (AUTO-TLC). Platform: Claude Code.*