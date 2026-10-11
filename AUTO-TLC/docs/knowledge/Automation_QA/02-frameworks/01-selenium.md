# Selenium

> **Archivo:** 1 de 4 | **Sección:** Frameworks | **Nivel:** Intermedio

---

## Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Arquitectura](#arquitectura)
3. [Instalación](#instalación)
4. [Ejemplos Básicos](#ejemplos-básicos)
5. [WebDriver API](#webdriver-api)
6. [Esperas (Waits)](#esperas-waits)
7. [Mejores Prácticas](#mejores-prácticas)
8. [Resumen](#resumen)

---

## Visión General

**Selenium** es el framework de automatización web más maduro y ampliamente utilizado. Soporta múltiples lenguajes de programación y navegadores.

### Características

- ✅ Multi-browser (Chrome, Firefox, Safari, Edge)
- ✅ Multi-lenguaje (Java, Python, C#, JavaScript)
- ✅ W3C Standard
- ✅ Gran comunidad y ecosistema
- ✅ Selenium Grid para ejecución distribuida

---

## Arquitectura

```
Selenium Architecture
├── WebDriver (API)
│   ├── ChromeDriver
│   ├── GeckoDriver
│   └── EdgeDriver
├── Selenium Grid
│   ├── Hub (coordinator)
│   └── Node (executors)
└── Test Runner
    ├── TestNG
    ├── JUnit
    └── pytest
```

---

## Instalación

### Java

```xml
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.15.0</version>
</dependency>
```

### Python

```bash
pip install selenium
```

### JavaScript

```bash
npm install selenium-webdriver
```

---

## Ejemplos Básicos

### Java

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class SeleniumTest {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        
        driver.get("https://example.com");
        System.out.println(driver.getTitle());
        
        driver.quit();
    }
}
```

### Python

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

---

## WebDriver API

### Acciones Comunes

```java
// Navegación
driver.get("https://example.com");
driver.navigate().back();
driver.navigate().forward();
driver.navigate().refresh();

// Elementos
WebElement element = driver.findElement(By.id("myId"));
element.click();
element.sendKeys("text");
element.clear();
element.getText();
element.getAttribute("href");
element.isDisplayed();
element.isEnabled();

// Select dropdown
Select select = new Select(driver.findElement(By.id("mySelect")));
select.selectByVisibleText("Option 1");
select.selectByValue("option1");
```

---

## Esperas (Waits)

### Implicit Wait

```java
driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
```

### Explicit Wait

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement element = wait.until(
    ExpectedConditions.visibilityOfElementLocated(By.id("myId"))
);
```

### Fluent Wait

```java
FluentWait<WebDriver> wait = new FluentWait<>(driver)
    .withTimeout(Duration.ofSeconds(30))
    .pollingEvery(Duration.ofSeconds(2))
    .ignoring(NoSuchElementException.class);
```

---

## Mejores Prácticas

```
✅ Usar Page Object Model
✅ No hardcodear datos
✅ Usar waits explícitos
✅ Manejar excepciones
✅ Cleanup después de tests
✅ Usar Selenium Grid para parallel
```

---

## Resumen

- **Selenium** es el estándar para web automation
- **Multi-browser y multi-lenguaje**
- **WebDriver API** para interacción
- **Waits** para manejar asincronía
- **Page Object Model** para mantenibilidad

---

## Navegación

- **Anterior:** [README.md](README.md)
- **Siguiente:** [02-cypress.md](02-cypress.md)
- **Volver a Frameworks:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 1 - Selenium*
