# Keyword-Driven Testing

> **Archivo:** 2 de 3 | **Sección:** Estrategias | **Nivel:** Intermedio-Avanzado

---

## Definición

**Keyword-Driven Testing** descompone tests en pasos basados en keywords (acciones reutilizables).

## Estructura

```
keywords/
├── actions/
│   ├── login.java
│   └── search.java
├── keywords.json
└── testcases/
    └── login_tests.xlsx
```

## Ejemplo

### Keywords

```json
{
  "login": {
    "action": "performLogin",
    "params": ["email", "password"]
  },
  "verify_dashboard": {
    "action": "verifyElement",
    "params": ["dashboard_title"]
  }
}
```

### Test Case (Excel/CSV)

| Step | Keyword | Params |
|------|---------|--------|
| 1 | open_browser | chrome |
| 2 | navigate | https://example.com |
| 3 | login | user@test.com, pass123 |
| 4 | verify_dashboard | Welcome |

### Executor

```java
public void executeTestCase(TestCase testCase) {
    for (Step step : testCase.getSteps()) {
        Keyword keyword = keywords.get(step.getKeyword());
        keyword.execute(step.getParams());
    }
}
```

## Resumen

- **Keyword-Driven** separa acciones de test cases
- **Reutilización** máxima de keywords
- **No-programadores** pueden crear tests

---

## Navegación

- **Anterior:** [01-data-driven.md](01-data-driven.md)
- **Siguiente:** [03-bdd.md](03-bdd.md)
- **Volver a Estrategias:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - Keyword-Driven Testing*
