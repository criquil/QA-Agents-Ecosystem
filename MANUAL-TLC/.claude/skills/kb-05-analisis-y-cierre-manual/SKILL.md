---
name: kb-05-analisis-y-cierre-manual
description: Skill autónoma de conocimiento sobre análisis y cierre de un ciclo de pruebas manuales. No depende de archivos externos.
---

# Análisis y Cierre de un Ciclo de Pruebas Manuales

## Fase de Análisis

### 1. Recopilación de resultados

```yaml
results:
  execution_summary:
    session_id: "S-20260921-01"
    environment: "qa"
    build: "4.3.0"
    total_cases: 48
    passed: 44
    failed: 3
    blocked: 1
    skipped: 0
    pass_rate: "91.7%"
    execution_time: "150 minutes"
    evidence_files: 112

  by_type:
    smoke:       { total: 8,  passed: 8,  failed: 0 }
    sanity:      { total: 5,  passed: 5,  failed: 0 }
    functional:  { total: 20, passed: 18, failed: 2 }
    system:      { total: 6,  passed: 6,  failed: 0 }
    regression:  { total: 7,  passed: 6,  failed: 1 }
    exploratory: { total: 0,  sessions: 2, findings: 4 }
    uat:         { total: 2,  passed: 1,  failed: 0, conditional: 1 }

  by_priority:
    p1: { total: 20, passed: 20, failed: 0 }
    p2: { total: 18, passed: 16, failed: 2 }
    p3: { total: 10, passed: 8,  failed: 1 }
```

### 2. Análisis de defectos

```yaml
defects:
  - id: "DEF-0341"
    severity: "HIGH"
    priority: "P1"
    module: "Checkout"
    case: "TC-FUNC-012"
    issue: "El cupón del 100% envía total null al confirmar el pedido"
    status: "Open"
    impact: "Pedidos con total nulo en facturación"
    root_cause: "Validación de cupón no contempla el descuento total"

  - id: "DEF-0342"
    severity: "MEDIUM"
    priority: "P2"
    module: "Reportes"
    case: "TC-REG-008"
    issue: "El reporte mensual no muestra el último día del mes"
    status: "Fixed"
    impact: "Faltante de datos en el cierre contable"
    root_cause: "Rango de fechas con límite superior exclusivo"
```

### 3. Métricas de calidad

```markdown
## Cobertura
- Requisitos cubiertos: 34/34 (100%)
- Casos ejecutados: 48/50 (96%)
- Módulos cubiertos: 9/9 (100%)
- Navegadores ejecutados: 3/3 (100%)
- Charters exploratorios ejecutados: 2/2

## Calidad
- Pass rate: 91.7%
- Defectos encontrados: 3
- Defectos P1 abiertos: 1
- Defectos P1 encontrados: 1
- Densidad de defectos por módulo: 0.33

## Evidencia
- Casos PASS con evidencia: 44/44 (100%)
- Archivos de evidencia generados: 112

## Eficiencia
- Duración de la sesión: 150 min
- Casos por hora: 19.2
- Blocked rate: 2.1%
```

## Fase de Cierre

### 1. Checklist de cierre

```yaml
closure_checklist:
  - item: "Todos los casos planificados ejecutados o justificados"
    status: "Complete"
    evidence: "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/S-20260921-01.yaml"

  - item: "Toda la evidencia archivada y nombrada por caso"
    status: "Complete"
    evidence: "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/"

  - item: "Todos los defectos registrados con pasos y evidencia"
    status: "Complete"
    evidence: "PRJ-{proyecto}/{ambiente}/Issues&Bugs/{YYYY-MM-DD}/Issues_Bugs_{YYYY-MM-DD}.md"

  - item: "Causa raíz documentada para los defectos P1"
    status: "Complete"
    evidence: "PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Test_Report_{proyecto}_{ambiente}_{YYYY-MM-DD}.md"

  - item: "UAT firmada o condiciones documentadas"
    status: "Complete"
    evidence: "Acta de aceptación"

  - item: "Entorno restaurado o estado documentado"
    status: "Complete"
    evidence: "Notas de sesión"

  - item: "Lecciones aprendidas registradas"
    status: "Complete"
    evidence: "Retrospectiva del ciclo"

  - item: "Suite de regresión actualizada"
    status: "Complete"
    evidence: "PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/"
```

### 2. Informe final (estructura)

```markdown
# Reporte de Pruebas Manuales - <Sistema> - <Build>

## Resumen Ejecutivo
<2-3 oraciones: qué se probó, resultado global, veredicto>

## Alcance Ejecutado
<navegadores, módulos, tipos de prueba, sesiones>

## Resultados por Tipo de Prueba
<tabla: tipo, casos, pass, fail, blocked, notas>

## Cobertura
<requisitos, casos, módulos, navegadores>

## Defectos
<tabla por severidad y estado; análisis de causa raíz de los P1>

## Pruebas Exploratorias
<charters ejecutados y hallazgos>

## Pruebas de Aceptación (UAT)
<criterios, resultado y firma>

## Riesgos Residuales
<qué queda sin cubrir y su impacto>

## Recomendaciones
<P1/P2/P3 accionables con responsable y plazo>

## Veredicto
PASSED | CONDITIONAL | FAILED + condiciones
```

### 3. Lecciones aprendidas

```markdown
## Qué funcionó bien
- Sesiones asistidas con evidencia completa desde el primer paso
- Gate de smoke evitó ejecutar ciclos sobre builds inestables
- Datos semilla versionados redujeron los BLOCKED

## Qué mejorar
- Mayor variedad de datos límite
- Involucrar al negocio antes en la definición de criterios de aceptación
- Reducir el tamaño de la suite de regresión retirando casos que no aportan

## Acciones
1. Ampliar el catálogo de datos límite por módulo
2. Incorporar al Product Owner al refinamiento de criterios
3. Revisar y depurar la suite de regresión por riesgo
```

### 4. Archivo de artefactos

```yaml
artifacts:
  test_cases:
    location: "PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/"
    version: "1.0"
  test_data:
    location: "PRJ-{proyecto}/{ambiente}/Test_Data/"
    sensitive: false
  evidence:
    location: "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/"
    format: ["PNG", "WEBM", "ZIP", "PDF", "LOG", "JSON"]
    retention: "90 days"
  results:
    location: "PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/"
  reports:
    location: "PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/"
    files: ["Test_Report_{proyecto}_{ambiente}_{YYYY-MM-DD}.md", "Analysis_{YYYY-MM-DD}.md", "RCA_DEF-{NNNN}.md"]
```

## Aprobación Final

| Rol | Nombre | Aprobado | Fecha | Firma |
|-----|--------|----------|-------|-------|
| QA Lead | | ☐ | | |
| Product Owner | | ☐ | | |
| Tech Lead | | ☐ | | |
| Project Manager | | ☐ | | |

## Próximos Pasos

1. Corregir los defectos P1 y re-ejecutar sanity + regresión del módulo.
2. Actualizar la suite de regresión con los casos derivados de los hallazgos exploratorios.
3. Ampliar la matriz de compatibilidad si aparecieron diferencias por navegador.
4. Planificar el siguiente ciclo con los riesgos residuales identificados.
