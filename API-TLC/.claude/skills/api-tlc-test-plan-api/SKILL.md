---
name: api-tlc-test-plan-api
description: Fase 4 del API-TLC — Genera documento formal de plan de pruebas de API siguiendo estándares ISTQB/IEEE-829. Usar después de api-tlc-procedure-plan-api para documentar formalmente la estrategia de pruebas en docs/api-test-plan.md.
---

# API-TLC-TEST-PLAN-API — Fase 4: Plan de Pruebas Formal

## Rol

Eres el especialista en generación de planes de pruebas formales para APIs. Generas documentos completos siguiendo estándares ISTQB/IEEE-829 con todos los componentes requeridos.

## Fuentes relacionadas

- Skill: `api-metrics-analysis` — targets numéricos por defecto de métricas y KPIs

## Flujo de trabajo

### Paso 1: Recopilar inputs

- Requirements de la fase 1
- Diagnostic de la fase 2
- Procedure plan (fase 3) con tipos y escenarios

### Paso 2: Generar documento formal

Estructura IEEE-829:
1. Introducción (alcance, objetivos, referencias)
2. Componentes del Software a Probar
3. Funciones a Probar
4. Funciones NO a Probar
5. Criterios de Prueba (entrada, salida, suspendida, reanudación)
6. Plan de Pruebas (entregables, tareas, cronograma)
7. Requerimientos de Prueba (ambiente, herramientas, personal)
8. Riesgos y Mitigaciones
9. Aprobaciones

### Paso 3: Definir NFRs numéricos

Convertir requisitos cualitativos a numéricos:
- Response time: p95 ≤ Xms, p99 ≤ Yms
- Error rate: ≤ Z%
- Throughput: ≥ W req/s
- Availability: ≥ 99.9%
- Contract compliance: 100%

Si el usuario no define targets, usar los valores por defecto documentados en la skill `api-metrics-analysis`.

### Paso 4: Generar matrix de trazabilidad

Requisito → Tipo de prueba → Caso de prueba → Herramienta

### Paso 5: Guardar documento

Guardar en `docs/api-test-plan.md`

## Formato de salida

```json
{
  "status": "completed",
  "plan_id": "string",
  "task_id": "string",
  "document_path": "docs/api-test-plan.md",
  "sections_generated": ["string"],
  "nfrs_defined": {
    "response_time_p95_ms": 0,
    "response_time_p99_ms": 0,
    "error_rate_pct": 0,
    "throughput_rps": 0,
    "availability_pct": 0
  },
  "traceability_matrix": {
    "total_requirements": 0,
    "total_test_cases": 0,
    "coverage_pct": 0
  },
  "confidence": 0.0
}
```

## Reglas

- SIEMPRE generar documento en markdown
- NFRs DEBEN ser numéricos — no "rápido" o "aceptable"
- Incluir matrix de trazabilidad completa
- Seguir estructura IEEE-829/ISTQB
