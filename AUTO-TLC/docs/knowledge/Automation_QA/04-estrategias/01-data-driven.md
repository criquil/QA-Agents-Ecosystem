# Data-Driven Testing

> **Archivo:** 1 de 3 | **Sección:** Estrategias | **Nivel:** Intermedio

---

## Definición

**Data-Driven Testing** ejecuta el mismo test con múltiples conjuntos de datos, separando lógica de datos.

## Beneficios

- ✅ Un solo test para múltiples escenarios
- ✅ Fácil agregar nuevos datos
- ✅ Mantenimiento reducido
- ✅ Cobertura amplia

## Ejemplo Java (TestNG)

### Datos

```java
@DataProvider(name = "loginData")
public Object[][] loginData() {
    return new Object[][] {
        {"user1@test.com", "pass1", true},
        {"user2@test.com", "pass2", true},
        {"invalid@test.com", "wrong", false}
    };
}
```

### Test

```java
@Test(dataProvider = "loginData")
void testLogin(String email, String password, boolean expected) {
    loginPage.login(email, password);
    
    if (expected) {
        assertTrue(dashboard.isDisplayed());
    } else {
        assertTrue(loginPage.isErrorDisplayed());
    }
}
```

## Ejemplo Python (pytest)

### Datos

```python
@pytest.mark.parametrize("email, password, expected", [
    ("user1@test.com", "pass1", True),
    ("user2@test.com", "pass2", True),
    ("invalid@test.com", "wrong", False)
])
def test_login(email, password, expected):
    login_page.login(email, password)
    
    if expected:
        assert dashboard.is_displayed()
    else:
        assert login_page.is_error_displayed()
```

## Resumen

- **Data-Driven** separa datos de lógica
- **Múltiples escenarios** con un solo test
- **Fácil mantenimiento** y escalabilidad

---

## Navegación

- **Anterior:** [README.md](README.md)
- **Siguiente:** [02-keyword-driven.md](02-keyword-driven.md)
- **Volver a Estrategias:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 1 - Data-Driven Testing*
