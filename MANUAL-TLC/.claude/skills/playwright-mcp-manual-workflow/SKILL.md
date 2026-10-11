---
name: playwright-mcp-manual-workflow
description: Usa esta skill para conducir una sesión de prueba manual con el Playwright MCP Server, incluyendo navegación, interacción, snapshots de accesibilidad, captura de evidencia y diagnóstico.
---

# Playwright MCP Manual Workflow

## Objetivo

Conducir una sesión de **prueba manual asistida** sobre una aplicación web usando el Playwright MCP Server como único soporte de navegador y evidencia.

## Configuración del servidor

En `.claude/settings.json`:

```json
{
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "-y", "@playwright/mcp@latest"],
      "enabled": true
    }
  }
}
```

Requisitos: Node.js 18 o superior y el navegador objetivo instalado.

## Flujo

1. **Definir el alcance de la sesión**: módulo, caso(s) de prueba, rol, entorno y URL base.
2. **Abrir el navegador**: `browser_navigate` a la URL base del entorno confirmado.
3. **Confirmar el render**: `browser_snapshot` y validar título, menú y versión desplegada.
4. **Ajustar la ventana** si la matriz exige una resolución específica: `browser_resize`.
5. **Iniciar la evidencia de sesión** cuando aplique: `browser_start_video` y/o `browser_start_tracing`.
6. **Ejecutar el caso paso a paso** usando `browser_snapshot` (o `browser_find` para búsquedas puntuales) antes de cada interacción para localizar el elemento correcto. Para escribir o corregir un XPath, seguir `manual-selector-strategy`.
7. **Capturar evidencia por paso crítico**: `browser_take_screenshot`.
8. **Diagnosticar ante fallo**: `browser_console_messages` y `browser_network_requests`.
9. **Cerrar la evidencia**: `browser_stop_tracing` / `browser_stop_video`.
10. **Cerrar el navegador**: `browser_close`.

## Herramientas disponibles

| Categoría | Herramientas |
|---|---|
| Navegación | `browser_navigate`, `browser_navigate_back` |
| Inspección | `browser_snapshot` |
| Interacción | `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_press_key`, `browser_hover`, `browser_drag`, `browser_file_upload`, `browser_handle_dialog` |
| Espera | `browser_wait_for` |
| Evidencia | `browser_take_screenshot`, `browser_pdf_save` |
| Diagnóstico | `browser_console_messages`, `browser_network_requests`, `browser_evaluate` |
| Sesión | `browser_tabs`, `browser_resize`, `browser_close`, `browser_install` |
| Grabación | `browser_start_tracing`, `browser_stop_tracing`, `browser_start_video`, `browser_stop_video` |
| Simulación | `browser_network_state_set`, `browser_route` |

## Patrones útiles

### Login y preparación de rol
```
browser_navigate -> URL de login
browser_snapshot -> localizar campos
browser_fill_form -> usuario y contraseña
browser_click -> botón iniciar sesión
browser_wait_for -> texto del dashboard
browser_take_screenshot -> evidencia de sesión iniciada
```

### Validación de formularios
Ejecutar cada campo con datos límite, capturar el mensaje de validación y contrastarlo con el requisito. Un mensaje genérico ("error inesperado") cuando el requisito pide un mensaje específico es un defecto de usabilidad/validación.

### Verificación de persistencia
Tras guardar, recargar la página, cerrar sesión y volver a entrar, y comprobar que el dato persiste con el valor y el formato correctos.

### Pruebas offline y de error
Usar `browser_network_state_set` con `offline` para validar mensajes de "sin conexión" y `browser_route` para forzar respuestas de error controladas en pruebas exploratorias.

## Guardado de evidencia

- Los archivos se resuelven contra la raíz del workspace cuando se indica un nombre relativo.
- Convención: `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/{CASE-ID}/{CASE-ID}-{paso}-{timestamp}.png`
- Si no se especifica nombre, la herramienta guarda en su directorio de salida con nombre autogenerado.

## Reglas

- Siempre `browser_snapshot` (o `browser_find` para un nodo puntual) antes de interactuar: evita clics a ciegas y snapshots obsoletos.
- Todo XPath se define y valida con `manual-selector-strategy`, dentro de esta misma sesión. Nunca usar Chrome DevTools MCP.
- Nunca ejecutar dos sesiones simultáneas sobre el mismo navegador.
- Confirmar el entorno objetivo con el usuario antes de la primera navegación.
- No operar sobre producción sin autorización explícita y sólo en modo lectura.
- Cerrar siempre la sesión (`browser_close`) al terminar el caso o la suite.
- Si un elemento no aparece tras `browser_wait_for`, registrar BLOCKED y no forzar el paso.
