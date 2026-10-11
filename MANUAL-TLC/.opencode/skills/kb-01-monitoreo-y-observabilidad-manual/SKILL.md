---
name: kb-01-monitoreo-y-observabilidad-manual
description: Skill autónoma de conocimiento sobre observabilidad de sesiones de prueba manual. No depende de archivos externos.
---

# Monitoreo y Observabilidad de Sesiones de Prueba Manual

## Objetivo

Hacer observable una sesión manual: qué se ejecutó, qué se observó, con qué evidencia y con qué señales técnicas de respaldo, de modo que cualquier resultado sea auditable y reproducible.

## Capas de Observabilidad de una Sesión Manual

### 1. Observación del tester (capa primaria)
- Lo que el usuario humano ve: mensajes, estados, formato, coherencia visual.
- Registro del paso ejecutado y del resultado observado.
- Comentarios cualitativos: confusión, fricción, ambigüedad del mensaje.

### 2. Evidencia visual (capa documental)
- Screenshot por paso crítico y en cada hallazgo.
- Screenshot de página completa (`fullPage`) para reportes y listados.
- Video de sesión para flujos largos o UAT.
- PDF para comprobantes, facturas y reportes que el negocio necesita como documento.

### 3. Señales técnicas (capa de diagnóstico)
- `browser_console_messages`: errores de JavaScript invisibles al usuario, warnings, deprecaciones.
- `browser_network_requests`: códigos 4xx/5xx, latencias altas, payloads inesperados, llamadas duplicadas.
- Timeout y estado de la sesión (expiración, cierre inesperado).
- Verificación de build/versión desplegada visible en la UI.

### 4. Trazas de sesión (capa de reproducción)
- `browser_start_tracing` / `browser_stop_tracing` para obtener una traza reproducible paso a paso.
- La traza permite volver al momento exacto de un defecto sin depender de la memoria del tester.

## Convención de artefactos

```
PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/{CASE-ID}/
├── {CASE-ID}-{paso}-{timestamp}.png     # screenshots
├── {CASE-ID}-full-{timestamp}.png       # página completa de reportes
├── {CASE-ID}-{timestamp}.webm           # video de sesión
├── {CASE-ID}-trace-{timestamp}.zip      # traza de sesión
├── {CASE-ID}-{timestamp}.pdf            # documentos de negocio
└── {CASE-ID}-console-{timestamp}.log    # mensajes de consola
```

## Dashboards recomendados

1. **Session Dashboard** — casos por hora, sesiones activas, blocked rate.
2. **Defect Dashboard** — defectos por severidad, módulo y navegador.
3. **Coverage Dashboard** — cobertura por requisito, módulo y tipo de prueba.
4. **UAT Dashboard** — criterios aceptados, observaciones y estado de firma.

## Buenas prácticas

1. Capturar la evidencia en el momento, no al final de la sesión.
2. Nombrar la evidencia con el ID del caso: hace la auditoría trivial.
3. Adjuntar la evidencia al defecto en el mismo acto de su registro.
4. Registrar siempre navegador, resolución, rol, build y entorno de la sesión.
5. No depender de logs de servidor para validar un defecto de UI: la evidencia del navegador es la fuente primaria.
6. Si la consola o la red muestran errores, registrarlos aunque el caso haya pasado: son riesgos latentes.
