---
name: kb-02-roles-y-responsabilidades-manual
description: Skill autónoma de conocimiento sobre roles y responsabilidades en pruebas manuales. No depende de archivos externos.
---

# Roles y Responsabilidades en Pruebas Manuales

## Roles Principales

### 1. Manual Test Engineer (QA Manual)
**Responsabilidades:**
- Diseñar y ejecutar casos de prueba manual
- Conducir sesiones asistidas con el Playwright MCP Server y capturar evidencia
- Reportar defectos con pasos de reproducción y evidencia
- Ejecutar smoke y sanity como gates de cada build
- Colaborar con desarrollo en la reproducción y el análisis

**Habilidades:**
- Criterio de testing: qué probar, cuándo parar, qué es un defecto
- Conocimiento del dominio de negocio
- Lectura de requisitos y detección de ambigüedades
- Manejo de las herramientas de conducción de navegador y de gestión de casos
- Redacción clara de defectos y de evidencia

### 2. Test Lead (QA Lead)
**Responsabilidades:**
- Definir la estrategia de pruebas manuales y la matriz de cobertura
- Planificar ciclos, sesiones y asignación de testers
- Revisar y aprobar casos de prueba
- Decidir el Go/No-Go del release y reportar métricas
- Coordinar la UAT con el negocio

**Habilidades:**
- Liderazgo técnico y gestión de prioridades
- Dominio de ISTQB y de los estándares de documentación
- Análisis de riesgo y estimación
- Comunicación con stakeholders

### 3. Product Owner / Usuario de Negocio
**Responsabilidades:**
- Definir y firmar los criterios de aceptación
- Participar y decidir en la UAT
- Priorizar los defectos según el impacto en el negocio
- Aceptar, aceptar con condiciones o rechazar el sistema

**Habilidades:**
- Conocimiento profundo del proceso de negocio
- Capacidad de decisión sobre el alcance funcional
- Disponibilidad durante la ventana de UAT

### 4. QA Facilitator / Session Facilitator (exploratorio)
**Responsabilidades:**
- Definir charters y timeboxes
- Acompañar y registrar la sesión exploratoria
- Consolidar hallazgos y reportes SBTM
- Convertir hallazgos en defectos y en casos formales

**Habilidades:**
- Dominio de heurísticas de exploración
- Registro en vivo sin perder el hilo de la sesión
- Síntesis y priorización de hallazgos

### 5. Dev / Soporte Técnico
**Responsabilidades:**
- Analizar la causa raíz de los defectos reportados
- Corregir y desplegar los fixes
- Proveer información técnica (logs, trazas, estado de servicios) cuando se solicite
- Mantener los entornos y los datos semilla disponibles

## Responsabilidades por Fase

### Fase 1: Requirements
- **QA Manual**: analizar requisitos funcionales y detectar ambigüedades
- **Product Owner**: priorizar el alcance y anticipar criterios de aceptación
- **Test Lead**: definir alcance y criterios de entrada/salida

### Fase 2: Planning
- **Test Lead**: crear la estrategia y la matriz de cobertura
- **QA Manual**: diseñar casos y definir datos de prueba
- **QA/Soporte**: verificar el readiness del entorno y del MCP

### Fase 3: Design
- **QA Manual**: redactar los casos detallados con evidencia esperada
- **Test Lead**: revisar y aprobar los casos
- **Product Owner**: validar los escenarios de UAT

### Fase 4: Execution
- **QA Manual**: ejecutar smoke, sanity, funcionales, sistema, regresión y exploratorias
- **QA Facilitator**: conducir las sesiones exploratorias y sus reportes
- **Product Owner**: ejecutar o conducir la UAT
- **Test Lead**: monitorear progreso, bloqueos y calidad de la evidencia

### Fase 5: Analysis
- **QA Manual**: analizar los defectos y proponer causas raíz
- **Test Lead**: consolidar métricas y el veredicto
- **Product Owner**: decidir la aceptación final

### Fase 6: Closure
- **Test Lead**: generar el reporte final y las lecciones aprendidas
- **QA Manual**: archivar casos, evidencia y datos
- **Todo el equipo**: revisar la regresión y actualizar la suite

## Mapas de responsabilidad (RACI)

| Actividad | Test Lead | QA Manual | Product Owner | Dev |
|---|---|---|---|---|
| Estrategia de pruebas | R/A | C | C | I |
| Diseño de casos | A | R | C | I |
| Smoke y sanity | I | R | I | C |
| Funcionales y sistema | I | R | C | C |
| Regresión | A | R | I | C |
| Exploratorias | A | R | I | C |
| UAT | A | C | R | I |
| Reporte y veredicto | R/A | C | C | I |
| Fix de defectos | I | C | I | R |

## Herramientas por Rol

| Rol | Herramientas principales |
|---|---|
| QA Manual | Playwright MCP Server, gestor de casos y defectos, catálogo de datos |
| Test Lead | Gestor de casos y ciclos, tablero de métricas, repositorio de evidencia |
| Product Owner | Criterios de aceptación, gestor de defectos, entorno de UAT |
| QA Facilitator | Plantillas de charter y SBTM, cronómetro, captura de evidencia |

## Mejores Prácticas

1. **Colaboración temprana**: QA desde el refinamiento del requisito.
2. **Criterios de aceptación antes de ejecutar**: nunca después.
3. **Trazabilidad**: cada caso ligado a un requisito y a su evidencia.
4. **Reporte consistente**: mismas métricas en todos los ciclos.
5. **Mejora continua**: retrospectiva por ciclo y ajuste de la suite de regresión.
