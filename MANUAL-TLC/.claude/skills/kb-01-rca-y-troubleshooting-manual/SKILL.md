---
name: kb-01-rca-y-troubleshooting-manual
description: Skill autónoma de conocimiento sobre rca y troubleshooting de defectos encontrados en pruebas manuales. No depende de archivos externos.
---

# RCA y Troubleshooting para Pruebas Manuales

## Técnicas de Root Cause Analysis

### 1. 5 Whys

Preguntar "¿por qué?" sucesivamente hasta llegar a la causa raíz.

**Ejemplo (defecto de UI):**
1. ¿Por qué falló el caso? → El botón "Confirmar compra" no respondió
2. ¿Por qué no respondió? → Se lanzó un error de JavaScript al hacer clic
3. ¿Por qué se lanzó el error? → El total del carrito llegó como `null`
4. ¿Por qué llegó `null`? → El cupón aplicado vació el cálculo del total
5. ¿Por qué vació el total? → La validación del cupón no contempla el caso de descuento del 100%

### 2. Fishbone (Ishikawa) para testing manual

- **Personas:** pasos mal interpretados, falta de contexto de negocio, UAT sin inducción.
- **Proceso:** casos incompletos, precondiciones no declaradas, ausencia de datos semilla.
- **Herramienta:** sesión MCP caída, snapshot obsoleto, navegador desactualizado.
- **Entorno:** build equivocado, datos no reseteados, integración externa caída, entorno lento.
- **Datos:** cuenta sin permisos, dato caducado, dato inconsistente.
- **Requisito:** criterio de aceptación ambiguo, requisito ausente, requisito contradictorio.

### 3. 8D Report

1. Formar equipo
2. Definir el problema
3. Contener el problema (evitar más daño en producción)
4. Identificar causa raíz
5. Elegir acciones correctivas
6. Implementar acciones
7. Prevenir recurrencia (agregar el caso a la regresión)
8. Reconocer al equipo

## Troubleshooting común en sesiones manuales

| Síntoma | Causa común | Solución |
|---------|-------------|----------|
| No puedo iniciar sesión | Credenciales caducadas o cuenta bloqueada | Verificar vigencia, desbloquear, confirmar rol |
| El elemento no existe / no aparece | Snapshot obsoleto o UI aún cargando | Refrescar snapshot, `browser_wait_for` el texto esperado |
| Resultado distinto a la sesión anterior | Dato preexistente o caché | Resetear entorno, usar datos semilla, repetir |
| Mensaje de error de red en la UI | Dependencia externa caída | Verificar servicio, reportar como riesgo de entorno |
| La pantalla queda cargando | Performance degradada o recurso bloqueado | Medir tiempos, revisar red y consola |
| Comportamiento solo en un navegador | Incompatibilidad real | Reproducir en la matriz completa y reportar |
| Las herramientas `browser_*` fallan | Servidor MCP no disponible | Verificar configuración MCP y reiniciar la sesión |
| El dato se duplica | Doble submit o falta de idempotencia | Reproducir con doble clic y registrar defecto |

## Clasificación de la causa raíz

| Categoría | Cuándo asignarla |
|---|---|
| Requisito | El comportamiento observado no contradice ningún requisito escrito o el requisito es ambiguo |
| Diseño funcional | La lógica de negocio está implementada de forma incorrecta o incompleta |
| Validación de UI | Faltan validaciones, mensajes o estados de error |
| Datos | El defecto depende de un dato concreto o de su ausencia |
| Entorno | El defecto desaparece en otro entorno o con el entorno reseteado |
| Dependencia externa | El defecto proviene de un servicio de terceros |
| Performance | El defecto es de tiempo de respuesta o de percepción de lentitud |
| Accesibilidad | El defecto impide el uso con teclado, lector de pantalla o contraste insuficiente |
| Caso de prueba | El caso estaba mal especificado: expectativa incorrecta, no defecto |

## Reglas

1. Nunca declarar causa raíz sin evidencia adjunta (screenshot, consola, red o traza).
2. Separar siempre: defecto real, falso positivo, limitación de la herramienta y caso mal especificado.
3. Todo defecto P1 debe tener RCA documentado y acción preventiva que evite su recurrencia.
4. Si la causa raíz es un caso de prueba mal especificado, corregir el caso y versionar el cambio.
5. La acción preventiva por defecto es agregar o reforzar el caso en la suite de regresión.
