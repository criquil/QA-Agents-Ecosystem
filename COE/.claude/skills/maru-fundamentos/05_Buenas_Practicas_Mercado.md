# Buenas Prácticas de Mercado (Nivel 3)

## DAMA-DMBOK — Data Management Body of Knowledge

Conocimiento de gestión de datos. Relevant para COE en la **calidad del dato**
(característica ISO/IEC 25010 para modelos de datos, subcaracterística de integridad).

### Marco DAMA-DMBOK2 (11 Knowledge Areas)

| # | Knowledge Area | Aplicación QA |
|---|---|---|
| 1 | Data & Information Governance | Ownership y custodia del dato |
| 2 | Data Architecture | Modelado, integración |
| 3 | Data Modeling & Analysis | Calidad del esquema |
| 4 | Data Management | Políticas de retención |
| 5 | Data Quality Management | **Dimensiones de calidad del dato** |
| 6 | Data Governance | **Políticas y Standards** |
| 7 | Data Security | Clasificación, cifrado |
| 8 | Data Integration | Contratos de datos |
| 9 | Data Warehouse/BI | Consistencia de reportes |
| 10 | Data Operations | Runbooks, observabilidad |
| 11 | Data & Tech Governance | Ownership de stack |

### Aplicación a QA testing
- Pruebas de **calidad de datos** (accuracy, completeness, consistency) en migraciones y ETLs.
- Contratos de datos = contract testing para integraciones.

## Agile Testing

Marco de Martin Fowler y Kent Beck sobre testing en contextos ágiles.

### Los 4 cuadrantes de Agile Testing

| Cuadrante | Objetivo | Tipo de prueba | Consideración |
|---|---|---|---|
| **Q1** | Apoyar al equipo en el diseño | Unit | Se hace junto al dev, no aparte |
| **Q2** | Verificar que el producto cumple | Functional/E2E | Team-facing, automatizado |
| **Q3** | Explorar y dar feedback | Exploratory | Discovery,Iterations |
| **Q4** | Prevenir problemas futuros | Non-functional (load, security, usability) | Mejora continua |

### Principios ágiles aplicados al testing
- **Testing is not a phase** — continuo e integrado.
- **Automation != testing** — automatización acelera; no sustituye criterio humano.
- **Fast feedback** — cycle feedback corto, Shift-Left.
- Whole-team: QA participa en refinamiento, diseño, code review.

## DevSecOps

Integra seguridad (Sec) dentro de las prácticas Dev + Ops.

### Controles clave para COE QA

| Práctica | Control de calidad |
|---|---|
| SAST (análisis estático) | Code review automático, corrección antes de commit |
| DAST (dinámico) | Vulnerabilidades en runtime |
| SCA (dependencias) | Vulnerabilidades en librerías |
| IAST | Instrumentado en ejecución de tests |
| SBOM | Trazabilidad de dependencias |
| Shift-Left Security | Security testing temprano en pipeline |
| Security Gates | Pipeline bloquea en CVEs críticos |

### Pipeline DevSecOps de referencia
```
commit → SAST → unit tests → build → DAST/IAST → SCA/SBOM → deploy → observability
         ↑ quality gates en cada etapa
```

## Integración de buenas prácticas en gobernanza

| Buena práctica | Estándar ISO que la respalda |
|---|---|
| Agile Testing (cuadrantes) | ISO/IEC 25010 §3.1 functional suitability |
| DevSecOps (security gates) | ISO/IEC 27001 Anexo A §8.25-8.29 |
| DAMA (data quality) | ISO/IEC 25012 modelo de calidad de datos |
| Whole team quality | ISO 9001 §7.2 competencias / §8.3 |

## Referencias
- DAMA-DMBOK2 — Data Management Body of Knowledge, 2ª ed.
- Agile Testing — Martin Fowler, Kent Beck
- DevSecOps — Fundamentals, workflow, and tooling (Humble & Faraco)
- ISO/IEC 25012 — Data quality model
- NIST SP 800-218 — Secure Software Development (SSDF)
