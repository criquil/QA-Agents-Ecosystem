---
name: api-diagnostics-rca
description: Usa esta skill para diagnosticar fallos en pruebas de API, identificar la causa raíz (RCA) y proponer acciones correctivas. Cubre: validación de contratos, error handling, timeout analysis y dependency mapping.
---

# API Diagnostics & RCA

## Objetivo
Diagnosticar fallos en pruebas de API y determinar la causa raíz con evidencia.

## Flujo
1. Clasifica el fallo: contrato, HTTP, timeout, autenticación, datos, dependencia.
2. Recopila evidencia: logs, traces, request/response bodies, status codes.
3. Aplica técnicas RCA: 5 Whys (preguntar "¿por qué?" hasta la causa raíz), Fishbone/Ishikawa (categorías: personas, proceso, herramientas, entorno, datos), Fault Tree.
4. Identifica causa raíz con evidencia vinculada.
5. Propón acciones correctivas priorizadas (P1/P2/P3).

## Referencias rápidas de troubleshooting

| Problema | Causa común | Solución |
|----------|-------------|----------|
| 401 Unauthorized | Token expirado | Refresh token, re-autenticar |
| 403 Forbidden | Permisos insuficientes | Verificar roles y permisos |
| 404 Not Found | Endpoint incorrecto | Verificar URL y versionado |
| 429 Too Many Requests | Rate limiting | Implementar backoff, reducir frecuencia |
| 500 Internal Server Error | Bug en backend | Escalar a equipo de desarrollo |
| Timeout | Server lento o caído | Verificar disponibilidad, ajustar timeout |
| Connection Refused | Servicio no disponible | Verificar que el servicio esté corriendo |

## Salida Esperada
- Clasificación del tipo de fallo.
- Evidencia recopilada (logs, traces, requests).
- Causa raíz identificada con técnica RCA aplicada.
- Acciones correctivas priorizadas (P1/P2/P3) con responsable estimado.
