---
name: kb-01-sesiones-asistidas-mcp
description: Skill autónoma de conocimiento sobre sesiones de prueba manual asistidas por MCP: patrones, registro paso a paso, manejo de errores y criterio del tester.
---

# Sesiones de Prueba Manual Asistidas por MCP

## Concepto

Una **sesión asistida** es una ejecución de prueba manual en la que el tester conserva el criterio y la decisión (¿esto es correcto? ¿esto es un defecto?), mientras el agente conduce el navegador y registra la evidencia mediante las herramientas del Playwright MCP Server.

No es automatización de pruebas: no hay assertions automáticas ni suites desatendidas. Es **ejecución manual con conducción y evidencia asistidas**.

## Anatomía de una sesión

```
1. Preparación    -> entorno, build, rol, datos, evidencia de sesión iniciada
2. Paso a paso    -> snapshot -> acción -> espera -> screenshot -> veredicto
3. Diagnóstico    -> consola, red, DOM ante cualquier anomalía
4. Registro       -> PASS/FAIL/BLOCKED + notas + evidencia por paso
5. Cierre         -> detener grabaciones, cerrar navegador, resumen de sesión
```

## Patrón de ejecución paso a paso

Para cada paso del caso de prueba:

| Fase | Acción | Herramienta |
|---|---|---|
| 1 | Localizar el elemento | `browser_snapshot` / `browser_find` |
| 2 | Ejecutar la acción | `browser_click` / `browser_type` / `browser_fill_form` / `browser_select_option` / `browser_press_key` |
| 3 | Sincronizar | `browser_wait_for` (texto o estado esperado) |
| 4 | Observar y decidir | Juicio del tester contra el resultado esperado |
| 5 | Evidenciar | `browser_take_screenshot` |
| 6 | Registrar | PASS / FAIL / BLOCKED + nota |

## Registro paso a paso (plantilla de ejecución)

```
TC-<ID>  Paso 3
Acción        : clic en "Confirmar pedido"
Resultado esp.: se muestra el resumen con total y número de pedido
Resultado obs.: se muestra el resumen; el total queda en 0,00
Veredicto     : FAIL
Evidencia     : evidence/checkout/TC-FUNC-012-paso3-20260921T1042.png
Notas         : la consola muestra 500 en POST /orders/total
```

## Manejo de errores durante la sesión

| Situación | Acción |
|---|---|
| Elemento no encontrado tras la espera | Registrar BLOCKED, capturar pantalla y consola, no forzar el paso |
| Error de JavaScript en consola | Registrar como hallazgo, aunque el caso pase |
| Respuesta 4xx/5xx en red | Registrar como hallazgo con la petición y la respuesta |
| Sesión expirada a mitad del caso | Reiniciar sesión, registrar el evento y continuar desde el paso previo |
| El entorno no responde | Detener la sesión, escalar como riesgo de entorno y no reportar BLOCKED como defecto de producto |
| El dato semilla no existe | Detener el caso, recrear el dato y documentar el incidente |

## Localización de elementos

La localización de elementos sigue la skill `manual-selector-strategy`:

- El elemento se identifica primero en el árbol de accesibilidad (`browser_snapshot`, o `browser_find` para un nodo puntual).
- Cuando el selector debe documentarse, reutilizarse o el snapshot es ambiguo, se escribe un **XPath** con la jerarquía `id` → `name` → `data-*` → ARIA → texto → `class` → complejo.
- El XPath se entrega a los comandos en el parámetro `target` con el prefijo `xpath=`.
- **Todo selector se valida dentro de esta misma sesión**: `browser_evaluate` debe devolver **1** coincidencia, y luego se confirma funcionalmente ejecutando la acción real.
- **Prohibido Chrome DevTools MCP**: la localización y la validación ocurren exclusivamente con el Playwright MCP Server.

## Criterio del tester: qué NO delegar a la herramienta

- Decidir si un texto, un formato o un mensaje es aceptable.
- Evaluar usabilidad, claridad y coherencia visual.
- Determinar la severidad y el impacto de negocio del defecto.
- Interpretar ambigüedades del requisito.
- Decidir la variación exploratoria del siguiente paso.

## Métricas de la sesión

- Pasos ejecutados vs planificados.
- Hallazgos por hora de sesión.
- Proporción de evidencia por paso crítico (debe ser 100%).
- Casos BLOCKED atribuidos a entorno vs a producto.

## Reglas

1. Sin confirmación del entorno y del rol no se inicia la sesión.
2. Cada paso crítico deja evidencia; los pasos triviales no la requieren.
3. Un BLOCKED por causa de entorno no es un defecto de producto: se clasifica y se escala aparte.
4. La sesión termina siempre con el navegador cerrado y las grabaciones detenidas.
5. Si el criterio del tester y el resultado de la herramienta se contradicen, prevalece el criterio del tester con la evidencia adjunta.
