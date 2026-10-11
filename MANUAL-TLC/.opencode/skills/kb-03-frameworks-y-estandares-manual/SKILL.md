---
name: kb-03-frameworks-y-estandares-manual
description: Skill autónoma de conocimiento sobre frameworks y estándares aplicables al testing manual (ISTQB, IEEE-829, ISO 25010, WCAG). No depende de archivos externos.
---

# Frameworks y Estándares en Pruebas Manuales

## Visión General

Las pruebas manuales se apoyan en estándares internacionales que dan estructura, trazabilidad y credibilidad al trabajo del tester. Este documento describe los principales marcos y estándares aplicables.

---

## Estándares Internacionales

### ISTQB (International Software Testing Qualifications Board)

**Fundamentos aplicados:**
- **Niveles de testing**: Unit → Integration → System → Acceptance
- **Tipos de testing**: Functional, Non-functional, Regression, Maintenance, Confirmation
- **Proceso de testing**: Plan → Design → Implementation → Execution → Closure
- **Principios**: el testing muestra defectos, no su ausencia; no es exhaustivo; se prioriza por riesgo; los defectos se agrupan; la paradoja del pesticida; el testing depende del contexto; ausencia de errores no es ausencia de defectos.

**Certificaciones relevantes:**

| Certificación | Enfoque | Relevancia |
|---|---|---|
| ISTQB Foundation Level | Fundamentos generales | Alta |
| ISTQB Advanced - Test Analyst | Diseño de pruebas y análisis | Muy Alta |
| ISTQB Advanced - Test Manager | Gestión de pruebas y equipos | Alta |
| ISTQB Expert - Improving the Test Process | Mejora de proceso | Media |

### IEEE 829 — Standard for Software Test Documentation

| Documento | Contenido |
|---|---|
| Test Plan | Alcance, recursos, cronograma, criterios |
| Test Design | Criterios y técnicas de diseño |
| Test Case | Especificación del caso (precondiciones, pasos, resultado esperado) |
| Test Procedure | Secuencia de ejecución de los casos |
| Test Report | Resultados, métricas y análisis |

### ISO/IEC 25010 — Modelo de Calidad de Producto

Características verificables manualmente:
- **Adecuación funcional**: completitud, corrección, pertinencia
- **Eficiencia de desempeño**: comportamiento temporal, utilización de recursos
- **Compatibilidad**: coexistencia, interoperabilidad
- **Usabilidad**: reconocibilidad, aprendibilidad, operabilidad, protección contra errores, estética, accesibilidad
- **Fiabilidad**: madurez, disponibilidad, tolerancia a fallos, recuperabilidad
- **Seguridad**: confidencialidad, integridad, no repudio, responsabilidad, autenticidad
- **Mantenibilidad**: modularidad, reusabilidad, analizabilidad, modificabilidad, testabilidad
- **Portabilidad**: adaptabilidad, instalabilidad, reemplazabilidad

### WCAG 2.1 — Accesibilidad Web

Verificación manual de los cuatro principios POUR:

| Principio | Verificación manual |
|---|---|
| **Perceptible** | Contraste suficiente, texto alternativo en imágenes, no depender sólo del color |
| **Operable** | Navegación completa por teclado, foco visible, sin trampas de foco |
| **Comprensible** | Lenguaje claro, etiquetas correctas, errores identificados y sugeridos |
| **Robusto** | Compatibilidad con lector de pantalla y tecnologías de asistencia |

---

## Estándares de Documentación de Casos

### Plantilla de caso de prueba

```markdown
### TC-<TIPO>-<n>: <título>

| Campo | Valor |
|---|---|
| Tipo | funcional / sistema / regresión / smoke / sanity / exploratoria / uat |
| Prioridad | P1 / P2 / P3 |
| Trazabilidad | REQ-xxx / AC-xxx |
| Precondiciones | build, entorno, navegador, rol, datos |
| Datos de prueba | valores exactos |

**Pasos**
1. ...
2. ...

**Resultado esperado**
...

**Evidencia requerida**
screenshot / PDF / video / correo

**Resultado obtenido**
PASS / FAIL / BLOCKED / SKIPPED + evidencia + notas
```

---

## Mejores Prácticas

### 1. Pirámide del esfuerzo manual

```
        /   UAT    \          pocas, de negocio, end-to-end
       /  Sistema   \         moderadas, flujos integrados
      /  Funcional   \        muchas, por requisito
     /   Regresión    \       amplias, repetitivas, deterministas
    / Smoke y Sanity    \     mínimas, por build y por fix
    \  Exploratorias     /    sesiones timeboxeadas dirigidas por charter
```

### 2. Trazabilidad bidireccional
Requisito → caso → evidencia → defecto, y a la inversa. Permite responder "¿qué cubre esto?" y "¿qué se probó para este requisito?".

### 3. Gestión de datos de prueba
Catálogo de cuentas y datos semilla versionados; reset del entorno antes de cada ciclo.

### 4. Evidencia como artefacto de primera clase
Formato, naming y ubicación definidos antes de ejecutar.

### 5. Cierre con lecciones aprendidas
Retrospectiva por ciclo y actualización de la suite de regresión.

---

## Métricas de Calidad del Proceso de Testing

| Métrica | Fórmula | Meta |
|---|---|---|
| Requirement Coverage | requisitos_con_caso / total | 100% |
| Case Execution Coverage | ejecutados / diseñados | ≥ 95% |
| Pass Rate | pass / ejecutados | ≥ 95% |
| Defect Detection Effectiveness | defectos_válidos / reportados | ≥ 90% |
| Reopen Rate | reabiertos / cerrados | ≤ 10% |
| Evidence Completeness | casos_pass_con_evidencia / pass | 100% |
| Escape Rate | defectos_en_producción / total | ≤ 10% |

---

## Herramientas de Soporte

### Conducción y evidencia
- **Playwright MCP Server**: herramienta única de MANUAL-TLC v1.0.
- **Playwright CLI**: alternativa para flujos muy repetitivos.

### Gestión de casos y defectos
- TestRail, Zephyr, Xray, TestLink, Jira, hojas de cálculo.

### Accesibilidad
- Herramientas de contraste y auditores automáticos como apoyo, nunca como sustituto de la verificación manual.
