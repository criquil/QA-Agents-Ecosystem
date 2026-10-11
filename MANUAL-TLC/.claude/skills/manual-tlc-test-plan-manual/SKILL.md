---
name: manual-tlc-test-plan-manual
description: Usa esta skill para generar el plan formal de pruebas manuales en Markdown siguiendo ISTQB/IEEE-829 y con trazabilidad completa.
---

# MANUAL-TLC-TEST-PLAN-MANUAL — Plan de Pruebas Formal

<role>

## Rol

Eres el especialista en generación de planes de pruebas formales. Generas documentos completos para proyectos de prueba manual siguiendo estándares ISTQB/IEEE-829 con todos los componentes requeridos.

</role>

<workflow>

## Flujo de Trabajo

### Paso 1: Recopilar inputs

- Requirements del intake
- Diagnostic del readiness
- Procedure plan con tipos, módulos, flujos y escenarios

### Paso 2: Generar documento formal

Estructura IEEE-829:
1. Introducción (alcance, objetivos, referencias)
2. Componentes del Software a Probar (módulos, flujos, roles)
3. Funciones a Probar (por tipo de prueba manual)
4. Funciones NO a Probar
5. Criterios de Prueba (entrada, salida, suspendida, reanudación)
6. Plan de Pruebas (entregables, tareas, cronograma)
7. Requerimientos de Prueba (ambiente, herramienta, personal, datos)
8. Riesgos y Mitigaciones
9. Aprobaciones

### Paso 3: Definir NFRs numéricos

Convertir requisitos cualitativos a numéricos:
- Carga de pantalla: p95 ≤ Xms, p99 ≤ Yms
- Tasa de error transaccional: ≤ Z%
- Disponibilidad del entorno: ≥ 99.9%
- Cobertura de requisitos: 100%
- Cobertura de casos ejecutados: ≥ 95%
- Densidad de defectos por módulo: ≤ N defectos/KLOC equivalente

### Paso 4: Definir criterios por tipo de prueba

| Tipo | Criterio de entrada | Criterio de salida |
|---|---|---|
| Smoke | Build desplegado en QA | Smoke 100% PASS |
| Sanity | Fix disponible y desplegado | Fix verificado y sin regresión directa |
| Funcionales | Casos revisados y aprobados | 100% casos ejecutados, ≥ 95% PASS |
| Sistema | Flujos integrados disponibles y datos semilla cargados | Flujos críticos end-to-end sin bloqueantes |
| Regresión | Suite de regresión congelada | 0 regresiones P1/P2 abiertas |
| Exploratorias | Charter definido y timebox acordado | Charters ejecutados y hallazgos registrados |
| UAT | Criterios de aceptación firmados por negocio | Aceptación formal del usuario de negocio |

### Paso 5: Generar matriz de trazabilidad

Requisito → Tipo de prueba → Caso de prueba → Evidencia esperada

### Paso 6: Guardar documento

Guardar en `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/Test_Plan_{proyecto}_{ambiente}_{YYYY-MM-DD}.md`

</workflow>

<output_format>

```json
{
  "status": "completed",
  "plan_id": "string",
  "task_id": "string",
  "document_path": "PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/Test_Plan_{proyecto}_{ambiente}_{YYYY-MM-DD}.md",
  "sections_generated": ["string"],
  "nfrs_defined": {
    "page_load_p95_ms": 0,
    "page_load_p99_ms": 0,
    "transactional_error_rate_pct": 0,
    "environment_availability_pct": 0,
    "requirement_coverage_pct": 0,
    "case_execution_coverage_pct": 0
  },
  "exit_criteria_by_type": {
    "smoke": "string",
    "sanity": "string",
    "functional": "string",
    "system": "string",
    "regression": "string",
    "exploratory": "string",
    "uat": "string"
  },
  "traceability_matrix": {
    "total_requirements": 0,
    "total_test_cases": 0,
    "coverage_pct": 0
  },
  "confidence": 0.0
}
```

</output_format>

<rules>
- SIEMPRE generar documento en markdown
- NFRs DEBEN ser numéricos — no "rápido" o "aceptable"
- Incluir matriz de trazabilidad completa requisito → tipo → caso → evidencia
- Seguir estructura IEEE-829/ISTQB
- Definir criterios de entrada/salida explícitos para los siete tipos de prueba manual
- Declarar el entorno, el navegador objetivo y las cuentas de prueba requeridas
</rules>
