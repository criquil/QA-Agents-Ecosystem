---
name: kb-01-cicd-y-tendencias-futuras-manual
description: Skill autónoma de conocimiento sobre mejores prácticas y tendencias en pruebas manuales. No depende de archivos externos.
---

# Mejores Prácticas y Tendencias en Pruebas Manuales

## Integración con el Ciclo de Entrega

### Pipeline recomendado

```yaml
stages:
  - desarrolladores: pruebas unitarias e integración
  - qa-smoke: Smoke Testing manual asistido por Playwright MCP
  - qa-funcional: Pruebas Funcionales y de Sistema
  - qa-regresion: Pruebas de Regresión (gate de release)
  - qa-exploratorio: sesiones exploratorias timeboxeadas
  - uat: Pruebas de Aceptación con negocio
  - release: pase a producción
```

### Gates de calidad

- **Merge Gate**: Smoke 100% PASS
- **Deploy Gate a QA**: sin defectos P1 bloqueantes
- **Release Gate**: Regresión sin regresiones P1/P2, evidencia completa
- **Production Gate**: UAT aceptada y firmada

## Mejores Prácticas

### 1. Smoke primero, siempre
Un build que no pasa smoke no merece una sesión funcional. Es el gate más barato del proceso.

### 2. Sanity tras cada fix
Cuando se corrige un defecto puntual, ejecutar un sanity estrecho y profundo antes de devolver el build a regresión completa.

### 3. Casos de prueba como código
- Casos versionados en el repositorio (`PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/`).
- Cambios de casos revisados como un pull request.
- Reutilización de casos en regresión y UAT.

### 4. Evidencia por diseño
No capturar evidencia "si hace falta": definir en el caso qué evidencia se requiere y capturarla en el punto exacto del flujo.

### 5. Exploratorias con disciplina
Charter, timebox y reporte SBTM. Sin charter la sesión no es exploratoria, es improvisación.

### 6. Datos de prueba confiables
Catálogo de cuentas por rol y datos semilla versionados; reset del entorno antes de cada ciclo.

### 7. UAT con el negocio, no por el negocio
El QA facilita y evidencia; el negocio acepta o rechaza.

### 8. Pirámide de esfuerzo manual

```
        /  UAT   \             pocas, de negocio, end-to-end
       / Sistema  \            moderadas, flujos integrados
      / Funcional  \           muchas, por requisito
     / Regresión    \          amplias, repetitivas, deterministas
    / Smoke / Sanity  \        mínimas, por build y por fix
```

## Tendencias Futuras

1. **AI-Assisted Manual Testing** — generación de casos y de datos a partir de requisitos y de la propia UI.
2. **Self-healing selectors** — los snapshots de accesibilidad reducen el mantenimiento de la conducción.
3. **Session-based test management (SBTM)** — gestión de exploratorias por sesiones y cobertura, no por casos.
4. **Accesibilidad como requisito de aceptación** — WCAG 2.1 AA validado manualmente en cada release.
5. **Evidence-driven QA** — todo resultado ligado a evidencia verificable y comparable entre ciclos.
6. **Testing de compatibilidad continua** — matrices automatizadas de navegador, dispositivo y resolución.
7. **Shift-left del testing exploratorio** — sesiones exploratorias tempranas sobre prototipos y features tras feature.
