---
name: manual-uat-workflow
description: Usa esta skill para planificar y ejecutar pruebas de aceptación de usuario (UAT) manuales, con criterios de aceptación de negocio, guiones de usuario y firma formal de aceptación.
---

# Manual UAT Workflow

## Objetivo

Planificar, facilitar y evidenciar las **Pruebas de Aceptación de Usuario (UAT)** manuales, de modo que el negocio acepte o rechace el sistema con base en criterios verificables y evidencia.

## Diferencia con Pruebas Funcionales y de Sistema

| | Funcionales / Sistema | UAT |
|---|---|---|
| Quién ejecuta | QA | Usuario de negocio / Product Owner |
| Base de diseño | Requisitos funcionales y de sistema | Criterios de aceptación de negocio |
| Pregunta | ¿Funciona según especificación? | ¿Sirve para el negocio? ¿Lo aceptamos? |
| Resultado | PASS/FAIL técnico | Aceptado / Aceptado con condiciones / Rechazado |

## Flujo

1. **Confirmar los criterios de aceptación** de negocio (medibles, firmados antes de ejecutar).
2. **Definir los escenarios de negocio end-to-end** (no pantallas aisladas): alta de cliente, compra completa, conciliación, cierre de mes, etc.
3. **Identificar los participantes**: usuario de negocio, product owner, QA como facilitador, TI como soporte.
4. **Preparar el entorno y los datos**: entorno estable congelado, cuentas reales de negocio, datos semilla realistas.
5. **Elaborar el guion UAT**: caso, criterio de aceptación asociado, pasos en lenguaje de negocio, resultado esperado, evidencia requerida.
6. **Ejecutar la sesión UAT** acompañando al usuario; el QA facilita con Playwright MCP para conducir y capturar evidencia, pero **el juicio de aceptación es del negocio**.
7. **Registrar** por cada criterio: Aceptado / Aceptado con observaciones / Rechazado, con evidencia y comentario del usuario.
8. **Documentar defectos y solicitudes de cambio** derivados; clasificarlos por bloqueante y no bloqueante.
9. **Obtener la firma formal** de aceptación o rechazo.

## Criterios de aceptación: buenos vs malos

```
MALO:  "El módulo de pagos debe funcionar bien"
BUENO: "Un cliente puede pagar con tarjeta válida y recibe confirmación
        en pantalla y por correo en menos de 2 minutos"

MALO:  "El reporte debe ser rápido"
BUENO: "El reporte mensual con 12 meses de datos carga en ≤ 5 s en Chromium
        con la cuenta de gerente"
```

## Guion UAT (plantilla)

```
UAT-<n>: <nombre del escenario de negocio>
Criterio de aceptación: <criterio firmado>
Rol del usuario: <rol de negocio>
Precondiciones: <build, datos, cuentas>
Pasos:
  1. ...
  2. ...
Resultado esperado en lenguaje de negocio: ...
Evidencia requerida: screenshot / PDF / correo recibido
Resultado obtenido: Aceptado | Aceptado con observaciones | Rechazado
Comentario del usuario: ...
```

## Uso del Playwright MCP en UAT

- Conducir el flujo mientras el usuario de negocio observa y decide.
- Capturar screenshot por criterio de aceptación.
- Generar `browser_pdf_save` de comprobantes o reportes cuando el negocio necesite el documento como evidencia.
- Usar `browser_take_screenshot` con `fullPage` para evidenciar reportes y listados completos.

## Salida Esperada

- Criterios de aceptación firmados.
- Guion UAT con escenarios de negocio.
- Resultado por criterio con evidencia y comentario del usuario.
- Lista de defectos y observaciones por impacto en la aceptación.
- Acta de aceptación: Aceptado / Aceptado con condiciones / Rechazado.

## Reglas

- Sin criterios de aceptación definidos y firmados no se inicia UAT.
- El QA no firma la aceptación en nombre del negocio.
- Todo "Aceptado con condiciones" debe listar condiciones, responsables y plazo.
- Los defectos bloqueantes deben resolverse y re-validarse antes de la aceptación final.
