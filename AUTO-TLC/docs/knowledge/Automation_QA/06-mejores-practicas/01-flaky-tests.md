# Flaky Tests

> **Archivo:** 1 de 3 | **Sección:** Mejores Prácticas | **Nivel:** Intermedio

---

## Definición

**Flaky tests** son tests que pasan y fallan intermitentemente sin cambios en el código.

## Causas Comunes

| Causa | Solución |
|-------|----------|
| **Timing issues** | Usar waits explícitos |
| **Dependencia de datos** | Data factory, cleanup |
| **Dependencia de red** | Mock, retry |
| **Estado compartido** | Tests aislados |
| **Recursos externos** | Mock, stubs |

## Estrategias

### 1. Retry

```java
@Test(retryAnalyzer = RetryAnalyzer.class)
public void testWithRetry() {
    // Test que puede fallar intermitentemente
}
```

### 2. Explicit Waits

```java
// ❌ Mal
Thread.sleep(5000);

// ✅ Bien
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
wait.until(ExpectedConditions.visibilityOf(element));
```

### 3. Test Isolation

```java
@BeforeEach
void setUp() {
    // Crear datos frescos para cada test
    testData = createFreshTestData();
}

@AfterEach
void tearDown() {
    // Limpiar después de cada test
    cleanupTestData();
}
```

## Resumen

- **Flaky tests** reducen confianza
- **Timing** es la causa más común
- **Isolation** y **retry** ayudan

---

## Navegación

- **Anterior:** [README.md](README.md)
- **Siguiente:** [02-parallelization.md](02-parallelization.md)
- **Volver a Mejores Prácticas:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 1 - Flaky Tests*
