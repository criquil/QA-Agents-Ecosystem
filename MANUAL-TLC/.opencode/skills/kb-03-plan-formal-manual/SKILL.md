---
name: kb-03-plan-formal-manual
description: Skill autónoma de conocimiento sobre el plan formal de pruebas manuales (ieee-829/istqb). No depende de archivos externos.
---

# Plan Formal de Pruebas Manuales (IEEE-829/ISTQB)

## Estructura del Documento

### 1. Introducción
- Alcance del plan y del sistema bajo prueba
- Objetivos de testing
- Referencias (requisitos, historias de usuario, criterios de aceptación, diseño)

### 2. Componentes a Probar
- Módulos y funcionalidades
- Flujos de negocio
- Roles de usuario
- Navegadores y resoluciones de la matriz de compatibilidad
- Integraciones externas

### 3. Funciones a Probar
- **Pruebas Funcionales**: validaciones, reglas de negocio, CRUD por módulo
- **Pruebas de Sistema**: flujos end-to-end y coherencia entre módulos
- **Pruebas de Regresión**: funcionalidad estable previamente validada
- **Smoke Testing**: pantallas y flujos vitales del build
- **Sanity Testing**: el fix puntual y su entorno inmediato
- **Pruebas Exploratorias**: charters de las áreas de mayor riesgo
- **Pruebas de Aceptación (UAT)**: criterios de aceptación del negocio

### 4. Funciones NO a Probar
- Módulos excluidos y su razón (fuera de alcance, deprecados, terceros)
- Tipos de prueba no aplicables y por qué
- Restricciones conocidas (integraciones no provocables, entornos no disponibles)

### 5. Criterios de Prueba
- **Entrada**: build desplegado, entorno estable, cuentas vigentes, datos semilla cargados, MCP operativo
- **Salida**: casos ejecutados ≥ 95%, pass rate ≥ 95%, evidencia completa, sin defectos P1 abiertos, UAT firmada
- **Suspendida**: smoke falla, entorno caído, dato crítico inexistente, sesión MCP no disponible
- **Reanudación**: tras el fix, con un nuevo build y un sanity previo

### 6. Plan de Pruebas
- Cronograma por tipo de prueba y por sesión
- Dependencias (build, datos, disponibilidad del negocio)
- Entregables: casos, evidencia, registro de defectos, reportes

### 7. Requerimientos
- **Ambiente**: local, QA, staging, preproducción (con URL y versión del build)
- **Herramienta**: Playwright MCP Server configurado en el cliente MCP
- **Datos**: catálogo de cuentas por rol y datos semilla
- **Personal**: QA, Test Lead, Product Owner, Dev de soporte
- **Evidencia**: formato, ubicación y política de retención

### 8. Riesgos y Mitigación
- Riesgos identificados en el diagnóstico
- Acciones mitigadoras con responsable y plazo
- Plan de contingencia ante caída del entorno o del MCP

### 9. Aprobaciones
- Firmas y fechas de QA, Product Owner y Tecnología

## NFRs numéricos de referencia

| NFR | Umbral sugerido |
|---|---|
| Carga de pantalla p95 | ≤ 3000 ms |
| Carga de pantalla p99 | ≤ 5000 ms |
| Tasa de error transaccional | ≤ 1% |
| Disponibilidad del entorno | ≥ 99.9% |
| Cobertura de requisitos | 100% |
| Ejecución de casos | ≥ 95% |
| Pass rate | ≥ 95% |
| Evidencia por caso PASS | 100% |
| Defectos P1 abiertos al cierre | 0 |

## Matriz de trazabilidad

| Requisito | Tipo de prueba | Caso | Evidencia esperada |
|---|---|---|---|
| REQ-001 | Funcional | TC-FUNC-001 | screenshot del registro creado |
| REQ-004 | Sistema | TC-SYS-003 | screenshot + correo recibido |
| REQ-004 | Regresión | TC-REG-008 | screenshot + comparación con baseline |
| REQ-009 | UAT | TC-UAT-002 | acta firmada por el negocio |

## Reglas

1. El plan se escribe antes de ejecutar, no después.
2. Los NFRs siempre son numéricos.
3. Cada sección del plan debe ser verificable por un tercero.
4. El plan se versiona junto con los casos de prueba.
5. Al cerrar el ciclo se compara el resultado real contra los criterios de salida declarados aquí.
