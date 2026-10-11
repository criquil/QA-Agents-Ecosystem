---
name: auto-tlc-execution
description: "Fase 5 del AUTO-TLC — Genera la estructura y el codigo de automatizacion segun el stack seleccionado, captura selectores validados con Chrome DevTools MCP y ejecuta la suite con smoke test obligatorio primero. Usar tras la aprobacion del plan formal."
---

# AUTO-TLC-EXECUTION — Fase 5: Generacion y ejecucion

## Rol

Eres el ingeniero de automatizacion. Generas Page Objects y tests con el stack seleccionado, capturas selectores **validados contra el DOM real** y ejecutas la suite.

**DEBES** cargar las skills de apoyo antes de generar codigo. No se improvisa estructura.

## Precondicion bloqueante

Esta fase **no arranca** sin:

1. `awaiting_approval = false` — aprobacion explicita del usuario (Approval Gate)
2. `readiness_score >= 50` en la fase 2
3. Playwright MCP activo (GATE 2) para navegar la app real

Si falta cualquiera → `status: blocked`. Volver al orquestador.

## Skills de apoyo

Cargar **segun el stack y la necesidad** de la fase:

| Necesidad | Skill |
|---|---|
| Estructura base del proyecto | `automation-scaffold` |
| Page Objects y BasePage | `automation-pom` |
| Captura de selectores | `automation-selectors` |
| Datos externalizados | `automation-data` |
| Tags y filtros | `automation-tagging` |
| Configuracion de pipeline | `automation-cicd` |
| Fallo en ejecucion | `automation-troubleshooting` |
| Reglas A1-A9 | `automation-rules` |

## Flujo de trabajo

### Paso 1: Leer el plan completo

- `requirements` — aplicacion, entorno, stack
- `diagnostic` — riesgos, widgets JS, bloqueos
- `procedure_plan` — escenarios, tags, datos, orden
- `test_plan` — criterios de exito y trazabilidad

### Paso 2: Crear la estructura del proyecto

```
tests/{ApplicationName}/{Environment}/{stack}/{project_name}/
├── scripts/    ├── data/    ├── fixtures/    └── reports/
```

Usar `automation-scaffold`. Nunca generar la estructura completa de una sola vez: **modulo por modulo**.

### Paso 3: Capturar selectores con MCP — antes de escribir codigo

Orden obligatorio por cada flujo:

1. **Playwright MCP** — navegar a la URL real del entorno
2. **Chrome DevTools MCP** — `browser_snapshot` para inspeccionar el DOM
3. `browser_evaluate` — confirmar que el selector matchea **un solo** elemento
4. Interactuar con el elemento y verificar que responde
5. Registrar en `automation-plans/{plan_id}/selectors.md` con origen y fecha

> **Prohibido**: escribir un selector sin capturarlo. Un selector inventado produce timeouts de 30 s por paso y una tasa de exito de 0%.

Jerarquia: `id` > `name` > `data-testid` > `data-*` > ARIA > texto > `class` > XPath complejo.

### Paso 4: Generar codigo por escenario

Para cada escenario de la fase 3:

- **Page Object** — hereda de `BasePage`, selectores `UPPERCASE` con prefijo de rol, metodos de accion separados de los de verificacion
- **Test** — sin selectores, con los 4 tags obligatorios, datos desde `data/`
- **Datos** — `config.yaml`, `users.json`, `messages.json`, o `cases/TC_<ID>.json`

Si el diagnostico destino widgets JavaScript, aplicar el patron **click + type + Enter**, no `selectOption`.

### Paso 5: Ejecutar — smoke primero

Si `execute = true`:

```
1. Smoke           -> si falla, STOP. Reportar. No seguir.
2. Funcionales     -> happy path
3. Integracion     -> flujos multi-pagina
4. Negativos / Limites / Criticos
```

Nunca saltar el smoke. Un smoke rojo significa que el acceso o el ambiente esta roto; seguir genera una mountain de timeouts que no son fallos reales.

Capturar: stdout/stderr, archivo de resultados, hora de inicio y fin, screenshots y traces de los fallos.

### Paso 6: Empaquetar resultados

- Artefactos crudos en `tests/.../reports/`
- Resumen de ejecucion y cobertura de funcionalidades

## Formato de salida

```json
{
  "status": "completed | failed | smoke_failed | blocked | skipped_execution",
  "blockers": ["string"],
  "stack": "Playwright-TS",
  "project_path": "tests/{App}/{Env}/{stack}/{project_name}",
  "selectors_captured": {
    "total": 0,
    "validated": 0,
    "reused_from_catalog": 0,
    "detail_file": "automation-plans/{plan_id}/selectors.md"
  },
  "code_generated": {
    "page_objects": [
      { "file": "string", "feature": "string", "selectors": 0, "tests_using": 0 }
    ],
    "tests": [
      { "test_id": "TC-001", "file": "string", "tags": ["string"] }
    ],
    "data_files": ["string"]
  },
  "execution_results": [
    {
      "stage": "smoke | functional | integration | negative | boundary | critical",
      "status": "pass | fail | skipped",
      "duration_seconds": 0,
      "tests_total": 0,
      "tests_passed": 0,
      "tests_failed": 0,
      "tests_skipped": 0,
      "result_file": "string"
    }
  ],
  "coverage": {
    "features_total": 0,
    "features_automated": 0,
    "coverage_pct": 0
  },
  "violations": [
    { "rule": "A5", "description": "string", "file": "string" }
  ],
  "overall_pass": true,
  "recommendations": ["string"],
  "confidence": 0.0
}
```

## Reglas

- **Approval Gate**: sin aprobacion explicita → `blocked`. No ejecutar.
- **Smoke primero, siempre.** Si falla, detener y reportar; no continuar con etapas mayores.
- Ningun selector sin validar con Chrome DevTools MCP.
- Todo dato desde `data/` — input **y** output esperado. Cero hardcodeo.
- Los 4 tags obligatorios en todo test. Verificar con `--list` que el filtro lo encuentra.
- Los asserts deben coincidir con los criterios de exito del plan formal.
- Si `execute = false`, solo generar codigo y retornar `skipped_execution`.
- Ejecutar en **una** combinacion de stack. Multi-stack solo si se solicita.
- Registrar violaciones de reglas A1-A9 en `violations`. No ocultarlas.
- Documentar en el README del proyecto el stack usado y las skills aplicadas.

## Lectura bajo demanda

Este SKILL.md cubre el flujo, el gate y los formatos.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Sintaxis exacta del Page Object | `.opencode/skills/automation-pom/SKILL.md` |
| Sintaxis de la captura de selectores | `.opencode/skills/automation-selectors/SKILL.md` |
| Templates base del proyecto | `.opencode/skills/automation-scaffold/SKILL.md` |
| Sintaxis por framework | `docs/knowledge/Automation_QA/02-frameworks/03-playwright.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: el flujo de esta fase esta aca. Carga de apoyo **una** skill a la vez, segun la necesidad del momento — no las diez.