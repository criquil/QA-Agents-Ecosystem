---
name: kb-04-smoke-y-sanity-testing-manual
description: Skill autónoma de conocimiento sobre smoke testing y sanity testing manuales: alcance, casos mínimos, gates y diferencias. No depende de archivos externos.
---

# Smoke Testing y Sanity Testing Manuales

## Definición

### Smoke Testing
Verificación mínima, amplia y superficial que responde a la pregunta: **¿este build es lo bastante estable para probarlo en serio?** Es un gate: si el smoke falla, todo el ciclo se detiene.

### Sanity Testing
Verificación estrecha y profunda que responde a la pregunta: **¿este fix funciona y no rompió lo inmediato?** Se ejecuta sobre un cambio puntual, no sobre el sistema completo.

## Diferencias

| | Smoke Testing | Sanity Testing |
|---|---|---|
| Pregunta | ¿Es testeable? | ¿El fix es correcto? |
| Amplitud | Amplia | Estrecha |
| Profundidad | Superficial | Profunda |
| Momento | Al recibir cada build | Tras un fix o cambio puntual |
| Cobertura | Pantallas y flujos vitales | El módulo afectado y su entorno inmediato |
| Duración | 15–45 min | 30–90 min |
| Documentación | Caso ligero, lista de verificación | Caso detallado del fix |
| Resultado | Go / No-Go para el ciclo | Fix verificado / rechazado |
| Sustituye a | Nada | Nada (no reemplaza la regresión) |
| Ejecuta | QA | QA |

> Un smoke aprobado **no** implica calidad; sólo implica que el build es testeable.
> Un sanity aprobado **no** implica ausencia de regresiones en el resto del sistema.

## Smoke: casos mínimos recomendados

```
SMK-01  La aplicación carga y responde en el entorno correcto
SMK-02  Se verifica la versión/build desplegado en la UI
SMK-03  El login funciona con cada rol principal
SMK-04  El menú principal y las pantallas clave abren sin error
SMK-05  Una operación de lectura trae datos reales
SMK-06  Una operación de escritura básica se completa
SMK-07  No hay errores de JavaScript en consola en el arranque
SMK-08  No hay respuestas 5xx en las peticiones iniciales
```

### Checklist de smoke

```
[ ] URL del entorno responde
[ ] Build/versión confirmado en la UI
[ ] Login admin, operador y cliente
[ ] Navegación por los módulos principales
[ ] Una lectura y una escritura por módulo crítico
[ ] Consola sin errores bloqueantes
[ ] Sin respuestas 5xx en las peticiones de pantalla
```

## Sanity: casos típicos

```
SNT-01  Reproducir el defecto original y confirmar que ya no ocurre
SNT-02  Ejecutar variantes cercanas al defecto (mismo campo, otros valores)
SNT-03  Verificar la función directamente relacionada
SNT-04  Verificar el caso límite que originó el defecto
SNT-05  Confirmar que la corrección no afectó el flujo inmediato
```

## Uso del Playwright MCP

### Smoke

```
browser_navigate      -> URL base del entorno
browser_snapshot      -> verificar render y build
browser_console_messages / browser_network_requests -> errores en el arranque
browser_fill_form + browser_click -> login por rol
browser_take_screenshot           -> evidencia del smoke
```

### Sanity

```
browser_navigate      -> URL del módulo afectado
reproducir los pasos exactos del defecto original
browser_take_screenshot -> evidencia de la corrección
browser_take_screenshot del caso límite asociado
```

## Criterios de resultado

| Tipo | PASS | FAIL |
|---|---|---|
| Smoke | Todos los puntos de la checklist OK | Cualquier punto vital falla → detener el ciclo |
| Sanity | El fix funciona y no rompe lo inmediato | El fix no funciona o rompe la función relacionada |

## Reglas

1. **Nunca se salta el smoke.** Es el gate de entrada de todo ciclo.
2. Un smoke fallido se reporta de inmediato y se devuelve el build.
3. El sanity se ejecuta **antes** de devolver el build a regresión (ahorra ciclos completos).
4. Smoke y sanity no sustituyen a las pruebas funcionales, de sistema ni de regresión.
5. Ambos dejan evidencia, aunque sea mínima.
6. Si el smoke falla por causa de entorno, se clasifica como problema de entorno, no como defecto de producto.
