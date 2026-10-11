# Parallelization

> **Archivo:** 2 de 3 | **Sección:** Mejores Prácticas | **Nivel:** Intermedio

---

## Definición

La **paralelización** ejecuta tests simultáneamente para reducir tiempo de ejecución.

## Estrategias

| Estrategia | Descripción | Herramienta |
|------------|-------------|-------------|
| **Test Level** | Tests individuales en paralelo | pytest-xdist |
| **Suite Level** | Suites en paralelo | TestNG |
| **Process Level** | Múltiples procesos | Grid |

## Ejemplo pytest

### Instalación

```bash
pip install pytest-xdist
```

### Ejecución

```bash
# 4 workers en paralelo
pytest -n 4

# Auto-detectar CPUs
pytest -n auto
```

## Ejemplo TestNG

### Configuración

```xml
<suite name="Suite" parallel="tests" thread-count="4">
    <test name="Test1">
        <classes>
            <class name="com.example.Test1"/>
        </classes>
    </test>
    <test name="Test2">
        <classes>
            <class name="com.example.Test2"/>
        </classes>
    </test>
</suite>
```

## Consideraciones

```
✅ Datos de test aislados
✅ No compartir estado entre tests
✅ Usar base de datos por test
✅ Cleanup después de cada test
```

## Resumen

- **Parallelization** reduce tiempo de ejecución
- **Aislamiento** es crítico
- **Herramientas** como pytest-xdist facilitan

---

## Navegación

- **Anterior:** [01-flaky-tests.md](01-flaky-tests.md)
- **Siguiente:** [03-maintenance.md](03-maintenance.md)
- **Volver a Mejores Prácticas:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - Parallelization*
