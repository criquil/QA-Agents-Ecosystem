# Pirámide de Automatización

> **Archivo:** 2 de 3 | **Sección:** Fundamentos | **Nivel:** Principiante

---

## La Pirámide de Testing

```
        /\
       /  \        ← E2E Tests (pocos, lentos)
      /    \
     / API  \      ← API Tests (medios)
    /        \
   / Unit     \    ← Unit Tests (muchos, rápidos)
  /____________\
```

## Distribución Recomendada

| Nivel | Porcentaje | Velocidad | Costo |
|-------|------------|-----------|-------|
| **Unit Tests** | 60-70% | Muy rápido | Bajo |
| **Integration** | 15-25% | Rápido | Medio |
| **API Tests** | 10-15% | Rápido | Medio |
| **E2E Tests** | 5-10% | Lento | Alto |

## Por Qué Esta Distribución

### Unit Tests (Base Ancha)

- **Velocidad:** Milisegundos
- **Costo:** Bajo
- **Estabilidad:** Alta
- **Código:** Aislado, mocking

### API Tests (Capa Media)

- **Velocidad:** Segundos
- **Costo:** Medio
- **Estabilidad:** Alta
- **Código:** HTTP requests

### E2E Tests (Punta Estrecha)

- **Velocidad:** Minutos
- **Costo:** Alto
- **Estabilidad:** Media
- **Código:** Browser automation

---

## Anti-Pattern: Pirámide Invertida

```
   __________
  /          \
 / E2E Tests  \     ← Muchos tests lentos
/              \
\    API       /    ← Pocos tests
 \            /
  \  Unit    /      ← Casi nada
   \________/
```

### Consecuencias

- Tests lentos
- Flaky tests
- Alto mantenimiento
- Baja confianza

---

## Resumen

- **Pirámide:** Unit (60-70%) → Integration (15-25%) → API (10-15%) → E2E (5-10%)
- **Anti-pattern:** Pirámide invertida (mucho E2E, poco unit)
- **Objetivo:** Base ancha para tests rápidos y estables

---

## Navegación

- **Anterior:** [01-que-es-automatizacion.md](01-que-es-automatizacion.md)
- **Siguiente:** [03-cuando-automatizar.md](03-cuando-automatizar.md)
- **Volver a Fundamentos:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - Pirámide de Automatización*
