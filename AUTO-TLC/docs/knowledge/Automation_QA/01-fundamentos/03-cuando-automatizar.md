# Cuándo Automatizar

> **Archivo:** 3 de 3 | **Sección:** Fundamentos | **Nivel:** Principiante-Intermedio

---

## Tabla de Decisión

| Criterio | Automatizar | No Automatizar |
|----------|-------------|----------------|
| **Frecuencia** | Tests repetitivos | Tests únicos |
| **Estabilidad** | Requisitos estables | Requisitos cambiantes |
| **ROI** | Alto retorno | Bajo retorno |
| **Riesgo** | Componentes críticos | Componentes secundarios |
| **Tiempo** | Largo para manual | Rápido para manual |

## Qué Automatizar

### ✅ Sí Automatizar

```
- Smoke tests (verificación rápida)
- Regression tests (verificar cambios)
- Data-driven tests (múltiples datos)
- Tests de API (rápidos y estables)
- Tests de integración
- Flujos críticos de negocio
```

### ❌ No Automatizar

```
- Exploratory testing
- Usability testing
- Tests de un solo uso
- Tests con datos muy volátiles
- Tests visuales (sin herramienta especial)
- Tests de exploración inicial
```

## ROI de Automatización

### Fórmula

```
ROI = (Tiempo Manual Ahorrado - Inversión Automatización) / Inversión Automatización
```

### Ejemplo

```
Tiempo manual por ejecución: 2 horas
Frecuencia: 10 veces por semana
Tiempo automatizado: 10 minutos
Inversión inicial: 40 horas

Tiempo manual semanal: 20 horas
Tiempo automatizado semanal: 1.7 horas
Ahorro semanal: 18.3 horas

Payback: 40 / 18.3 = 2.2 semanas
```

---

## Resumen

- **Automatizar:** Tests repetitivos, estables, de alto ROI
- **No automatizar:** Exploratory, usability, un solo uso
- **ROI:** Calcular antes de automatizar
- **Priorizar:** Componentes críticos primero

---

## Navegación

- **Anterior:** [02-piramide-automatizacion.md](02-piramide-automatizacion.md)
- **Volver a Fundamentos:** [README.md](README.md)
- **Siguiente Sección:** [02-frameworks/](../02-frameworks/README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 3 - Cuándo Automatizar*
