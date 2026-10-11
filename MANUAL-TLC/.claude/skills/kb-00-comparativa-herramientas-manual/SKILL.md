---
name: kb-00-comparativa-herramientas-manual
description: Skill autónoma de conocimiento sobre comparativa de herramientas de soporte para pruebas manuales. No depende de archivos externos.
---

# Comparativa de Herramientas de Soporte para Pruebas Manuales

## Matriz de Decisión

| Criterio | Playwright MCP Server | Playwright CLI | Herramienta de gestión (TestRail / Zephyr / Xray) | Hoja de cálculo |
|----------|----------------------|----------------|--------------------------------------------------|-----------------|
| **Propósito** | Conducir navegador y capturar evidencia | Conducir navegador desde terminal | Gestionar casos, ciclos y trazabilidad | Registro informal |
| **Tipo de prueba ideal** | Todas (asistida paso a paso) | Regresión y smoke scriptados | Todas (organización) | Smoke puntual |
| **Snapshot de accesibilidad** | ✅ | ✅ | ❌ | ❌ |
| **Screenshot / video / traza** | ✅ | ✅ | ❌ | ❌ |
| **Diagnóstico de consola y red** | ✅ | ✅ | ❌ | ❌ |
| **Simulación offline / rutas mock** | ✅ | ✅ | ❌ | ❌ |
| **Estado persistente entre acciones** | ✅ | Parcial | N/A | N/A |
| **Integración con MCP** | ✅ | ❌ | Variable | ❌ |
| **Curva de aprendizaje** | Baja | Baja | Media | Muy baja |
| **Reporte** | Evidencia cruda + generado por el agente | Igual | Reportes y dashboards nativos | Manual |
| **Ideal para** | Sesiones manuales asistidas, exploratorias, UAT | Equipos con flujos muy repetitivos | Trazabilidad y auditoría | Pruebas ad-hoc |

## Recomendaciones por Escenario

### Sesión manual asistida (recomendado por defecto) → Playwright MCP Server
- Única herramienta soportada por MANUAL-TLC v1.0.
- Conduce un navegador real y captura evidencia utilizable como prueba.
- Permite al tester mantener el juicio humano mientras la herramienta ejecuta y registra.

### Regresión muy repetitiva → Playwright CLI
- Menor consumo de contexto que un cliente MCP.
- Útil cuando el mismo flujo se repite muchas veces y ya está estabilizado.

### Trazabilidad y auditoría → Herramienta de gestión + evidencia del MCP
- La herramienta de gestión guarda casos, ciclos y resultados.
- La evidencia (screenshots, trazas, video) queda en `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/` y se referencia desde el caso.

## Reglas de selección

1. Si el usuario no especifica herramienta, usar **Playwright MCP Server**.
2. Nunca proponer stack multi-herramienta por defecto.
3. La herramienta de gestión es complementaria: guarda el registro, no ejecuta las pruebas.
4. La evidencia siempre vive en el repositorio (`PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/`), no embebida en el gestor.
