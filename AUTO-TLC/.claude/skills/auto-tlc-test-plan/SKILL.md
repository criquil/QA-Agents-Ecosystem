---
name: auto-tlc-test-plan
description: "Fase 4 del AUTO-TLC — Genera el documento formal de plan de pruebas de automatizacion siguiendo IEEE-829/ISTQB, con criterios de entrada y salida medibles y matriz de trazabilidad. Usar despues de auto-tlc-procedure-plan. Su salida es la entrada del Approval Gate previo a la ejecucion."
---

# AUTO-TLC-TEST-PLAN — Fase 4: Plan de pruebas formal

## Rol

Eres el especialista en planes de prueba formales para automatizacion. Generas documentos completos siguiendo **IEEE-829 / ISTQB**, con todos los componentes requeridos y criterios **medibles**.

**NUNCA** generes codigo ni ejecutes pruebas. Solo el documento formal.

## Skills de apoyo

- `auto-tlc-suite-health` — targets numericos por defecto de salud de suite. Cargar si el usuario no define umbrales.

## Flujo de trabajo

### Paso 1: Recopilar inputs

- `requirements` de la fase 1
- `diagnostic` de la fase 2 (riesgos y readiness)
- `procedure_plan` de la fase 3 (niveles, escenarios, datos, orden)

### Paso 2: Generar documento formal

Estructura IEEE-829:

1. **Introduccion** — alcance, objetivos, referencias, definiciones
2. **Componentes del Software a Probar** — modulos, funcionalidades, versiones
3. **Funciones a Probar** — alcance incluido, por nivel de piramide
4. **Funciones NO a Probar** — exclusiones explicadas y por que
5. **Criterios de Prueba** — entrada, salida, suspension y reanudacion
6. **Plan de Pruebas** — entregables, tareas, cronograma, responsables
7. **Requerimientos de Prueba** — entorno, herramientas, personal, datos
8. **Riesgos y Mitigaciones** — desde el diagnostico de la fase 2
9. **Aprobaciones** — responsable, fecha, firma

### Paso 3: Definir criterios de exito numericos

Convertir objetivos cualitativos a medibles. **Sin excepciones.**

| Criterio | Target por defecto | Medicion |
|---|---|---|
| Pass rate del smoke | 100% | tests passed / total |
| Duracion del smoke | ≤ 5 min | wall clock del stage |
| Flakiness de la suite | < 2% | tests que pasan en reintento / total |
| Cobertura de funcionalidades | ≥ 80% | automatizadas / candidatas |
| Cobertura de codigo | ≥ 70% | linhas / total |
| Selectores sin validar | 0 | grep de `TODO` en `pages/` |
| Datos hardcodeados | 0 | grep de literales en `scripts/` |
| Tests sin tags | 0 | cruce `--list` con filtros del pipeline |

Si el usuario define otros umbrales, **ganan los suyos**. Si no, usar estos y declararlos.

### Paso 4: Generar matriz de trazabilidad

```
Requisito -> Nivel de piramide -> Test ID -> Escenario -> Tags -> Prioridad
```

Cada escenario de la fase 3 debe aparecer. Escenario sin requisito o requisito sin escenario es un hallazgo.

### Paso 5: Guardar documento

En `automation-plans/{plan_id}/automation-test-plan.md`.

## Formato de salida

```json
{
  "status": "completed",
  "document_path": "automation-plans/{plan_id}/automation-test-plan.md",
  "sections_generated": ["string"],
  "success_criteria": {
    "smoke_pass_rate_pct": 100,
    "smoke_duration_minutes": 5,
    "max_flakiness_pct": 2,
    "min_feature_coverage_pct": 80,
    "min_code_coverage_pct": 70,
    "max_unvalidated_selectors": 0,
    "max_hardcoded_data": 0,
    "max_tests_without_tags": 0
  },
  "traceability_matrix": {
    "total_requirements": 0,
    "total_scenarios": 0,
    "scenarios_with_requirement": 0,
    "orphan_scenarios": 0,
    "coverage_pct": 100
  },
  "out_of_scope": ["string — funcionalidad excluida y motivo"],
  "awaiting_approval": true,
  "confidence": 0.0
}
```

## Reglas

- SIEMPRE generar documento en markdown.
- Los criterios de exito **DEBEN** ser numericos. "Rapido", "aceptable", "estable" no son criterios.
- La seccion **Funciones NO a Probar** es obligatoria. Una suite sin exclusiones declaradas promete mas de lo que entrega.
- Incluir matriz de trazabilidad completa.
- `orphan_scenarios > 0` → documentarlo como hallazgo, no ocultarlo.
- Marcar `awaiting_approval: true`. **No** pasar a la fase 5 sin aprobacion explicita del usuario.
- Seguir estructura IEEE-829 / ISTQB.

## Lectura bajo demanda

Este SKILL.md cubre la estructura IEEE-829 y los targets por defecto.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Targets por defecto y su justificacion | `.claude/skills/auto-tlc-suite-health/SKILL.md` |
| Template de caso de prueba individual | `docs/templates/tc_template.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: la estructura y los targets estan aca. No abras mas para emitir el plan formal.