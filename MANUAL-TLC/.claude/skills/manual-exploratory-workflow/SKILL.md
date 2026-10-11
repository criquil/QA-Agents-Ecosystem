---
name: manual-exploratory-workflow
description: Usa esta skill para diseñar y ejecutar sesiones de pruebas exploratorias manuales con charters, timeboxes y reporte basado en sesiones (SBTM).
---

# Manual Exploratory Workflow

## Objetivo

Diseñar y ejecutar **pruebas exploratorias manuales** — aprendizaje, diseño y ejecución simultáneos — obteniendo hallazgos accionables y trazables.

## Cuándo usarlo

- Módulos nuevos o recién integrados.
- Áreas de alto riesgo con requisitos incompletos o ambiguos.
- Después de un cambio grande que invalida los casos existentes.
- Como complemento del ciclo formal, para descubrir lo que los casos no cubren.

## Flujo

1. **Definir charters** con la plantilla: *Explorar [área] con [recursos] para descubrir [información/riesgo]*.
2. **Estimar y timeboxear** cada charter (ej. 60 o 90 minutos).
3. **Preparar el entorno**: build, cuentas, datos semilla y herramientas (Playwright MCP).
4. **Ejecutar la sesión** registrando en vivo: tiempo, cobertura, notas, defectos y preguntas.
5. **Variar heurísticas** durante la sesión para no quedarse en el happy path.
6. **Cerrar la sesión** con el reporte SBTM.
7. **Triar hallazgos** y convertirlos en defectos o en nuevos casos de prueba formales, construidos SIEMPRE desde las plantillas obligatorias de `templates/` (`tc_template.md` para casos, `bdd_template.md` para escenarios Gherkin).

## Plantilla de Charter

```
CHARTER: EXPLORAR <área>
CON <recursos: rol, datos, navegador>
PARA DESCUBRIR <riesgo o información buscada>
TIMEBOX: <minutos>
```

## Heurísticas recomendadas

- **SFDPOT** (Structure, Function, Data, Platform, Operations, Time)
- **CRUD** por entidad
- **Fronteras y límites**: vacío, uno, máximo, máximo+1
- **Interrupciones**: recargar, volver atrás, cerrar pestaña, sesión expirada, doble submit
- **Estados**: vacío, cargando, error, sin permisos, dato inexistente
- **Roles**: cada rol intentando lo que no debería poder hacer
- **Idioma y formato**: fechas, monedas, decimales, caracteres especiales, emojis
- **Compatibilidad**: otra resolución, otro navegador, teclado y zoom
- **Explotación del error**: provocar el error y seguir explorando desde ahí
- **Concurrencia**: dos pestañas editando el mismo registro

## Uso del Playwright MCP en sesiones exploratorias

- `browser_snapshot` para inventariar todo lo interactuable de la pantalla y no olvidar elementos.
- `browser_console_messages` para detectar errores de JavaScript ocultos al usuario.
- `browser_network_requests` para revisar respuestas lentas, códigos 4xx/5xx y payloads inesperados.
- `browser_network_state_set` con `offline` para explorar el comportamiento sin red.
- `browser_take_screenshot` en cada hallazgo, inmediatamente, sin esperar al cierre de la sesión.

## Reporte SBTM

```
SESIÓN: S-<n>  |  Charter: <nombre>  |  Timebox: <min>  |  Duración real: <min>
ENTORNO: build <versión>, <entorno>, <navegador>, <resolución>
COBERTURA: <áreas/pantallas/flujos visitados>
TAREAS:
 - <min> min  <actividad>
HALLAZGOS:
 - <descripción breve> -> <defecto DEF-xxx | caso TC-xxx | pregunta>
DEFECTOS: <n por severidad>
PREGUNTAS / BLOQUEOS: <pendientes>
NOTAS: <observaciones y oportunidades>
```

## Salida Esperada

- Charters definidos y timeboxeados.
- Reporte de sesión SBTM por cada charter ejecutado.
- Lista de hallazgos convertidos en defectos y en nuevos casos de prueba (creados desde las plantillas obligatorias de `templates/`).
- Áreas no exploradas y cobertura alcanzada.

## Reglas

- Toda sesión exploratoria debe tener charter y timebox; sin charter no es exploratoria, es improvisación.
- Registrar hallazgos en el momento, no de memoria.
- Un hallazgo sin evidencia (screenshot, log, red) no puede convertirse en defecto.
- Al cerrar: convertir los hallazgos relevantes en casos de prueba formales para futuras regresiones.
- Los nuevos casos formales se construyen SIEMPRE desde las plantillas obligatorias de `templates/` (`tc_template.md` o `bdd_template.md`): nunca desde cero.
