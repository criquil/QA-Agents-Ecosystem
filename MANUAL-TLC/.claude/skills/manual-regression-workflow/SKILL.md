---
name: manual-regression-workflow
description: Usa esta skill para planificar y ejecutar ciclos de regresión manual, incluyendo selección de la suite, gates de smoke y sanity, y comparación de resultados contra el baseline.
---

# Manual Regression Workflow

## Objetivo

Planificar y ejecutar **ciclos de regresión manual** que confirmen que los cambios no rompieron funcionalidad previamente validada, usando smoke y sanity como gates de entrada.

## Flujo

1. **Confirmar el disparador del ciclo**: nuevo build, hotfix, cambio de configuración, migración de datos o despliegue de una dependencia.
2. **Ejecutar el gate de Smoke Testing** — si falla, no se ejecuta la regresión y se devuelve el build.
3. **Ejecutar el gate de Sanity Testing** sobre el cambio que disparó el ciclo.
4. **Seleccionar la suite de regresión** según el riesgo del cambio:
   - **Regresión completa**: cambio transversal, arquitectura, autenticación o datos.
   - **Regresión parcial (riesgo dirigido)**: cambio localizado; se corre el módulo afectado más sus dependencias.
   - **Regresión mínima**: cambio menor y de bajo riesgo; sólo flujos P1.
5. **Ejecutar la suite** en el orden congelado por la suite de regresión.
6. **Comparar contra el baseline**: mismo caso, mismo dato, mismo navegador, mismo rol.
7. **Registrar** PASS/FAIL y toda diferencia contra el resultado anterior.
8. **Cerrar el ciclo** con el resumen de regresiones y su impacto.

## Smoke vs Sanity en el ciclo

| | Smoke | Sanity |
|---|---|---|
| Alcance | Amplio y superficial | Estrecho y profundo |
| Momento | Al recibir el build | Después del smoke, sobre el cambio |
| Objetivo | ¿Es testeable? | ¿El fix funciona y no rompió lo inmediato? |
| Resultado | Go / No-Go para la regresión | Confirma o rechaza el cambio puntual |

## Reglas de oro

- Un mismo caso debe ejecutarse con los mismos datos y el mismo rol que en el baseline; si cambian, el resultado no es comparable.
- Nunca "optimizar" un paso de un caso de regresión sin versionar el cambio del caso.
- Todo FAIL se compara contra el estado anterior: si antes pasaba, es una **regresión** y se marca como tal.
- Un caso BLOCKED se registra como BLOCKED y se escala; no se cuenta como PASS.
- La suite de regresión debe estar congelada antes de iniciar el ciclo.

## Uso del Playwright MCP

- Ejecutar cada caso con la misma secuencia de acciones del baseline.
- Usar `browser_take_screenshot` en el mismo punto del flujo anterior para permitir comparación visual.
- Usar `browser_console_messages` y `browser_network_requests` para detectar errores nuevos que el baseline no mostraba.
- Registrar el build/versión visible en la UI como evidencia de que se probó el artefacto correcto.

## Salida Esperada

- Alcance del ciclo de regresión y su justificación por riesgo.
- Resultado del gate de smoke y de sanity.
- Resultado por caso, comparado contra el baseline.
- Lista de regresiones con severidad, impacto y evidencia.
- Recomendación de Go / No-Go para el release.

## Reglas

- Sin smoke aprobado no hay regresión.
- Toda regresión debe indicar el caso, el build anterior y el build actual.
- La regresión no se declara satisfactoria si hay defectos P1 abiertos.
