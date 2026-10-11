# 📁 Estructura Obligatoria de Proyecto — API-TLC

Esta es la **estructura de carpetas obligatoria** que debe generarse cuando se crea un nuevo proyecto de pruebas. **Bajo ninguna circunstancia** se debe utilizar la carpeta `docs/` para almacenar los planes o los artefactos del proyecto.

---

## 🗺️ Estructura Completa

```
tests/
└── {ApplicationName}/              ← Nivel 1: Nombre de la aplicación (ej: "MiApp", "Portal-Web")
    └── {Environment}/              ← Nivel 2: Entorno (ej: "QA", "Staging", "UAT")
        └── {selected_tool}/        ← Nivel 3: Herramienta seleccionada
        │   │                        (ej: Karate, Playwright, RestSharp, RestAssured)
        │   └── {plan_id}/          ← Nivel 4: Identificador único del plan
        │   │   ├── context_envelope.json   ← Estado del contexto (envelope acumulado)
        │   │   ├── plan.yaml               ← Plan activo (workflows resumibles)
        │   │   └── performance-test-plan.md ← Plan de pruebas formal (ISTQB/IEEE-829)
        │   └── {project_name}/           ← Contenedor del proyecto (coded o openai)
        │   │   ├── scripts/                    ← Scripts de pruebas generados
        │   │   ├── data/                       ← Datos de prueba
        │   │   ├── fixtures/                   ← Ficheros de configuración (appsettings, globals...)
        │   │   └── reports/                    ← Contenedor de reportes de ejecuciones
        │   │       ├── reports_{datestamp}_{iteration}/
        │   │       │   ├── 00_API-test-report.md
        │   │       │   ├── 01_metrics-kpis-report.md
        │   │       │   ├── 02_results-analysis-report.md
        │   │       │   ├── 03_rca-report.md
        │   │       │   ├── 04_final-verdict-report.md
        │   │       │   └── 05_executive-report.md
        │   │       └── reports_{datestamp}_{iteration}/
        │   │           └── (misma estructura por cada ejecución)
        └── {other_plan_id}/            ← Planes adicionales (si aplica)
            ├── context_envelope.json
            ├── plan.yaml
            └── performance-test-plan.md
```

---

## 📖 Descripción de Cada Nivel

### Nivel 1: `{ApplicationName}`
- **Propósito**: Agrupa todos los proyectos de pruebas pertenecientes a una aplicación.
- **Ejemplos**: `"MiApp"`, `"Portal-Web"`, `"Servicio-Usuarios"`, `"API-Comercio"`.
- **Nota**: Se recomienda usar un nombre descriptivo, en minúsculas o con guiones, sin espacios.

### Nivel 2: `{Environment}`
- **Propósito**: Separa los planes según el entorno donde se ejecutan.
- **Ejemplos**: `"QA"`, `"Staging"`, `"UAT"`, `"Prod"`, `"DEV"`.
- **Importante**: Los datos y resultados de un entorno no deben mezclarse con otros.

### Nivel 3: `{selected_tool}`
- **Propósito**: Identifica la herramienta de testing seleccionada para este plan.
- **Valores permitidos**: `Karate`, `Playwright`, `RestSharp`, `RestAssured`, u otras.
- **Regla**: Solo una herramienta por proyecto (single-tool por defecto, salvo que se solicite explícitamente).

### Nivel 4: `{plan_id}`
- **Propósito**: Identificador único del plan de pruebas.
- **Formato recomendado**: `{YYYYMMDD}-{ApplicationName}-{short-name}` (ej: `20251008-portal-web-regresion`).
- **Contenido**:
  - `context_envelope.json` — Estado acumulado del contexto (evita releer información ya sintetizada).
  - `plan.yaml` — Plan activo con workflows resumibles.
  - `performance-test-plan.md` — Documento formal de plan de pruebas (ISTQB/IEEE-829).

### `{project_name}/` — Contenedor del Proyecto
- **Propósito**: Alberga todos los scripts y recursos generados para el proyecto.
- **Organización por proyecto** (coded u openai):
  ```
  {project_name}/
  ├── scripts/                    ← Scripts de pruebas generados
  ├── data/                       ← Datos de prueba
  ├── fixtures/                   ← Ficheros de configuración (appsettings, globals...)
  └── reports/                    ← Reportes generados durante la ejecución
  ```

### `{reports}/` — Contenedor de Reportes
- **Propósito**: Todos los reportes del ciclo de vida de pruebas.
- **Orden numérico obligatorio** para mantener consistencia:
  | Archivo | Descripción |
  |---------|-------------|
  | `00_API-test-report.md` | Reporte general de pruebas de API |
  | `01_metrics-kpis-report.md` | Métricas y KPIs (tiempos, throughput, error rates) |
  | `02_results-analysis-report.md` | Análisis detallado de resultados |
  | `03_rca-report.md` | Root Cause Analysis de fallos |
  | `04_final-verdict-report.md` | Veredicto final (PASSED / CONDITIONAL / FAILED) |
  | `05_executive-report.md` | Reporte ejecutivo para stakeholders |

---

## 🚫 Prohibiciones

| Regla | Explicación |
|-------|-------------|
| ❌ **NO usar `docs/`** | Los planes **nunca** deben guardarse en `docs/plan/{plan_id}/`. |
| ❌ **NO mezclar entornos** | Cada entorno (`QA`, `Staging`, `UAT`) tiene su propio subdirectorio. |
| ❌ **NO mezclar herramientas** | Una carpeta `{selected_tool}` solo contiene la herramienta seleccionada. |
| ❌ **NO desordenar reportes** | Los reportes deben seguir el orden numérico `00` → `05`. |

---

## ✅ Ejemplo de Proyecto Real

```
tests/
└── Portal-Web/
    └── QA/
        └── Karate/
            ├── 20251008-portal-web-regresion/
            │   ├── context_envelope.json
            │   ├── plan.yaml
            │   └── performance-test-plan.md
            ├── portal-web-coded/
            │   ├── scripts/
            │   │   └── api_tests.feature
            │   ├── data/
            │   │   └── users.json
            │   └── fixtures/
            │       └── globals.js
            └── reports/
                ├── 00_API-test-report.md
                ├── 01_metrics-kpis-report.md
                ├── 02_results-analysis-report.md
                ├── 03_rca-report.md
                ├── 04_final-verdict-report.md
                └── 05_executive-report.md
        └── UAT/
            └── Karate/
                └── 20251008-portal-web-uat/
                    ├── context_envelope.json
                    ├── plan.yaml
                    └── performance-test-plan.md
```

---

## 🔄 Relación con los Entregables del Proyecto

| Entregable | Ubicación |
|------------|-----------|
| Plan activo | `{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/plan.yaml` |
| Estado del contexto | `{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/context_envelope.json` |
| Plan formal | `{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/performance-test-plan.md` |
| Scripts generados | `{ApplicationName}/{Environment}/{selected_tool}/{project_name}/scripts/` |
| Datos de prueba | `{ApplicationName}/{Environment}/{selected_tool}/{project_name}/data/` |
| Reporte general | `{ApplicationName}/{Environment}/{selected_tool}/{reports}/00_API-test-report.md` |
| Reporte final | `{ApplicationName}/{Environment}/{selected_tool}/{reports}/05_executive-report.md` |

---

**Nota**: Esta estructura es la versión 3.0 del Performance Test Life Cycle (PTLC) y se alinea con las convenciones definidas en `AGENTS.md`.
