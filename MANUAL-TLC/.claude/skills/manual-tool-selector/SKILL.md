---
name: manual-tool-selector
description: Usa esta skill cuando necesites elegir la herramienta de soporte para un caso de pruebas manuales. Aplica criterios de tipo de prueba manual, navegador objetivo, capacidad de evidencia, entorno y curva de aprendizaje.
---

# Manual Tool Selector

## Objetivo

Elegir la herramienta de soporte adecuada para conducir y evidenciar un ciclo de **pruebas manuales** y justificar la decisión con criterios técnicos.

## Herramienta por defecto

**Playwright MCP Server** — es la herramienta única y por defecto de MANUAL-TLC v1.0.

Razones técnicas:

- Conduce un **navegador real** y permite ejecutar pasos manuales sobre la UI tal como los vería un usuario.
- Usa el **árbol de accesibilidad** (`browser_snapshot`) para localizar elementos, lo que da determinismo al paso a paso sin depender de coordenadas.
- Captura **evidencia de calidad**: `browser_take_screenshot`, `browser_start_video`, `browser_start_tracing`, `browser_pdf_save`.
- Permite **diagnóstico humano**: `browser_console_messages`, `browser_network_requests`.
- Soporta **manipulación de estado de red** (offline, rutas mockeadas) útil para pruebas exploratorias y de validación de mensajes de error.
- Soporta múltiples navegadores (Chromium, Firefox, WebKit, Edge) para cubrir la matriz de compatibilidad.
- Si no está disponible el MCP, puede usarse el **Playwright CLI** como alternativa de conducción.

## Flujo

1. Identifica el objetivo principal: funcional, sistema, regresión, smoke, sanity, exploratoria o UAT.
2. Confirma el navegador objetivo y si se requiere emulación responsive.
3. Confirma el tipo de evidencia exigida (screenshot, video, traza, PDF, consola, red).
4. Evalúa restricciones: entorno accesible, credenciales, MFA/captcha, políticas de automatización.
5. Compara opciones con una matriz corta (pros, contras, riesgos).
6. Devuelve recomendación final, alternativa de respaldo y rationale.

## Matriz de decisión (orientativa)

| Criterio | Playwright MCP Server | Playwright CLI | Otra herramienta explícita |
|----------|----------------------|----------------|----------------------------|
| Conducción de navegador real | ✅ | ✅ | Variable |
| Snapshot de accesibilidad | ✅ | ✅ | — |
| Evidencia visual/video/traza | ✅ | ✅ | Variable |
| Simulación de red offline | ✅ | ✅ | Poco común |
| Integración en cliente MCP | ✅ | ❌ | Variable |
| Estado persistente entre acciones | ✅ | Parcial | — |
| Costo de tokens | Medio | Bajo | Variable |

## Salida Esperada

- Herramienta recomendada (por defecto: Playwright MCP Server).
- Razones técnicas en bullets.
- Riesgos de implementación.
- Configuración mínima requerida (servidor MCP, navegador, directorio de evidencia).

## Reglas

- Si el usuario no especifica herramienta, usar **Playwright MCP Server** sin preguntar.
- Sólo se acepta una herramienta distinta si el usuario la solicita de forma explícita.
- Nunca proponer un stack multi-herramienta por defecto.
