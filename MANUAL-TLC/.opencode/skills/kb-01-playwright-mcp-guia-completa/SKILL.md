---
name: kb-01-playwright-mcp-guia-completa
description: Skill autónoma de conocimiento sobre Playwright MCP Server - guía completa para sesiones de prueba manual. No depende de archivos externos.
---

# Playwright MCP Server - Guía Completa para Pruebas Manuales

## ¿Qué es?

Servidor Model Context Protocol que expone las capacidades de Playwright (automatización de navegador) como herramientas que un agente puede invocar paso a paso. La interacción con la página se realiza mediante **snapshots del árbol de accesibilidad**, no mediante visión por píxeles, lo que la hace determinista y útil para sesiones de prueba manual asistida.

## Instalación y configuración

### Requisitos
- Node.js 18 o superior
- Un cliente MCP (OpenCode, VS Code, Claude Desktop, Cursor, ...)
- El navegador objetivo instalado

### Configuración en OpenCode (`opencode.json`)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@playwright/mcp@latest"],
      "enabled": true
    }
  }
}
```

Los nombres de las herramientas quedan prefijados con el nombre del servidor (`playwright`).

### Instalación de navegadores

Si el navegador no está disponible, usar `browser_install` o instalar Chromium con Playwright. Para emular dispositivos, Playwright usa perfiles de dispositivo y dimensiones de viewport (`browser_resize`).

## Herramientas principales

| Categoría | Herramientas |
|---|---|
| Navegación | `browser_navigate`, `browser_navigate_back` |
| Inspección | `browser_snapshot`, `browser_find` |
| Interacción con elementos | `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_check`, `browser_uncheck`, `browser_press_key`, `browser_hover`, `browser_drag`, `browser_file_upload`, `browser_handle_dialog` |
| Espera y sincronización | `browser_wait_for` |
| Evidencia | `browser_take_screenshot`, `browser_pdf_save` |
| Diagnóstico | `browser_console_messages`, `browser_network_requests`, `browser_evaluate` |
| Gestión de sesión | `browser_tabs`, `browser_resize`, `browser_close`, `browser_install` |
| Grabación y trazado | `browser_start_tracing`, `browser_stop_tracing`, `browser_start_video`, `browser_stop_video` |
| Demostración y resaltado | `browser_start_recording`, `browser_stop_recording`, `browser_highlight`, `browser_hide_highlight` |
| Simulación de red | `browser_network_state_set`, `browser_route` |

> Algunas capacidades están disponibles de forma opt-in mediante el flag `--caps` del servidor (por ejemplo `config`, `network`). Las herramientas de verificación y de generación de pruebas también son capacidades opcionales; verificar `browser_get_config` para conocer la configuración efectiva de la sesión.

## Parámetros clave

- **`target`**: referencia exacta del elemento obtenida del `browser_snapshot`. Es la forma recomendada de referenciar elementos.
- **`element`**: descripción legible del elemento, usada para confirmar la interacción correcta.
- **`browser_take_screenshot`**: acepta `filename` (relativo a la raíz del workspace), `fullPage` (página completa) y `scale` (`css` o `device`).
- **`browser_start_video`**: acepta `filename`, `size` y `fps`; por defecto guarda `video-{timestamp}.webm` en el directorio de salida.
- **`browser_wait_for`**: acepta `time` (segundos), `text` (esperar que aparezca) y `textGone` (esperar que desaparezca).

## Guardado de artefactos

- Los nombres de archivo relativos se resuelven contra la raíz del workspace.
- Si no se indica nombre, la captura se guarda en el directorio de salida con nombre autogenerado (`page-{timestamp}.png`, `video-{timestamp}.webm`).
- Convención MANUAL-TLC: `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/{CASE-ID}/{CASE-ID}-{descriptor}-{timestamp}.{ext}`

## Patrones de uso para pruebas manuales

### Apertura de sesión

```
browser_navigate      -> https://<entorno>/login
browser_snapshot      -> inventario de elementos interactuables
browser_fill_form     -> usuario y contraseña
browser_click         -> botón de ingreso
browser_wait_for      -> texto del dashboard
browser_take_screenshot -> evidencia de sesión iniciada
browser_start_video   -> grabar la sesión (flujos largos / UAT)
```

### Ejecución de un paso
1. `browser_snapshot` para localizar el elemento por su referencia.
2. Ejecutar la acción (`browser_click`, `browser_type`, `browser_select_option`, ...).
3. `browser_wait_for` el texto o estado esperado.
4. `browser_take_screenshot` del resultado observado.

### Validación de formularios
Recorrer campo por campo con datos inválidos, vacíos y límite; capturar el mensaje mostrado y contrastarlo con el requisito. Un mensaje genérico donde el requisito exige uno específico es un defecto.

### Verificación de persistencia
Guardar → recargar (`browser_navigate` a la misma URL) → cerrar sesión → volver a entrar → comprobar el dato con su valor y formato.

### Diagnóstico de un fallo
```
browser_console_messages   -> errores de JavaScript
browser_network_requests   -> 4xx/5xx, latencias, duplicados
browser_evaluate           -> lectura puntual del DOM o de variables de la página
browser_take_screenshot    -> evidencia del estado fallido
```

### Cierre de sesión
```
browser_stop_tracing / browser_stop_video -> cerrar artefactos
browser_close                             -> cerrar el navegador
```

## Buenas prácticas

1. **Snapshot antes de interactuar**: evita clics a ciegas y referencias obsoletas. Usar `browser_find` para localizar un nodo puntual sin volcar todo el árbol.
2. **XPath validado**: los selectores que se escriben o documentan se definen con `manual-selector-strategy` y se validan dentro de la sesión (`browser_evaluate` → 1 coincidencia). Nunca Chrome DevTools MCP.
3. **Una acción por paso**: facilita aislar el origen de un defecto.
4. **Evidencia inmediata**: capturar en el momento del hallazgo, no al final.
5. **Esperas explícitas**: usar `browser_wait_for` en lugar de esperas ciegas por tiempo.
6. **Sesión única**: no intercalar dos sesiones sobre el mismo navegador.
7. **Cerrar siempre**: dejar el navegador cerrado al terminar para evitar sesiones huérfanas.
8. **Registrar el contexto**: entorno, build, navegador, resolución y rol van en el caso, no en la memoria del tester.

## Limitaciones y consideraciones

- **Consumo de contexto**: los snapshots del árbol de accesibilidad son verbosos; conviene trabajar pantalla por pantalla.
- **MFA, captcha y OTP**: pueden requerir intervención manual del tester durante la sesión.
- **Elementos no accesibles**: componentes sin semántica de accesibilidad (canvas, divs clicables sin rol) pueden necesitar selectores CSS explícitos.
- **Sesiones largas**: conviene cerrar y reabrir el navegador entre suites para evitar acumulación de estado.
- **Datos productivos**: la herramienta no distingue entornos; la prohibición de operar sobre producción es responsabilidad del flujo, no de la herramienta.

## Referencia

- Repositorio: `microsoft/playwright-mcp`
- Documentación de Playwright: `playwright.dev`
