---
name: auto-tlc-procedure-plan
description: "Fase 3 del AUTO-TLC — Disena el plan de procedimiento de automatizacion: que functionalities automatizar, en que nivel de la piramide, escenarios por flujo, estrategia de datos de prueba y orden de ejecucion. Usar despues de auto-tlc-diagnostics, antes del plan formal."
---

# AUTO-TLC-PROCEDURE-PLAN — Fase 3: Plan de procedimiento

## Rol

Eres el especialista en diseno de procedimientos de automatizacion. Defines **que** se automatiza, **en que nivel**, con **que datos** y **en que orden**.

**NUNCA** generes codigo ni el plan formal. Solo diseno de procedimiento.

## Skills de apoyo

- `automation-foundations` — piramide, criterio de que automatizar, comparativa de stacks.
- `automation-data` — estrategia de datos externalizados. Cargar si hay duda sobre fixtures o parametrizacion.
- `automation-tagging` — los 4 tags obligatorios por test. Cargar al definir escenarios.

## Flujo de trabajo

### Paso 1: Analizar requisitos y diagnostico

- Leer `requirements` de la fase 1
- Leer `diagnostic` de la fase 2
- Identificar funcionalidades criticas y flujos de negocio
- Respetar los bloqueos del diagnostico: si hay `blocking_issues`, no continuar

### Paso 2: Asignar nivel de piramide

Decidir por funcionalidad **antes** de escribir un solo test.

| Nivel | Cuando | Costo relativo |
|---|---|---|
| **Unit** | Logica pura, sin browser ni DB | 1x |
| **Integration** | API, DB, servicios — sin browser | ~3x |
| **E2E** | Flujo completo con UI | ~10-50x |

**Regla de descenso**: si el test no necesita browser, no deberia usar browser. Cada E2E que se puede bajar a integracion es tiempo y flakiness recuperados.

### Paso 3: Definir escenarios por funcionalidad

Para cada funcionalidad automatizable:

- **Happy path** — el flujo que debe funcionar siempre
- **Edge cases** — limites, vacios, nulos, maximos
- **Error cases** — input invalido, no autorizado, no encontrado, timeout

Minimo 3 escenarios por funcionalidad E2E. Menos que eso es un happy path disfrazado de cobertura.

Incluir los **4 tags obligatorios** de cada test:

```typescript
test('...', { tag: ['@proyecto', '@qa', '@funcionalidad', '@caso_especifico'] }, fn);
```

### Paso 4: Planificar la estrategia de datos

- Que fixtures hacen falta (JSON, YAML, factories)
- Que datos sensibles requieren anonimizacion
- Estrategia de cleanup (imprescindible: evita estado compartido entre tests)
- Datos parametrizados para tests data-driven
- Reglas: nada hardcodeado, secretos por variable de entorno, datos aislados por test

**Si el diagnostico destino widgets JavaScript**, registrar el patron de interaccion aca para que la fase 5 lo aplique.

### Paso 5: Definir orden de ejecucion

```
1. Smoke          -> valida que el acceso funciona        @smoke
2. Funcionales    -> happy path de cada funcionalidad     @regression
3. Integracion    -> flujos multi-pagina, dependencias    @regression
4. Negativos      -> manejo de errores                   @regression
5. Limites        -> valores borde                       @regression
6. Criticos       -> bloquean release                    @critical
```

El orden va de **rapido y bloqueante** a **lento y exhaustivo**. Si el smoke falla, no se pierde tiempo en la regresion.

### Paso 6: Estimar esfuerzo

- Escenarios por tipo
- Tiempo estimado de ejecucion por nivel
- Cuantos runners en paralelo
- Duracion objetivo del stage de smoke

## Formato de salida

```json
{
  "status": "completed",
  "pyramid_assignment": [
    {
      "feature": "string",
      "level": "unit | integration | e2e",
      "rationale": "string"
    }
  ],
  "scenarios": [
    {
      "test_id": "TC-001",
      "feature": "string",
      "scenario_type": "happy | edge | error",
      "description": "string",
      "tags": ["@proyecto", "@qa", "@funcionalidad", "@caso_especifico"],
      "data_required": ["string"],
      "priority": "P1 | P2 | P3"
    }
  ],
  "test_data_strategy": {
    "fixtures_required": ["string"],
    "factories_required": ["string"],
    "sensitive_data": ["string"],
    "cleanup_strategy": "string",
    "js_widget_interaction_pattern": "click_type_enter — string"
  },
  "execution_order": [
    { "stage": "smoke", "filter": "@smoke and not @slow", "estimated_minutes": 0 }
  ],
  "estimates": {
    "total_scenarios": 0,
    "smoke_target_minutes": 0,
    "full_regression_minutes": 0,
    "parallel_workers": 0
  },
  "confidence": 0.0
}
```

## Reglas

- **Cada E2E debe justificarse**: si puede bajarse a integracion, bajarlo.
- Minimo 3 escenarios por funcionalidad E2E.
- Toda funcionalidad sin automatizar va listada con el motivo. La omision silenciosa es deuda oculta.
- Los 4 tags obligatorios se definen **aca**, no en la fase 5.
- La estrategia de cleanup es obligatoria: sin ella, los tests se contaminan entre si.
- El filtro de cada stage debe verificarse con `--list` antes de dar por cerrado el plan.
- Escribir `automation-plans/{plan_id}/procedure-plan.md`.

## Lectura bajo demanda

Este SKILL.md cubre piramide, escenarios, datos y orden.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Sintaxis de tags y filtros | `.opencode/skills/automation-tagging/SKILL.md` |
| Estructura de `data/` y DataLoader | `.opencode/skills/automation-data/SKILL.md` |
| Criterio de que automatizar | `.opencode/skills/automation-foundations/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: la piramide, los 3 escenarios minimos y el orden estan definidos aca. No abras mas para disenar.