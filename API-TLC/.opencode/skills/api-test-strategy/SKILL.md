---
name: api-test-strategy
description: Usa esta skill para diseñar la estrategia de pruebas de API: tipos de prueba, coverage matrix, priorización y plan de ejecución.
---

# API Test Strategy

## Objetivo
Diseñar una estrategia completa de pruebas de API que cubra functional, integration, contract y negative testing.

## Flujo
1. Identifica endpoints críticos y flujos de negocio.
2. Clasifica por tipo: functional, integration, contract, negative, boundary, security.
3. Define matrix de cobertura: endpoint × tipo de prueba.
4. Prioriza por riesgo y impacto al negocio.
5. Genera plan de ejecución con estimación de tiempo.

## Orden de ejecución por defecto

1. Smoke test → 2. Functional → 3. Contract → 4. Integration → 5. Negative → 6. Boundary → 7. Security

## Salida Esperada
- Estrategia de testing con tipos seleccionados por endpoint.
- Coverage matrix (endpoint × tipo de prueba).
- Priorización P1/P2/P3 por riesgo y negocio.
- Plan de ejecución con estimación de esfuerzo.
