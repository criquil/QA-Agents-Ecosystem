---
name: manual-test-strategy
description: Usa esta skill para diseñar la estrategia de pruebas manuales: tipos de prueba, matriz de cobertura, priorización y plan de ejecución.
---

# Manual Test Strategy

## Objetivo

Diseñar una estrategia completa de **pruebas manuales** que cubra los siete tipos soportados por MANUAL-TLC v1.0.

## Tipos de prueba cubiertos

| # | Tipo | Pregunta que responde |
|---|------|----------------------|
| 1 | **Pruebas Funcionales** | ¿Cada función hace lo que dice el requisito funcional? |
| 2 | **Pruebas de Sistema** | ¿El sistema completo, integrado, cumple los requisitos de sistema? |
| 3 | **Pruebas de Regresión** | ¿Lo que antes funcionaba sigue funcionando? |
| 4 | **Smoke Testing** | ¿El build es lo bastante estable para testearlo en serio? |
| 5 | **Sanity Testing** | ¿El fix puntual funciona y no rompió lo inmediato? |
| 6 | **Pruebas Exploratorias** | ¿Qué problemas hay que todavía no sabemos preguntar? |
| 7 | **Pruebas de Aceptación (UAT)** | ¿El negocio acepta el sistema tal como está? |

## Flujo

1. Identifica módulos, funcionalidades y flujos de negocio críticos.
2. Clasifica el alcance por tipo de prueba manual.
3. Define la matriz de cobertura: módulo/flujo × tipo de prueba.
4. Prioriza por riesgo, impacto al negocio y frecuencia de uso (P1/P2/P3).
5. Define la profundidad por tipo: smoke = cobertura superficial amplia, sanity = profunda y estrecha, funcional = exhaustiva por requisito, sistema = end-to-end, regresión = repetible y comparable, exploratoria = charter timeboxeado, UAT = criterios de negocio.
6. Genera el plan de ejecución con estimación de esfuerzo y dependencias de datos.

## Profundidad y amplitud por tipo

```
Smoke       : amplia y superficial   (¿abre? ¿responde? ¿navega?)
Sanity      : estrecha y profunda    (¿el fix hace lo que debía?)
Funcional   : exhaustiva por requisito
Sistema     : end-to-end a través de módulos y roles
Regresión   : amplia y determinista, sobre funcionalidad estable
Exploratoria: dirigida por charter, orientada a hallazgos
UAT         : guiada por escenarios de negocio y criterios de aceptación
```

## Salida Esperada

- Estrategia de testing con tipos seleccionados por módulo/flujo.
- Matriz de cobertura (módulo/flujo × tipo de prueba).
- Priorización P1/P2/P3 por riesgo y negocio.
- Plan de ejecución con estimación de esfuerzo.
- Riesgos que condicionan la estrategia (build, datos, entornos, accesos).

## Reglas

- El Smoke Testing es obligatorio en toda estrategia.
- Toda estrategia debe declarar el entorno, el navegador objetivo y el catálogo de cuentas.
- Las Pruebas de Regresión sólo aplican sobre funcionalidad previamente validada.
- UAT siempre es ejecutada o firmada por un usuario de negocio.
