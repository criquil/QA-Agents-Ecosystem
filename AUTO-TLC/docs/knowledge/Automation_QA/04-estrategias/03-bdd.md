# Behavior-Driven Development (BDD)

> **Archivo:** 3 de 3 | **Sección:** Estrategias | **Nivel:** Intermedio

---

## Definición

**BDD** es una metodología que usa lenguaje natural (Gherkin) para describir comportamiento de software.

## Gherkin Syntax

```gherkin
Feature: Login
  
  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be on the dashboard
    And I should see "Welcome"

  Scenario: Invalid login
    Given I am on the login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message
```

## Herramientas

| Herramienta | Lenguaje | Framework |
|-------------|----------|-----------|
| **Cucumber** | Java, JS | Multiple |
| **SpecFlow** | .NET | NUnit, xUnit |
| **Behave** | Python | pytest |
| **JBehave** | Java | Spring |

## Ejemplo Java (Cucumber)

### Step Definitions

```java
public class LoginSteps {
    
    @Given("I am on the login page")
    public void iAmOnLoginPage() {
        driver.get("https://example.com/login");
    }
    
    @When("I enter valid credentials")
    public void iEnterValidCredentials() {
        driver.findElement(By.id("email")).sendKeys("user@test.com");
        driver.findElement(By.id("password")).sendKeys("password");
    }
    
    @And("I click the login button")
    public void iClickLoginButton() {
        driver.findElement(By.id("login")).click();
    }
    
    @Then("I should be on the dashboard")
    public void iShouldBeOnDashboard() {
        assertTrue(driver.getCurrentUrl().contains("/dashboard"));
    }
}
```

## Resumen

- **BDD** mejora comunicación entre equipos
- **Gherkin** lenguaje legible para todos
- **Living documentation** se genera automáticamente

---

## Navegación

- **Anterior:** [02-keyword-driven.md](02-keyword-driven.md)
- **Volver a Estrategias:** [README.md](README.md)
- **Siguiente Sección:** [05-ci-cd/](../05-ci-cd/README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 3 - Behavior-Driven Development (BDD)*
