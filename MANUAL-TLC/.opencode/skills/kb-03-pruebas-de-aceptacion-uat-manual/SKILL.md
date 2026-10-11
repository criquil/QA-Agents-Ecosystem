---
name: kb-03-pruebas-de-aceptacion-uat-manual
description: Skill autónoma de conocimiento sobre pruebas de aceptación de usuario (UAT) manuales: criterios de aceptación, guiones, ejecución facilitada y firma. No depende de archivos externos.
---

# Pruebas de Aceptación de Usuario (UAT) Manuales

## Definición

Proceso de validación en el que el **usuario de negocio** determina si el sistema cumple los criterios de aceptación acordados y, en consecuencia, lo acepta o lo rechaza antes del pase a producción.

## Principios

1. **El negocio decide**: el QA facilita, evidencia y documenta; no acepta en su nombre.
2. **Criterios primero**: sin criterios de aceptación firmados no se inicia la UAT.
3. **Escenarios de negocio, no pantallas**: se valida el proceso completo, no la UI aislada.
4. **Entorno congelado**: nada cambia durante la UAT salvo bloqueantes justificados.
5. **Evidencia formal**: cada criterio verificado deja evidencia y comentario del usuario.

## Criterios de aceptación: cómo escribirlos

```
MALO : "El módulo de facturación debe funcionar correctamente"
BUENO: "El usuario de facturación puede emitir una factura desde un pedido
        confirmado; la factura muestra el mismo total que el pedido y queda
        disponible en el histórico en menos de 5 segundos"

MALO : "La búsqueda debe ser rápida"
BUENO: "La búsqueda de un cliente por documento devuelve el resultado
        en ≤ 3 s con 50.000 registros cargados"
```

Un buen criterio de aceptación es: **específico, medible, verificable por el negocio, con resultado esperado explícito y sin ambigüedad**.

## Flujo UAT

```
1. Acordar y firmar los criterios de aceptación      (negocio + QA)
2. Definir los escenarios de negocio end-to-end      (negocio + QA)
3. Preparar entorno congelado, cuentas y datos       (TI + QA)
4. Elaborar el guion UAT con trazabilidad a criterios (QA)
5. Ejecutar la sesión con el usuario de negocio      (negocio, QA facilita)
6. Registrar resultado por criterio con evidencia    (QA)
7. Documentar defectos y observaciones               (QA + Dev)
8. Resolver bloqueantes y re-validar                 (Dev + negocio)
9. Obtener la firma de aceptación o rechazo          (negocio)
```

## Plantilla de guion UAT

```
UAT-<n>     : <escenario de negocio>
Criterio    : AC-<n> — <texto del criterio firmado>
Rol         : <rol de negocio que ejecuta>
Precondición: <build, entorno, datos, cuentas>
Pasos       : 1) ... 2) ... 3) ...
Esperado    : <resultado en lenguaje de negocio>
Evidencia   : <screenshot / PDF / correo / reporte>
Resultado   : Aceptado | Aceptado con observaciones | Rechazado
Comentario  : <texto del usuario de negocio>
```

## Tipos de UAT

| Tipo | Enfoque |
|---|---|
| **Alpha (interna)** | Usuarios de la propia organización antes de salir |
| **Beta (externa)** | Usuarios reales en condiciones reales |
| **Contractual / regulatoria** | Cumplimiento de contrato o normativa, con evidencia formal |
| **Operacional** | Procesos de operación y soporte del día a día |
| **De regresión de negocio** | Confirmar que el negocio sigue operando tras un cambio |

## Gestión de resultados

| Resultado | Acción |
|---|---|
| Aceptado | Se documenta la firma y se procede al release |
| Aceptado con observaciones | Se listan observaciones, responsables y plazo; ninguno es bloqueante |
| Rechazado | Se documentan los bloqueantes; requiere nuevo build y nueva sesión UAT |

## Uso del Playwright MCP durante la UAT

- Conducir el flujo mientras el usuario de negocio observa y decide.
- Capturar screenshot por criterio de aceptación y por cada pantalla relevante.
- Generar PDF (`browser_pdf_save`) de comprobantes, facturas o reportes que el negocio necesite conservar.
- Usar capturas de página completa para reportes y listados.
- Grabar video en sesiones UAT de procesos largos o críticos.

## Métricas de UAT

| Métrica | Target |
|---|---|
| Acceptance Criteria Pass | 100% |
| Blocking Defects at Sign-off | 0 |
| Participant Coverage | ≥ 90% de los participantes planificados |
| Sign-off Timeliness | 100% dentro de la ventana acordada |
| Rework Cycles (sesiones repetidas) | ≤ 1 |

## Anti-patrones

1. Que QA ejecute la UAT "en nombre del negocio".
2. Iniciar la UAT sin criterios de aceptación escritos.
3. Usar datos irreales que no representan el proceso de negocio.
4. Ejecutar la UAT sobre un entorno que cambia durante la sesión.
5. Aceptar con bloqueantes abiertos.
6. Registrar resultados sin evidencia ni comentario del usuario.
