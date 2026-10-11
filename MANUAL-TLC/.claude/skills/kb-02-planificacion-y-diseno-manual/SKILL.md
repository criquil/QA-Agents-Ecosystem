---
name: kb-02-planificacion-y-diseno-manual
description: Skill autónoma de conocimiento sobre planificación y diseño de pruebas manuales. No depende de archivos externos.
---

# Planificación y Diseño de Pruebas Manuales

## Fase de Planificación

### 1. Definición del Alcance
- Módulos, funcionalidades y flujos a probar
- Flujos de negocio críticos y su prioridad
- Dependencias entre módulos y sistemas externos
- Lo que queda FUERA del alcance y por qué
- Restricciones de tiempo, personas y entornos

### 2. Selección de Tipos de Prueba

| Necesidad | Tipo a seleccionar |
|---|---|
| ¿Funciona esta función? | Pruebas Funcionales |
| ¿Funciona el sistema completo? | Pruebas de Sistema |
| ¿Rompimos algo? | Pruebas de Regresión |
| ¿Es testeable este build? | Smoke Testing |
| ¿Funciona este fix puntual? | Sanity Testing |
| ¿Qué se nos escapa? | Pruebas Exploratorias |
| ¿Lo acepta el negocio? | Pruebas de Aceptación (UAT) |

### 3. Diseño de Casos

Para cada módulo o flujo:
- Precondiciones explícitas (entorno, build, rol, datos)
- Pasos numerados y accionables en la UI
- Resultado esperado observable
- Datos de prueba concretos
- Evidencia requerida
- Prioridad P1/P2/P3

Estructura de un caso:

```
TC-<TIPO>-<n>: <título>
Tipo        : funcional | sistema | regresión | smoke | sanity | exploratoria | uat
Prioridad   : P1 | P2 | P3
Precondición: <build, entorno, navegador, rol, datos>
Datos       : <valores exactos>
Pasos       : 1) ...  2) ...  3) ...
Resultado   : <observable por el usuario>
Evidencia   : <screenshot / PDF / video>
Trazabilidad: <ID del requisito>
```

### 4. Estrategia de Datos
- Catálogo de cuentas por rol
- Datos semilla y datos creados en la sesión
- Datos límite y de caracteres especiales
- Datos de UAT provistos por el negocio
- Plan de reset y de cleanup

### 5. Orden de Ejecución
1. Smoke Testing
2. Sanity Testing (si hay un fix que validar)
3. Pruebas Funcionales
4. Pruebas de Sistema
5. Pruebas de Regresión
6. Pruebas Exploratorias
7. Pruebas de Aceptación (UAT)

### 6. Estimación

```
Estimación = (casos_a_ejecutar × tiempo_medio_por_caso)
           + preparación/limpieza de datos
           + navegación y cambio de contexto
           + gestión de defectos y evidencia
           + reseñas y coordinación de UAT
```

## Entregables

- Plan de procedimiento documentado
- Matriz de cobertura módulo/flujo × tipo de prueba
- Casos de prueba detallados en `PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/`
- Catálogo de datos y cuentas en `PRJ-{proyecto}/{ambiente}/Test_Data/`
- Estimación de esfuerzo y cronograma de sesiones
- Definición del esquema de evidencia

## Errores frecuentes de planificación

1. Planificar sólo el happy path.
2. Omitir el smoke como gate.
3. No definir los datos de prueba antes de la sesión.
4. Sobredimensionar la cobertura y no alcanzar la profundidad.
5. No reservar tiempo para la gestión de defectos y evidencia.
6. No incluir al negocio en la planificación de UAT.
