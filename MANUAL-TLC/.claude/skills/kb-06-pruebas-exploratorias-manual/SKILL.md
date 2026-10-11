---
name: kb-06-pruebas-exploratorias-manual
description: Skill autónoma de conocimiento sobre pruebas exploratorias manuales: charters, heurísticas, SBTM y gestión de sesiones. No depende de archivos externos.
---

# Pruebas Exploratorias Manuales

## Definición

En las pruebas exploratorias el tester **aprende, diseña y ejecuta de forma simultánea**, usando la información obtenida durante la propia ejecución para decidir el siguiente paso. Es el instrumento principal para descubrir lo que los casos predefinidos no anticiparon.

## Cuándo aplicarlas

- Funcionalidad nueva o recién integrada.
- Requisitos ambiguos, incompletos o contradictorios.
- Áreas con alto riesgo y bajo conocimiento.
- Después de un cambio grande o de una refactorización.
- Como complemento del ciclo formal, antes del release.

## Charter

Un charter define el objetivo de la sesión.

```
CHARTER: EXPLORAR <área/funcionalidad>
CON <recursos: rol, datos, navegador, entorno>
PARA DESCUBRIR <riesgo, información o comportamiento buscado>
TIMEBOX: <minutos>
```

**Ejemplos:**
```
CHARTER: EXPLORAR el checkout con el rol cliente
CON tarjetas de prueba, cupones variados y Chromium en 1440x900
PARA DESCUBRIR inconsistencias entre el total mostrado y el total enviado
TIMEBOX: 90 minutos

CHARTER: EXPLORAR la gestión de permisos
CON los cuatro roles y datos compartidos
PARA DESCUBRIR accesos no autorizados a acciones o datos
TIMEBOX: 60 minutos
```

## Heurísticas de exploración

### SFDPOT (San Francisco Depot)
| Área | Preguntas |
|---|---|
| **Structure** | ¿Qué compone el sistema? ¿Qué no se ve? |
| **Function** | ¿Qué hace? ¿Qué debería hacer y no hace? |
| **Data** | ¿Qué entra, qué se guarda, qué sale? ¿Qué pasa con datos límite? |
| **Platform** | ¿En qué depende del navegador, SO o dispositivo? |
| **Operations** | ¿Cómo se usa en el día a día real? |
| **Time** | ¿Qué pasa con concurrencia, timeout, orden, duración? |

### CRUD
Crear, leer, actualizar y borrar cada entidad, incluyendo operaciones sobre entidades inexistentes o ya borradas.

### Interrupciones y estados
- Recargar la página a mitad de un flujo.
- Botón atrás del navegador tras una acción.
- Cerrar y reabrir la pestaña.
- Sesión expirada a mitad del flujo.
- Doble clic o doble submit.
- Dos pestañas editando el mismo registro.

### Límites y datos
Vacío, un elemento, máximo, máximo+1, caracteres especiales, emojis, acentos, espacios, cero, negativo, decimales, fechas lejanas.

### Roles y permisos
Cada rol intentando la acción que no le corresponde: por URL directa, por acción oculta o por petición de red visible en las herramientas de desarrollo.

### Compatibilidad
Otra resolución, otro navegador, zoom al 200%, teclado sin mouse, navegación con Tab.

### Caos controlado
Usar `browser_network_state_set` con `offline` y `browser_route` para forzar errores, y observar el comportamiento del sistema.

## SBTM (Session-Based Test Management)

### Reporte de sesión

```
SESIÓN      : S-03
Charter     : Explorar el checkout con cupones variados
Timebox     : 90 min   |   Duración real: 85 min
Ambiente    : qa, build 4.3.0, Chromium 129, 1440x900, rol cliente
COBERTURA   : carrito, cupones, checkout, confirmación  (60% del charter)

TAREAS
  00:00-00:15  Reconocimiento del flujo de carrito
  00:15-00:45  Exploración de cupones válidos, expirados e inexistentes
  00:45-01:10  Combinaciones de cupón + envío + impuestos
  01:10-01:25  Interrupciones: recarga, atrás y doble submit

HALLAZGOS
  H1  Cupón del 100% envía total null al confirmar        -> DEF-0341 (HIGH)
  H2  Mensaje de cupón expirado es genérico               -> DEF-0343 (LOW)
  H3  Al recargar el carrito se pierde el cupón aplicado  -> TC-FUNC-021 (nuevo caso)
  H4  Total con impuestos se recalcula al ir atrás        -> DEF-0344 (MEDIUM)

DEFECTOS      : 3 (1 HIGH, 1 MEDIUM, 1 LOW)
PREGUNTAS     : ¿el cupón debe sobrevivir a la recarga del carrito?
BLOQUEOS      : ninguno
NOTAS         : el flujo de pago con 3D Secure no fue explorado (fuera del timebox)
```

### Métricas de SBTM

| Métrica | Fórmula | Uso |
|---|---|---|
| Charter Coverage | área_cubierta / área_del_charter | Ajustar el timebox |
| Session Duration Variance | real / planificada | Estimar mejor |
| Findings per Hour | hallazgos / horas | Efectividad de la sesión |
| Defect Ratio | defectos / hallazgos | Calidad de los hallazgos |
| Areas Not Covered | áreas pendientes | Planificar la próxima sesión |

## Heurísticas de parada

Detener la sesión cuando:
- El timebox se agota.
- El área deja de producir hallazgos nuevos (paradoja del pesticida).
- Se descubre un defecto bloqueante que impide continuar.
- El entorno se degrada y los resultados dejan de ser fiables.

## Uso del Playwright MCP en exploración

- `browser_snapshot`: inventariar todo lo interactuable y no olvidar elementos.
- `browser_console_messages`: detectar errores de JavaScript invisibles al usuario.
- `browser_network_requests`: detectar peticiones duplicadas, lentas o con 4xx/5xx.
- `browser_network_state_set`: explorar el comportamiento sin red.
- `browser_take_screenshot`: evidenciar cada hallazgo en el momento.

## Anti-patrones

1. Explorar sin charter ni timebox: es improvisación, no exploración.
2. Registrar hallazgos de memoria al final de la sesión.
3. Quedarse en el happy path.
4. No variar datos ni secuencias.
5. Convertir hallazgos en defectos sin evidencia.
6. No transferir los hallazgos a la suite de regresión.
7. Usar la exploración como excusa para no documentar nada.
