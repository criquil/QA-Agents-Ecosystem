# Appium

> **Archivo:** 4 de 4 | **Sección:** Frameworks | **Nivel:** Intermedio-Avanzado

---

## Tabla de Contenidos

1. [Visión General](#visión-general)
2. [Arquitectura](#arquitectura)
3. [Instalación](#instalación)
4. [Ejemplos](#ejemplos)
5. [Plataformas](#plataformas)
6. [Resumen](#resumen)

---

## Visión General

**Appium** es el framework estándar para automatización de testing mobile. Soporta iOS, Android y Windows.

### Características

- ✅ Cross-platform (iOS, Android, Windows)
- ✅ Multi-lenguaje (Java, Python, JS, Ruby)
- ✅ WebDriver protocol
- ✅ No recompilación de apps
- ✅ Testing nativo, híbrido y web

---

## Arquitectura

```
Appium Architecture
├── Appium Server
│   ├── WebDriver Protocol
│   └── JSON Wire Protocol
├── Drivers
│   ├── UiAutomator2 (Android)
│   ├── XCUITest (iOS)
│   └── Espresso (Android)
└── Test Scripts
    ├── Java
    ├── Python
    └── JavaScript
```

---

## Instalación

### Server

```bash
# npm
npm install -g appium

# brew (macOS)
brew install appium

# Iniciar servidor
appium
```

### Drivers

```bash
# Instalar drivers
appium driver install uiautomator2
appium driver install xcuitest

# Listar drivers
appium driver list --installed
```

### Client Libraries

```bash
# Java
<dependency>
    <groupId>io.appium</groupId>
    <artifactId>java-client</artifactId>
    <version>8.6.0</version>
</dependency>

# Python
pip install Appium-Python-Client

# JavaScript
npm install webdriverio
```

---

## Ejemplos

### Java

```java
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;

public class AppiumTest {
    @Test
    public void testLogin() {
        AppiumDriver driver = new AndroidDriver(url, capabilities);
        
        driver.findElement(By.id("email")).sendKeys("user@test.com");
        driver.findElement(By.id("password")).sendKeys("password");
        driver.findElement(By.id("login")).click();
        
        WebElement welcome = driver.findElement(By.id("welcome"));
        assertTrue(welcome.isDisplayed());
    }
}
```

### Python

```python
from appium import webdriver

caps = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:app': 'path/to/app.apk'
}

driver = webdriver.Remote('http://localhost:4723', caps)
driver.find_element('id', 'email').send_keys('user@test.com')
driver.find_element('id', 'login').click()
```

---

## Plataformas

### Android

```java
UiAutomator2Options options = new UiAutomator2Options();
options.setPlatformName("Android");
options.setDeviceName("Pixel 6");
options.setApp("/path/to/app.apk");
```

### iOS

```java
XCUITestOptions options = new XCUITestOptions();
options.setPlatformName("iOS");
options.setDeviceName("iPhone 14");
options.setApp("/path/to/app.app");
```

---

## Resumen

- **Appium** es el estándar para mobile automation
- **Cross-platform** iOS, Android, Windows
- **WebDriver protocol** para compatibilidad
- **No recompilación** de apps

---

## Navegación

- **Anterior:** [03-playwright.md](03-playwright.md)
- **Volver a Frameworks:** [README.md](README.md)
- **Siguiente Sección:** [03-herramientas/](../03-herramientas/README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 4 - Appium*
