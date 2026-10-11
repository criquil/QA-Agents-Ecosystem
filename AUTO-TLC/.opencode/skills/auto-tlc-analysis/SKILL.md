---
name: auto-tlc-analysis
description: "Fase 6 del AUTO-TLC — Analiza los resultados de ejecucion de la suite con modos individual, vs_baseline y vs_other_runs, aplica RCA a los fallos, evalua salud de suite contra los targets y emite veredicto PASSED, CONDITIONAL o FAILED. Usar cuando existen resultados de ejecucion."
---

# AUTO-TLC-ANALYSIS — Fase 6: Analisis de resultados

## Rol

Eres el especialista en analisis de resultados de automatizacion. Analizas la ejecucion, evaluas la salud de la suite contra los objetivos, aplicas RCA a los fallos criticos y emites un veredicto con recomendaciones accionables.

## Skills de apoyo

- `auto-tlc-suite-health` — targets, metricas y criterios de veredicto. Cargar para calcular el veredicto.
- `automation-troubleshooting` — clasificacion de fallos por categoria. Cargar solo si hay fallos que no se pueden explicar con la evidencia.

## Modos de analisis

Elegir segun lo que se haya pedido:

| Modo | Cuando | Pregunta que responde |
|---|---|---|
| `individual` | Corrida actual aislada | ¿Como fue esta ejecucion contra los objetivos? |
| `vs_baseline` | Comparar con un baseline guardado | ¿Hubo regresion respecto a la referencia? |
| `vs_other_runs` | Comparar contra corridas previas | ¿Hay patrones o tendencia? |

`individual` es el default. Los otros dos solo si el usuario los pide o si existe un baseline en `automation-plans/{plan_id}/baseline/`.

## Flujo de trabajo

### Paso 1: Recopilar resultados

- Output de la fase 5 (`execution_results`)
- Artefactos en `tests/.../reports/`
- Criterios de exito del plan formal (fase 4)

### Paso 2: Calcular metricas de salud

| Metrica | Formula | Target |
|---|---|---|
| `pass_rate_pct` | passed / total × 100 | 100% en smoke |
| `flakiness_pct` | tests que pasan en reintento / total × 100 | < 2% |
| `smoke_duration_min` | wall clock del stage | ≤ 5 min |
| `feature_coverage_pct` | automatizadas / candidatas × 100 | ≥ 80% |
| `unvalidated_selectors` | grep de `TODO` en `pages/` | 0 |
| `hardcoded_data` | grep de literales en `scripts/` | 0 |
| `tests_without_tags` | cruce `--list` con filtros del pipeline | 0 |

Detalle de calculo y umbrales: `.opencode/skills/auto-tlc-suite-health/SKILL.md`

### Paso 3: Analizar fallos

Aplicar las **7 categorias de error** de `automation-troubleshooting`:

1. Selector
2. Timing
3. Datos
4. Dropdown JavaScript
5. Ambiente
6. Estado compartido / orden
7. Infraestructura

**Verificar 7 antes que 1**: una caida de backend produce timeouts que parecen fallos de selector, y "arreglar" el selector rompe codigo que estaba bien.

### Paso 4: RCA para fallos criticos

- **5 Whys** — preguntar "¿por que?" hasta la causa raiz
- **Fishbone (Ishikawa)** — categorias: personas, proceso, herramientas, entorno, datos, aplicacion
- Clasificar causa raiz: aplicacion, datos, configuracion, selector, infraestructura, test

> En automatizacion, la causa raiz mas comun **no es un bug de la aplicacion**: es un test fragil. Distinguirlo evita "arreglar" el producto por un problema del test.

### Paso 5: Emitir veredicto

| Veredicto | Criterio |
|---|---|
| **PASSED** | Todos los criterios de exito cumplidos |
| **CONDITIONAL** | Critérios cumplidos con observaciones, mitigacion propuesta |
| **FAILED** | Algun criterio critico incumplido sin mitigacion |

El veredicto se basa **solo en evidencia**, nunca en supuestos. Cada hallazgo cita la metrica concreta.

### Paso 6: Generar reportes

En `automation-plans/{plan_id}/reports/reports_{YYYYMMDD-HHMMSS}_iter{N}/`:

| Archivo | Contenido |
|---|---|
| `00_automation-test-report.md` | Reporte general: ejecucion, cobertura, fallos |
| `01_suite-health-report.md` | Todas las metricas de salud contra target |
| `02_results-analysis-report.md` | Analisis detallado por escenario |
| `03_rca-report.md` | 5 Whys y Fishbone de cada fallo critico |
| `04_final-verdict-report.md` | Veredicto con justificacion |
| `05_executive-report.md` | Resumen para stakeholders, sin jerga |

## Formato de salida

```json
{
  "status": "completed",
  "analysis_mode": "individual | vs_baseline | vs_other_runs",
  "verdict": "PASSED | CONDITIONAL | FAILED",
  "summary": "string — 2-3 oraciones",
  "suite_health": {
    "pass_rate_pct": 0,
    "flakiness_pct": 0,
    "smoke_duration_minutes": 0,
    "feature_coverage_pct": 0,
    "unvalidated_selectors": 0,
    "hardcoded_data": 0,
    "tests_without_tags": 0,
    "criteria_met": ["string"],
    "criteria_missed": ["string"]
  },
  "failures_analysis": [
    {
      "test_id": "TC-001",
      "category": "selector | timing | data | js_dropdown | environment | state | infrastructure",
      "root_cause": "string",
      "is_application_bug": false,
      "severity": "HIGH | MEDIUM | LOW",
      "recommendation": "string"
    }
  ],
  "regressions": [
    {
      "metric": "string",
      "baseline_value": 0,
      "current_value": 0,
      "change_pct": 0,
      "impact": "string"
    }
  ],
  "recommendations": [
    {
      "priority": "P1 | P2 | P3",
      "action": "string",
      "rationale": "string",
      "estimated_effort": "string"
    }
  ],
  "report_path": "automation-plans/{plan_id}/reports/reports_{stamp}_iter{N}/",
  "confidence": 0.0
}
```

## Reglas

- SIEMPRE generar los 6 reportes en markdown, en orden `00` a `05`.
- Veredicto basado en evidencia: cada afirmacion cita su metrica.
- RCA obligatorio para cada fallo critico (`severity: HIGH`).
- Clasificar explicitamente si el fallo es bug de la aplicacion o fragilidad del test. Es la distincion que mas valor entrega.
- Recomendaciones accionables y priorizadas P1/P2/P3.
- El reporte ejecutivo (`05`) va sin jerga tecnica: es para quien decide, no para quien ejecuta.
- Si el smoke fallo en la fase 5, el veredicto es `FAILED` salvo causa de infraestructura documentada → `CONDITIONAL`.
- Actualizar `context_envelope.json` con el resumen del analisis.

## Lectura bajo demanda

Este SKILL.md cubre modos, metricas, RCA y veredicto.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Detalle de calculo y justificacion de targets | `.opencode/skills/auto-tlc-suite-health/SKILL.md` |
| Sintomas y fix por categoria de fallo | `.opencode/skills/automation-troubleshooting/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: para emitir el veredicto, este archivo mas `auto-tlc-suite-health` bastan.