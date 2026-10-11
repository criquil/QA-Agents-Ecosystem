---
name: automation-cicd
description: "Integracion de la suite de automatizacion con pipelines CI/CD: stages por tags, GitHub Actions, gestion de artefactos, reintentos y reportes. Invocar al conectar la suite a un pipeline o cuando los tests no corren en CI."
---

# Automation CI/CD — Pipelines

> **Principio**: cada stage del pipeline es un filtro de tags. Sin tags, el stage no ejecuta nada.

## Stages tipicos

```
1. smoke          cada commit       @smoke and not @slow
2. regression     nightly           @regression and not @slow
3. critical gate  pre-deploy        @critical and @prod
4. por funcion    deploy parcial    @<funcionalidad> and @prod
```

## GitHub Actions — esqueleto

```yaml
name: e2e

on:
  push:
    branches: [main]
  schedule:
    - cron: "0 3 * * *"        # regresion nightly

jobs:
  smoke:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npx playwright install --with-deps chromium
      - run: npx playwright test --grep "@smoke and not @slow"
        env:
          QA_ENV: qa
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: report-smoke
          path: reports/

  regression:
    needs: smoke                # no seguir si el smoke falla
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
      fail-fast: false          # ver todos los browsers, no cortar en el primero
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test --project=${{ matrix.browser }} --grep "@qa and not @slow"
        env: { QA_ENV: qa }
```

## Jenkins — esqueleto

```groovy
pipeline {
  agent any
  stages {
    stage('Smoke') {
      steps { sh 'npx playwright test --grep "@smoke and not @slow"' }
    }
    stage('Regresion QA') {
      when { branch 'main' }
      parallel {
        stage('Chromium') { steps { sh 'npx playwright test --project=chromium --grep "@qa"' } }
        stage('Firefox')  { steps { sh 'npx playwright test --project=firefox  --grep "@qa"' } }
      }
    }
    stage('Gate Produccion') {
      steps { sh 'npx playwright test --grep "@critical and @prod"' }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
    }
  }
}
```

## Buenas practicas

### Secretos

- Credenciales por gestor de secretos o secrets del CI. **Nunca** en el repo ni en `data/` versionado.
- El test lee de variable de entorno; `data/config.yaml` define la estructura, no el secreto.

### Ejecucion

| Practica | Motivo |
|---|---|
| `fail-fast: false` en matrices | Ver todos los browsers, no solo el primero que falla |
| Stage de smoke como precondicion | No gastar minutos de regresion si el camino critico esta roto |
| `npx playwright install --with-deps` | Evitar fallos de librerias del sistema |
| Variables de entorno para el ambiente | Un test no decide donde corre |

### Artefactos y evidencia

Subir **siempre**, incluso en fallo:

| Artefacto | Cuando | Por que |
|---|---|---|
| Reporte HTML | `if: always()` | Diagnostico |
| Screenshots | `if: failure()` | Evidencia visual del fallo |
| Video | solo `@critical` | Costo alto, se reserva al camino critico |
| Trace | `if: retry` | Debug fino de un fallo concreto |
| Logs de ejecucion | `if: always()` | Contexto de ambiente |

Activar video y screenshots siempre genera ~4 MB y +3-5 s por test. En smoke eso es overhead puro:
deshabilitalos y guardalos para los tags caros.

### Reintentos

```typescript
// playwright.config.ts
export default defineConfig({
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 4 : undefined,
  reporter: [
    ['html', { outputFolder: 'reports/', open: 'never' }],
    ['junit', { outputFile: 'reports/junit.xml' }],
    ['json',  { outputFile: 'reports/results.json' }]
  ],
  use: {
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
    video: 'retain-on-failure'
  }
});
```

Reintentos en local = 0, para ver el fallo real. Reintentos en CI = 2, para tolerar ruido de red.

> **Regla de higiene**: si un test necesita siempre 2 reintentos para pasar, es **flaky**, no es ruido.
> Ve a `.opencode/skills/automation-troubleshooting/SKILL.md`.

## Diagnostico: los tests no corren en CI

| Sintoma | Causa probable | Verificacion |
|---|---|---|
| Ningun test se ejecuta | Tags faltantes o mal escritos | `--grep "<tag>" --list` |
| Corren en el ambiente equivocado | Falta `@environment` | Revisar filtro del stage |
| Falla solo en CI | Timeout menor, o datos no disponibles | Comparar timeouts con `config.yaml` |
| Falla en un browser especifico | Fecha, locale o zona horaria | Fijar locale y timezone en `use` |
| Falla por permisos | Secrets no inyectados | Revisar secrets del pipeline |
| No encuentra datos | Path relativo distinto en CI | Usar path absoluto desde el repo root |

## Checklist de integracion

- [ ] Cada stage tiene un filtro de tags explicito
- [ ] Smoke corre en cada commit y es rapido
- [ ] Stage de smoke bloquea a los siguientes
- [ ] Secretos vienen del gestor, no del repo
- [ ] Artefactos suben con `if: always()`
- [ ] Video y screenshots no se activan en smoke
- [ ] `retries` activo solo en CI
- [ ] Variables de entorno para la seleccion de ambiente
- [ ] Verificado con `--list` que cada filtro encuentra tests

## Lectura bajo demanda

Este SKILL.md ya trae los eskeletos de GitHub Actions y Jenkins, y la tabla de diagnostico.

| Si el SKILL.md no alcanza y necesitás | Leé |
|---|---|
| Pipelines, Docker y reportes en CI | `docs/knowledge/Automation_QA/05-ci-cd/` |
| Sintaxis exacta de un filtro por tags | `.opencode/skills/automation-tagging/SKILL.md` |

Localiza la seccion antes de leer: `grep -n "^## " <archivo>`

**Stop**: los eskeletos cubren el caso comun. Adaptá la estructura, no busques mas.

---

*Automation CI/CD — cada stage es un filtro de tags. Platform: OpenCode.*