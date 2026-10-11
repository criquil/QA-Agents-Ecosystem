# Índice Maestro de Skills — COE Maru

## Cómo usar este índice

- **Nivel 1** (este archivo): catálogo completo de skills disponibles. Consultar primero.
- **Nivel 2** (`SKILL.md`): rol, workflow, reglas y formato de salida de cada skill. Leer antes de invocar.
- **Nivel 3** (`NN_Tema.md`): detalles autoritativos por tema (fórmulas, umbrales, ejemplos). Leer solo la sección necesaria con `grep -n "^## "` + `read offset/limit`.

## Reglas de lectura

- Nunca leer un documento completo si es &gt;2.000 tokens. Usar cheat sheets primero, luego secciones específicas.
- Cada skill con `<pre_execution>` debe cumplir esa sección antes de generar output.
- El contexto acumulado vive en `docs/qa-governance/{plan_id}/context_envelope.json`. No releer lo ya sintetizado.

---

## Skills de Gobernanza

### `maru` — Núcleo del COE
- **Ruta**: `.opencode/skills/maru/SKILL.md`
- **Rol**: Entry point y orquestador. Detecta disciplina, rutea, gestiona estado y formato de salida.
- **Invocar**: SIEMPRE que se inicia un request de gobernanza.

### `maru-fundamentos` — Políticas, normas ISO y certificaciones
- **Ruta**: `.opencode/skills/maru-fundamentos/SKILL.md`
- **Rol**: Define estándares, políticas de calidad, mapeo ISO/Certificaciones, NFRs, KPIs, SLAs.
- **Invocar**: Cuando se necesite una política nueva, una norma ISO o una métrica de calidad.
- **Cheat sheet**: `00_Cheat_Sheet_Fundamentos.md` (leer primero — 9 características ISO/IEC 25010:2023, cláusulas ISO 9001, niveles ISTQB/CMMI/TMMi)
- **Nivel 3**: `01_ISO_IEC_25010_Modelo_de_Calidad.md`, `02_ISO_IEC_29148_Requisitos.md`, `03_Certificaciones_ISTQB_CMMI_TMMi.md`, `04_ISO_9001_ISO_27001.md`, `05_Buenas_Practicas_Mercado.md`

### `maru-api-testing-governance` — API Testing
- **Ruta**: `.opencode/skills/maru-api-testing-governance/SKILL.md`
- **Rol**: Contratos (OpenAPI, Pact), seguridad (OWASP API Security Top 10), cobertura de endpoints, herramientas (Postman, RestAssured, Karate).
- **Invocar**: Cuando se trate de gobernanza de APIs (REST, SOAP, gRPC, GraphQL).

### `maru-manual-testing-governance` — Manual Testing
- **Ruta**: `.opencode/skills/maru-manual-testing-governance/SKILL.md`
- **Rol**: Guiones de prueba, criterios de aceptación, exploración, usabilidad, gestión de bugs.
- **Invocar**: Cuando se trate de estándares de pruebas manuales o revisión de casos de uso.

### `maru-automation-testing-governance` — Automation Testing
- **Ruta**: `.opencode/skills/maru-automation-testing-governance/SKILL.md`
- **Rol**: Frameworks (Selenium, Cypress, Playwright, Appium, Robot), CI/CD, calidad de código de pruebas, manejo de flaky tests.
- **Invocar**: Cuando se trate de estándares de automatización o revisión de suites.

### `maru-performance-testing-governance` — Performance Testing
- **Ruta**: `.opencode/skills/maru-performance-testing-governance/SKILL.md`
- **Rol**: SLAs/SLOs, carga/estrés/escalabilidad, herramientas (k6, JMeter, Gatling, Locust), métricas de rendimiento.
- **Invocar**: Cuando se trate de gobernanza de performance testing o revisión de SLAs.

### `maru-accessibility-testing-governance` — Accessibility Testing
- **Ruta**: `.opencode/skills/maru-accessibility-testing-governance/SKILL.md`
- **Rol**: WCAG 2.1/2.2, pruebas con usuarios reales, herramientas (axe, Lighthouse, WAVE), inclusividad.
- **Invocar**: Cuando se trate de accesibilidad o cumplimiento de estándares de inclusión.

### `maru-test-types` — Catálogo de tipos de prueba
- **Ruta**: `.opencode/skills/maru-test-types/SKILL.md`
- **Rol**: Funcionales, no funcionales, exploratorios, seguridad, compatibilidad, recuperación, contract testing.
- **Invocar**: Cuando haya que decidir o validar qué tipo de prueba aplica.

### `maru-process-quality` — Calidad de procesos del SDLC
- **Ruta**: `.opencode/skills/maru-process-quality/SKILL.md`
- **Rol**: Shift-Left Testing, métricas de proceso, lead time, defect escape rate.
- **Invocar**: Cuando el foco sea el proceso de desarrollo y no una disciplina concreta.

### `maru-audits-reviews` — Revisiones y auditorías
- **Ruta**: `.opencode/skills/maru-audits-reviews/SKILL.md`
- **Rol**: Process reviews, compliance audits, reportes de evidencia, planes CAPA.
- **Invocar**: Cuando se pida una auditoría, revisión de cumplimiento o plan de mejora.

---

## Skills de referencia (Nivel 3 + cheat sheets)

### `maru-metricas-kpis` — Métricas y KPIs
- **Ruta**: `.opencode/skills/maru-metricas-kpis/SKILL.md`
- **Cheat sheet**: `00_Cheat_Sheet_Metricas.md` (fórmulas y umbrales — leer primero)
- **Nivel 3**: `01_Metricas_de_Proceso.md`, `02_Metricas_de_Calidad.md`, `03_Umbrales_y_Criterios.md`

### `maru-workload` — Modelado de carga
- **Ruta**: `.opencode/skills/maru-workload/SKILL.md`
- **Cheat sheet**: `00_Cheat_Sheet_Workload.md` (fórmulas de VU/TPS/think time — leer primero)
- **Nivel 3**: `01_Dimensionamiento.md`, `02_Perfiles_de_Carga.md`

### `maru-herramientas` — Catálogo de herramientas
- **Ruta**: `.opencode/skills/maru-herramientas/SKILL.md`
- **Cheat sheet**: `00b_Cheat_Sheet_Herramientas.md` (matriz de decisión — leer primero)

### `maru-roadmap-decisiones` — Roadmap y decisiones
- **Ruta**: `.opencode/skills/maru-roadmap-decisiones/SKILL.md`
- **PRD**: `PRD.yaml` — requisitos y alcance del COE
- **Roadmap**: `roadmap.yaml` — fases de adopción de estándares
- **ADR**: `decisiones/ADR-NNN_Titulo.md` — decisiones de arquitectura

---

## Habilidades Futuras (pendientes de creación)

- `maru-tools` — pendiente de diseño (parcialmente cubierto por `maru-herramientas`).

---

## Entregables

- `docs/qa-governance/{plan_id}/qa-quality-plan.md`
- `docs/qa-governance/{plan_id}/governance-checklist.md`
- `docs/qa-governance/{plan_id}/audit-report.md`
- `docs/qa-governance/{plan_id}/improvement-plan.md`

---

*Índice maestro — COE Maru — 2026-10-10*