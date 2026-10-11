---
name: kb-01-definicion-y-fundamentos-manual
description: Skill autónoma de conocimiento sobre pruebas manuales: definición y fundamentos. No depende de archivos externos.
---

# Pruebas Manuales: Definición y Fundamentos

## ¿Qué son las Pruebas Manuales?

Las pruebas manuales son la verificación del sistema realizada por un humano que interactúa directamente con la aplicación, ejecutando pasos, observando resultados y aplicando criterio para decidir si el comportamiento observado corresponde al esperado.

El valor diferencial del testing manual no está en repetir pasos, sino en el **juicio**: detectar lo inesperado, cuestionar el requisito, evaluar la usabilidad, la accesibilidad y el impacto real en el usuario.

## ¿Por qué se siguen haciendo?

- **Criterio humano**: valida lo que no está escrito (usabilidad, claridad, coherencia visual).
- **Exploración**: descubre defectos que ningún caso anticipó.
- **Costo de diseño**: no todo merece automatizarse.
- **Aceptación**: el negocio debe validar con sus propios ojos.
- **Primera vez**: funcionalidad nueva o inestable se prueba mejor manualmente.

## Tipos de Prueba Manual cubiertos por MANUAL-TLC

1. **Pruebas Funcionales** — Verificación de cada función contra su requisito funcional.
2. **Pruebas de Sistema (System Testing)** — Validación del sistema completo e integrado contra los requisitos de sistema.
3. **Pruebas de Regresión** — Confirmación de que los cambios no rompieron lo que ya funcionaba.
4. **Smoke Testing** — Gate mínimo de aceptación del build: ¿es testeable?
5. **Sanity Testing** — Verificación estrecha y profunda de un fix o cambio puntual.
6. **Pruebas Exploratorias** — Aprendizaje, diseño y ejecución simultáneos guiados por charters.
7. **Pruebas de Aceptación (UAT)** — Validación del negocio contra criterios de aceptación.

## Diferencia con otros tipos de testing

| Aspecto | Pruebas Manuales | Pruebas Automatizadas | Pruebas de Performance |
|---|---|---|---|
| **Ejecutor** | Humano | Máquina | Generador de carga |
| **Fortaleza** | Criterio, exploración, usabilidad | Repetición, velocidad, CI | Escalabilidad y estabilidad |
| **Debilidad** | Lenta, costosa, no repetible al 100% | No detecta lo no anticipado | No valida lógica funcional |
| **Evidencia** | Screenshot, video, traza, observación | Reporte de ejecución | Gráficos de latencia y throughput |
| **Cuándo** | Funcionalidad nueva, UAT, exploración | Regresión amplia y estable | Antes de escalar |

## Niveles de prueba (ISTQB)

```
Unit  ->  Integration  ->  System  ->  Acceptance
                                 \-> UAT (validación de negocio)
```

Las pruebas manuales son protagonistas en **System** y **Acceptance**, y aportan valor en **Integration** cuando el flujo cruza servicios visibles al usuario.

## Estándares y Frameworks

- **ISTQB** — Fundamentos, niveles, tipos y proceso de testing.
- **IEEE 829** — Documentación de pruebas (plan, diseño, caso, procedimiento, reporte).
- **ISO/IEC 25010** — Modelo de calidad de producto (usabilidad, fiabilidad, eficiencia, seguridad, mantenibilidad, portabilidad).
- **WCAG 2.1** — Pautas de accesibilidad web (nivel AA como referencia habitual).
- **SBTM** — Session-Based Test Management para pruebas exploratorias.

## Principios aplicables

1. El testing muestra la presencia de defectos, no su ausencia.
2. El testing exhaustivo es imposible; se prioriza por riesgo.
3. Probar temprano ahorra costo.
4. Los defectos se agrupan: pocas áreas concentran la mayoría.
5. La paradoja del pesticida: repetir el mismo caso deja de encontrar defectos nuevos.
6. El testing depende del contexto.
7. Ausencia de errores no es ausencia de defectos: un sistema sin bugs puede ser inaceptable para el negocio.
