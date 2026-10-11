# Reporting

> **Archivo:** 3 de 3 | **Sección:** Herramientas | **Nivel:** Intermedio

---

## Definición

El **reporting** genera información sobre resultados de tests para análisis y toma de decisiones.

## Herramientas de Reporte

| Herramienta | Tipo | Lenguaje |
|-------------|------|----------|
| **Allure** | Multi-framework | Java, Python, JS |
| **ExtentReports** | HTML reports | Java |
| **Mochawesome** | HTML reports | JavaScript |
| **ReportPortal** | AI-powered | Multi |

## Allure Report

### Configuración (Java)

```xml
<dependency>
    <groupId>io.qameta.allure</groupId>
    <artifactId>allure-testng</artifactId>
    <version>2.24.0</version>
</dependency>
```

### Ejemplo

```java
@Epic("Login")
@Feature("Authentication")
public class LoginTest {
    
    @Test
    @Story("Successful Login")
    @Severity(SeverityLevel.CRITICAL)
    public void shouldLoginSuccessfully() {
        Allure.step("Enter credentials");
        loginPage.login("user@test.com", "password");
        
        Allure.step("Verify dashboard");
        assertTrue(dashboard.isDisplayed());
    }
}
```

### Generar Reporte

```bash
# Ejecutar con allure
mvn clean test -Dallure.results.directory=target/allure-results

# Generar reporte
allure serve target/allure-results
```

## Resumen

- **Reporting** es esencial para comunicación
- **Allure** es la herramienta estándar
- **Screenshots** y **logs** ayudan al debugging

---

## Navegación

- **Anterior:** [02-test-data.md](02-test-data.md)
- **Volver a Herramientas:** [README.md](README.md)
- **Siguiente Sección:** [04-estrategias/](../04-estrategias/README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 3 - Reporting*
