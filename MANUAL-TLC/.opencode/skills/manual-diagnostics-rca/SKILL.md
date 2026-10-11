---
name: manual-diagnostics-rca
description: Usa esta skill para diagnosticar defectos encontrados en sesiones de prueba manual, identificar la causa raíz (RCA) y proponer acciones correctivas. Cubre: reproducción, evidencia de UI, análisis de consola y red, y clasificación de severidad.
---

# Manual Diagnostics & RCA

## Objetivo

Diagnosticar los defectos encontrados durante una sesión de prueba manual y determinar la causa raíz con evidencia, separando siempre el defecto real del falso positivo provocado por el entorno, los datos o el propio caso de prueba.

## Flujo

1. **Reproducir**: confirmar que el defecto es reproducible siguiendo los pasos registrados y con el mismo entorno/build.
2. **Clasificar el defecto**: requisito ambiguo, validación de UI, lógica de negocio, datos, configuración de entorno, dependencia externa, rendimiento percibido, defecto visual o responsive, accesibilidad, caso de prueba mal especificado.
3. **Recopilar evidencia**: screenshot del estado fallido, mensajes de consola, peticiones de red relevantes, versión de build, navegador, resolución, rol usado y datos de entrada.
4. **Descartar causas espurias**: caché, sesión expirada, dato preexistente, orden de pasos, otro navegador, entorno no reseteado.
5. **Aplicar técnicas RCA**: 5 Whys, Fishbone, Fault Tree.
6. **Identificar la causa raíz** vinculada a evidencia concreta.
7. **Clasificar severidad y prioridad** (CRITICAL/HIGH/MEDIUM/LOW y P1/P2/P3) y proponer acciones correctivas.

## Fishbone adaptado a pruebas manuales

- **Personas**: pasos mal interpretados, falta de conocimiento del dominio, usuario de UAT sin contexto.
- **Proceso**: caso de prueba incompleto, precondiciones no verificadas, ausencia de datos semilla.
- **Herramienta**: sesión MCP caída, snapshot desactualizado, navegador desactualizado.
- **Entorno**: build incorrecto, datos no reseteados, integración externa caída, entorno lento.
- **Datos**: cuenta sin permisos, datos inconsistentes, dato caducado.
- **Requisito**: criterio de aceptación ambiguo o ausente.

## Troubleshooting común en sesiones manuales

| Síntoma | Causa común | Acción |
|---------|-------------|--------|
| No se puede iniciar sesión | Credenciales caducadas o usuario bloqueado | Verificar vigencia y desbloquear la cuenta |
| Elemento no encontrado | Snapshot desactualizado o UI no cargada | Refrescar snapshot y esperar el texto/estado esperado |
| Resultado inconsistente entre ejecuciones | Dato preexistente o caché | Resetear entorno y repetir |
| Error de red en el navegador | Dependencia externa caída | Verificar el servicio y reportar como riesgo de entorno |
| La página queda en carga | Performance degradada o recurso bloqueado | Medir tiempos y capturar red |
| Comportamiento distinto por navegador | Incompatibilidad real | Reproducir en la matriz y reportar |
| `browser_*` falla repetidamente | Servidor MCP no disponible | Verificar el MCP configurado y reiniciar la sesión |

## Salida Esperada

- Clasificación del tipo de defecto.
- Evidencia recopilada (screenshots, consola, red, build, navegador, rol).
- Causa raíz identificada con técnica RCA aplicada.
- Severidad y prioridad justificadas.
- Acciones correctivas priorizadas (P1/P2/P3) con responsable estimado.

## Reglas

- Un defecto sin pasos de reproducción y sin evidencia no es un defecto reportable.
- Separar siempre defecto real, falso positivo y limitación de la herramienta.
- Nunca atribuir la causa raíz al "usuario" sin evidencia de proceso o diseño.
