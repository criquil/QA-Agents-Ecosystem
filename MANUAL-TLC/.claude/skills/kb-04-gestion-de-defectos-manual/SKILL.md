---
name: kb-04-gestion-de-defectos-manual
description: Skill autónoma de conocimiento sobre gestión de defectos en pruebas manuales: ciclo de vida, severidad, prioridad y reporte. No depende de archivos externos.
---

# Gestión de Defectos en Pruebas Manuales

## Definición

Un **defecto** es una desviación entre el comportamiento observado del sistema y el comportamiento esperado según el requisito o el criterio de aceptación.

## Ciclo de vida del defecto

```
Nuevo -> Triado -> Asignado -> En progreso -> Resuelto -> En verificación -> Cerrado
                                                        \-> Reabierto
                                                        \-> Rechazado (no es defecto)
                                                        \-> Diferido (postergado)
```

## Campos obligatorios de un reporte

| Campo | Descripción |
|---|---|
| ID | Identificador único (DEF-0001) |
| Título | Qué falla y dónde, en una línea |
| Módulo | Módulo o pantalla afectada |
| Tipo de prueba | funcional, sistema, regresión, smoke, sanity, exploratoria, UAT |
| Severidad | Impacto técnico: CRITICAL, HIGH, MEDIUM, LOW |
| Prioridad | Urgencia de corrección: P1, P2, P3 |
| Entorno / Build | Dónde se reprodujo |
| Navegador / Resolución | Contexto de ejecución |
| Rol | Usuario con el que se reprodujo |
| Precondiciones | Estado previo necesario |
| Pasos de reproducción | Numerados y deterministas |
| Resultado esperado | Según el requisito |
| Resultado observado | Lo que realmente ocurrió |
| Frecuencia | Siempre, intermitente, una vez |
| Evidencia | Screenshot, video, traza, consola, red |
| Trazabilidad | Caso de prueba y requisito afectados |

## Severidad vs Prioridad

| Severidad | Descripción |
|---|---|
| CRITICAL | Bloquea el flujo principal o hay pérdida/corrupción de datos |
| HIGH | Impide completar una función relevante sin workaround |
| MEDIUM | Función afectada pero existe workaround razonable |
| LOW | Cosmético, textual, de formato o de usabilidad menor |

| Prioridad | Descripción |
|---|---|
| P1 | Debe corregirse antes del release |
| P2 | Debe corregirse en el sprint actual |
| P3 | Puede planificarse para más adelante |

La severidad mide el impacto; la prioridad mide la urgencia de negocio. Un defecto LOW de severidad puede ser P1 si el negocio lo requiere (por ejemplo, un texto legal incorrecto).

## Plantilla de reporte

```markdown
## DEF-0341 — El total del pedido no aplica el cupón del 100%

| Campo | Valor |
|---|---|
| Módulo | Checkout |
| Tipo de prueba | Funcional |
| Severidad | HIGH |
| Prioridad | P1 |
| Entorno / Build | QA / 4.3.0 |
| Navegador | Chromium 129, 1440x900 |
| Rol | Cliente |
| Frecuencia | Siempre |
| Trazabilidad | REQ-014 / TC-FUNC-012 |

**Precondiciones**
Carrito con 2 productos y cupón `FULL100` cargado.

**Pasos de reproducción**
1. Iniciar sesión como cliente.
2. Agregar 2 productos al carrito.
3. Aplicar el cupón `FULL100`.
4. Observar el total del pedido.

**Resultado esperado**
Total = 0,00 y mensaje "Cupón aplicado: 100% de descuento".

**Resultado observado**
Total = 0,00 en pantalla, pero la petición `POST /orders` envía `total: null`
y la orden se guarda con `total` nulo.

**Evidencia**
- evidence/checkout/TC-FUNC-012-paso3-20260921T1042.png
- evidence/checkout/TC-FUNC-012-console-20260921T1042.log
- evidence/checkout/TC-FUNC-012-network-20260921T1042.json
```

## Reglas de oro del reporte

1. **Reproducible**: otro tester debe poder reproducirlo siguiendo los pasos.
2. **Un defecto por reporte**: no agrupar problemas distintos.
3. **Evidencia siempre**: sin evidencia el defecto suele volver rechazado.
4. **Título autoexplicativo**: qué falla, dónde y con qué condición.
5. **Datos concretos**: usuario, rol, valor exacto, build exacto.
6. **Sin juicios**: describir hechos, no atribuir culpas ni sugerir quién lo causó.
7. **Buscar duplicados** antes de reportar.

## Triado y clasificación

| Resultado del triado | Cuándo |
|---|---|
| Aceptado | Defecto válido y reproducible |
| Duplicado | Ya existe un reporte equivalente |
| No reproducible | Falta información o depende de condiciones no documentadas |
| No es defecto (by design) | El comportamiento es el que el requisito define |
| Requisito ambiguo | Se necesita aclaración funcional antes de decidir |
| Caso de prueba incorrecto | La expectativa del caso estaba mal especificada |

## Métricas de defectos

| Métrica | Fórmula | Target |
|---|---|---|
| Defect Density | defectos / módulo | ≤ 5 |
| Defect Detection Effectiveness | defectos_válidos / reportados | ≥ 90% |
| Rejection Rate | defectos_rechazados / reportados | ≤ 10% |
| Reopen Rate | reabiertos / cerrados | ≤ 10% |
| Defect Resolution Time | tiempo medio hasta el cierre | ≤ 5 días |
| Escape Rate | defectos_en_producción / total | ≤ 10% |

## Anti-patrones

1. Reportar sin evidencia.
2. Reportar varios problemas en un solo ticket.
3. Títulos genéricos ("no funciona").
4. Reportar sin verificar duplicados.
5. Aceptar un defecto como "no reproducible" sin insistir con más contexto.
6. Reabrir un defecto sin nuevos datos.
7. Marcar como PASS un caso con un trabajo alternativo no documentado.
