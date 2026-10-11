---
name: kb-04-entorno-y-ejecucion-manual
description: Skill autónoma de conocimiento sobre entorno, preparación y ejecución de sesiones de prueba manual. No depende de archivos externos.
---

# Entorno y Ejecución de Sesiones de Prueba Manual

## Configuración del Entorno

### 1. Entornos disponibles

```yaml
environments:
  local:
    url: "http://localhost:3000"
    build: "dev"
    datos: "sintéticos"
    uso: "validación rápida del tester"

  qa:
    url: "https://qa.example.com"
    build: "candidato del sprint"
    datos: "semilla + creados en sesión"
    uso: "funcionales, sistema, exploratorias"

  staging:
    url: "https://staging.example.com"
    build: "release candidate"
    datos: "semilla representativa"
    uso: "regresión y UAT"

  preproduccion:
    url: "https://preprod.example.com"
    build: "idéntico a producción"
    datos: "anonimizados de producción"
    uso: "UAT final y validación de despliegue"

  produccion:
    url: "https://app.example.com"
    datos: "reales"
    uso: "SOLO lectura, con aprobación explícita"
```

### 2. Archivo de configuración de la sesión

```yaml
# PRJ-{proyecto}/{ambiente}/Test_Data/session-config.yaml
session:
  environment: qa
  base_url: "https://qa.example.com"
  build: "4.3.0"
  browser: chromium
  viewport: "1440x900"
  mcp_server: playwright
  evidence_dir: "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence"

accounts:
  admin:    { user: "qa.admin",    password_env: "QA_ADMIN_PWD" }
  operador: { user: "qa.oper",     password_env: "QA_OPER_PWD" }
  cliente:  { user: "qa.cliente",  password_env: "QA_CLIENTE_PWD" }

evidence:
  per_step: screenshot
  per_session: [video, trace]
  on_defect: [screenshot, console, network]
```

### 3. Variables de entorno

No guardar credenciales en el repositorio. Referenciar variables de entorno o un gestor de secretos.

## Preparación de la sesión (checklist)

```
[ ] Build desplegado y versión confirmada en la UI
[ ] Entorno accesible desde la máquina del agente
[ ] Cuentas por rol vigentes y desbloqueadas
[ ] Datos semilla cargados o creados
[ ] Entorno en estado conocido (sin datos residuales de otra sesión)
[ ] Servidor MCP playwright habilitado y respondiendo
[ ] Navegador objetivo instalado y en la versión esperada
[ ] Directorio de evidencia existente y escribible
[ ] Casos de prueba y datos de la sesión seleccionados
[ ] Confirmación del usuario para iniciar la sesión
```

## Ejecución

### 1. Secuencia obligatoria

```
Smoke Testing   -> gate: si falla, detener
Sanity Testing  -> sólo si hay un fix que validar
Funcionales     -> cobertura por requisito
Sistema         -> flujos end-to-end
Regresión       -> comparación contra baseline
Exploratorias   -> charters timeboxeados
UAT             -> ejecución/validación del negocio
```

### 2. Arranque de la sesión MCP

```
browser_navigate  -> URL base del entorno confirmado
browser_snapshot  -> verificar render y build desplegado
browser_resize    -> ajustar a la resolución de la matriz
browser_start_video / browser_start_tracing  -> según el tipo de prueba
```

### 3. Cierre de la sesión

```
browser_stop_tracing / browser_stop_video  -> cerrar artefactos
browser_close                              -> cerrar el navegador
```

Y luego, fuera del navegador:
- Adjuntar la evidencia a los casos ejecutados.
- Registrar los defectos en `PRJ-{proyecto}/{ambiente}/Issues&Bugs/{YYYY-MM-DD}/Issues_Bugs_{YYYY-MM-DD}.md`.
- Guardar el resumen de la sesión en `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/`.
- Restaurar o documentar el estado del entorno.

## Captura de resultados

```json
{
  "session_id": "S-20260921-01",
  "environment": "qa",
  "build": "4.3.0",
  "browser": "chromium",
  "start_time": "2026-09-21T09:00:00Z",
  "end_time": "2026-09-21T11:30:00Z",
  "duration_minutes": 150,
  "cases_total": 48,
  "cases_passed": 44,
  "cases_failed": 3,
  "cases_blocked": 1,
  "cases_skipped": 0,
  "pass_rate_pct": 91.7,
  "defects_logged": 3,
  "evidence_files": 112,
  "results_file": "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/S-20260921-01.yaml"
}
```

## Troubleshooting

| Problema | Causa | Solución |
|---|---|---|
| No puedo iniciar sesión | Credenciales caducadas o cuenta bloqueada | Verificar vigencia y desbloquear |
| El entorno no responde | Servicio caído o VPN desconectada | Verificar accesibilidad y escalar |
| No veo el build esperado | Despliegue incompleto o caché del navegador | Confirmar versión en la UI y recargar sin caché |
| Las herramientas `browser_*` fallan | Servidor MCP no disponible | Verificar configuración y reiniciar la sesión |
| Los datos están contaminados | Falta de reset del entorno | Resetear y repetir el caso |
| La sesión expira durante el caso | Timeout corto | Reingresar y continuar desde el paso previo |
| Resultados inconsistentes | Caché, dato preexistente u orden de pasos | Reproducir en condiciones controladas |
| No se puede guardar la evidencia | Ruta inexistente o sin permisos | Verificar el directorio de evidencia |
