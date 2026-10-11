# Page Object Model

> **Archivo:** 1 de 3 | **Sección:** Herramientas | **Nivel:** Intermedio

---

## Definición

El **Page Object Model (POM)** es un patrón de diseño que crea objetos para cada página de la aplicación, encapsulando los localizadores y acciones.

## Beneficios

- ✅ Separación de UI/Logic
- ✅ Reutilización de código
- ✅ Mantenimiento fácil
- ✅ Código más legible

## Estructura

```
pages/
├── LoginPage.java
├── DashboardPage.java
└── BasePage.java
```

## Ejemplo Java

### Page Object

```java
public class LoginPage {
    private WebDriver driver;
    
    @FindBy(id = "email")
    private WebElement emailField;
    
    @FindBy(id = "password")
    private WebElement passwordField;
    
    @FindBy(id = "login")
    private WebElement loginButton;
    
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }
    
    public void login(String email, String password) {
        emailField.sendKeys(email);
        passwordField.sendKeys(password);
        loginButton.click();
    }
    
    public boolean isErrorDisplayed() {
        return driver.findElement(By.className("error")).isDisplayed();
    }
}
```

### Test

```java
@Test
void shouldLoginSuccessfully() {
    LoginPage loginPage = new LoginPage(driver);
    loginPage.login("user@test.com", "password");
    
    DashboardPage dashboard = new DashboardPage(driver);
    assertTrue(dashboard.isWelcomeDisplayed());
}
```

## Resumen

- **POM** separa UI de lógica de testing
- **Page Objects** encapsulan localizadores y acciones
- **Beneficios:** Mantenimiento, reutilización, legibilidad

---

## Navegación

- **Anterior:** [README.md](README.md)
- **Siguiente:** [02-test-data.md](02-test-data.md)
- **Volver a Herramientas:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 1 - Page Object Model*
