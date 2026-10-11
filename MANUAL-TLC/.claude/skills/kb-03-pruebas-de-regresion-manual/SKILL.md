---
name: kb-03-pruebas-de-regresion-manual
description: Skill autónoma de conocimiento sobre pruebas de regresión manuales: selección de suite, comparación con baseline y gestión de regresiones. No depende de archivos externos.
---

# Pruebas de Regresión Manuales

## Definición

Ejecución manual repetida de un conjunto de casos previamente validados para confirmar que los cambios recientes no introdujeron defectos en funcionalidad que ya funcionaba.

Una **regresión** es un defecto en funcionalidad que antes funcionaba correctamente.

## Disparadores del ciclo

- Nuevo build desplegado en el entorno de pruebas.
- Hotfix o parche urgente.
- Cambio de configuración o de parámetros del sistema.
- Migración o actualización de datos.
- Actualización de una dependencia o de un servicio externo.
- Cambio en un módulo compartido (autenticación, permisos, facturación).

## Selección de la suite

| Riesgo del cambio | Suite a ejecutar |
|---|---|
| Transversal (auth, permisos, datos, arquitectura) | Regresión completa |
| Localizado en un módulo | Regresión parcial: módulo + dependencias directas |
| Menor y de bajo impacto | Regresión mínima: sólo flujos P1 |
| Fix de un defecto puntual | Sanity primero, luego regresión del módulo |

## Composición de la suite de regresión

1. **Flujos P1** — 100% obligatorios, siempre.
2. **Casos ligados a defectos corregidos** — histórico de fragilidad.
3. **Funcionalidad más usada por el negocio** — por frecuencia real.
4. **Funcionalidad con más defectos históricos** — por densidad de defectos.
5. **Integraciones externas** — por dependencia.
6. **Flujos multi-rol** — autorización y visibilidad.

## Ejecución y comparación con el baseline

Para que el resultado sea comparable, deben mantenerse constantes:

- El mismo **caso** (y su versión).
- Los mismos **datos** de entrada.
- El mismo **rol** de usuario.
- El mismo **navegador** y resolución.
- El mismo **orden** de pasos.

```
Caso            : TC-REG-008
Baseline        : ciclo 2026-08-15, build 4.2.1 -> PASS (evidencia: TC-REG-008-*.png)
Ciclo actual    : ciclo 2026-09-20, build 4.3.0 -> FAIL
Resultado obs.  : el total no refleja el descuento
Clasificación   : REGRESIÓN (antes pasaba)
Severidad       : HIGH  ->  DEF-0341
```

## Clasificación de resultados

| Resultado | Significado |
|---|---|
| PASS | Comportamiento idéntico al baseline |
| FAIL – Regresión | Antes pasaba, ahora falla |
| FAIL – Nunca pasó | El caso nunca fue válido o el requisito cambió |
| BLOCKED | No se pudo ejecutar (entorno, datos, sesión MCP) |
| SKIPPED | Fuera del alcance del ciclo, documentado el motivo |

## Uso del Playwright MCP en regresión

- Repetir exactamente la secuencia de acciones del baseline.
- Capturar el screenshot en el mismo punto del flujo que en el baseline para comparación visual.
- Revisar `browser_console_messages` y `browser_network_requests` para detectar errores nuevos que el baseline no mostraba.
- Registrar el build visible en la UI como prueba de que se ejecutó el artefacto correcto.

## Métricas

| Métrica | Fórmula | Target |
|---|---|---|
| Regression Pass Rate | casos_pass / casos_ejecutados | ≥ 95% |
| Regression Escape | regresiones_detectadas_en_producción / total_regresiones | ≤ 5% |
| Suite Stability | casos_con_resultado_consistente / total | ≥ 95% |
| Automation Candidate Rate | casos_candidatos_a_automatizar / total | informativo |

## Best Practices

1. Suite congelada y versionada antes del ciclo.
2. Sin datos ni roles idénticos al baseline, la comparación no tiene valor.
3. Smoke aprobado es la condición de entrada a la regresión.
4. Un BLOCKED no se cuenta como PASS.
5. Toda regresión detectada debe generar un caso nuevo o reforzado en la suite.
6. Revisar periódicamente la suite: casos que nunca fallan y ya no aportan deben evaluarse para retiro.
7. Priorizar por riesgo, no por comodidad: es mejor cubrir pocos flujos críticos a fondo que muchos superficialmente.
