# Element Locator Strategy

> **NOTA**: Esta sección es de **PRIORIDAD** y **REQUERIDA** para crear o modificar tests automatizados.

---

When defining locators in Page Objects, prioritize **robust, readable, and resilient** selectors that resist changes. The main strategy is to use **XPath based on unique and stable attributes**.

To fix selectors that don't work:
1. Start the **Playwright MCP Server** and navigate to the involved section.
2. Use **Chrome DevTools MCP** to capture the selector following the rules.

---

## 🎯 Main Strategy: XPath with Priority Attributes

### Always use XPath when possible.

### 🥇 1. XPath with `id` (Highest Priority)
- **Advantage**: Unique, fast, and reliable.
- **Strategy**: Use XPath with the `id` attribute.
- **Examples**:
```javascript
// Element with specific id
page.locator('xpath=//*[@id="login-button"]');

// Descendant of element with id
page.locator('xpath=//*[@id="form-container"]//button');

// Combined with element type
page.locator('xpath=//input[@id="email-input"]');
```

### 🥈 2. XPath with `name` (Second Priority)
- **Advantage**: Useful in forms and input fields, especially when there's no `id`.
- **Strategy**: Use XPath with the `name` attribute.
- **Examples**:
```javascript
// Form field by name
page.locator('xpath=//*[@name="email"]');

// Specific input by type and name
page.locator('xpath=//input[@name="password" and @type="password"]');

// Inside a form with id
page.locator('xpath=//*[@id="login-form"]//*[@name="username"]');
```

### 🥉 3. XPath with `data-testid` or custom `data-*` attributes
- **Advantage**: Specifically designed for tests, doesn't affect UI.
- **Strategy**: Use XPath with `data-*` attributes.
- **Examples**:
```javascript
// Using data-testid
page.locator('xpath=//*[@data-testid="submit-form"]');

// Using custom data-* attributes
page.locator('xpath=//*[@data-action="confirm"]');

// Combined with context
page.locator('xpath=//*[@id="modal"]//*[@data-testid="close-button"]');
```

### 🏷️ 4. XPath with Accessibility (ARIA roles, accessible labels)
- **Advantage**: Improves accessibility and semantics; ideal for inclusive apps.
- **Strategy**: Use XPath with ARIA attributes.
- **Examples**:
```javascript
// By role and aria-label
page.locator('xpath=//button[@role="button" and @aria-label="Submit"]');

// By aria-describedby
page.locator('xpath=//*[@aria-describedby="help-text"]');

// By aria-expanded
page.locator('xpath=//*[@aria-expanded="true"]');
```

### 📝 5. XPath with Visible Text (only if unique and stable)
- **Advantage**: Readable and direct.
- **Risk**: Fragile against language or content changes.
- **Strategy**: Use XPath with text functions, preferably combined with context.
- **Examples**:
```javascript
// Exact text
page.locator('xpath=//button[text()="Accept"]');

// Contained text
page.locator('xpath=//span[contains(text(), "terms and conditions")]');

// Normalized text (removes spaces)
page.locator('xpath=//div[normalize-space()="Success message"]');

// Combined with context
page.locator('xpath=//*[@id="modal"]//button[text()="Confirm"]');
```

### 🎨 6. XPath with `class` (only if unique and not dynamically generated)
- **Advantage**: Useful when there are no better options.
- **Risk**: May change with design or CSS frameworks.
- **Strategy**: Use XPath with `class`, preferably combined with other attributes.
- **Examples**:
```javascript
// By specific class
page.locator('xpath=//*[@class="btn-confirm"]');

// Class contains (for multiple classes)
page.locator('xpath=//*[contains(@class, "btn-primary")]');

// Combined with element type
page.locator('xpath=//button[contains(@class, "submit")]');

// Combined with context and other attributes
page.locator('xpath=//*[@id="form"]//input[contains(@class, "input-field") and @type="text"]');
```

### ⚙️ 7. Complex XPath (last resort)
- **Advantage**: Extremely flexible.
- **Risk**: May be fragile against structural changes.
- **Strategy**: Build from unique elements and use logical relationships.
- **Examples**:
```javascript
// Navigation by structure
page.locator('xpath=//*[@id="container"]//div[@class="row"][2]/span');

// Next sibling element
page.locator('xpath=//*[@id="label"]/following-sibling::input');

// Parent element
page.locator('xpath=//*[@name="email"]/parent::div');

// Logical combinations (AND, OR)
page.locator('xpath=//button[@type="submit" and contains(@class, "primary")]');
page.locator('xpath=//*[@id="btn-save" or @name="save-button"]');

// Ancestor with condition
page.locator('xpath=//input[@name="city"]/ancestor::form[@id="address-form"]');
```

---

## 🎓 XPath Best Practices

### ✅ DO:
- Use unique attributes (`id`, `name`, `data-*`) as anchors
- Build relative XPath from stable elements
- Combine multiple attributes for greater specificity
- Use text functions with normalization when necessary
- Keep XPath as short and simple as possible
- **ALWAYS validate selectors with Chrome DevTools MCP** before using them
- Never "invent" or use selectors that haven't been validated with Chrome DevTools MCP
- If a selector doesn't work, use MCP Server to navigate and Chrome DevTools MCP to recapture it

### ❌ AVOID:
- Absolute XPath from DOM root: `/html/body/div[1]/div[2]/span[3]`
- Selectors based solely on position without context: `//div[5]/span[2]`
- Relying on visual styles: `//*[@class="active"]` (without additional context)
- Ambiguous partial text that could repeat
- Extremely long XPath with many nesting levels
- Using dynamically generated selectors that change frequently
- Using selectors that haven't been validated with Chrome DevTools MCP

---

## 🔧 Recommended Pattern

```javascript
// General recommended pattern:
// 1. Locate unique container (by id, data-*, etc.)
// 2. Navigate to desired element using relationships and attributes

// Ideal example:
page.locator('xpath=//*[@id="user-form"]//input[@name="email"]');

// Example with multiple conditions:
page.locator('xpath=//*[@data-testid="modal"]//button[@type="submit" and contains(text(), "Save")]');
```

---

## 🚫 Anti-Patterns to Avoid:
- Selectors based solely on position: `//div[3]/span[2]`
- Absolute XPath without anchoring: `/html/body/div/div/div/button`
- Exclusive reliance on styles: `//*[@class="active highlight"]` (without context)
- Ambiguous text without context: `//span[text()="OK"]`
- Using dynamically generated selectors that change frequently
- Using selectors that haven't been validated with Chrome DevTools MCP

---

## 🎯 Priority Hierarchy for Locator Selection

| Priority | Locator Type | Example | When to Use |
|----------|-------------|---------|-------------|
| 1️⃣ | `id` | `xpath=//*[@id="login"]` | Always use if available |
| 2️⃣ | `name` | `xpath=//*[@name="email"]` | Form fields without id |
| 3️⃣ | `data-testid` | `xpath=//*[@data-testid="submit"]` | Test-specific attributes |
| 4️⃣ | `data-*` | `xpath=//*[@data-action="confirm"]` | Custom test attributes |
| 5️⃣ | ARIA | `xpath=//button[@aria-label="Submit"]` | Accessibility-focused apps |
| 6️⃣ | Text | `xpath=//button[text()="Accept"]` | Unique, stable text |
| 7️⃣ | `class` | `xpath=//*[contains(@class, "btn-primary")]` | Last resort, use with context |
| 8️⃣ | Complex | `xpath=//form[@id="x"]//input[@name="y"]` | When nothing else works |

---

## 🔍 Framework-Specific Examples

### Playwright (JavaScript/TypeScript)
```javascript
// Best practice
await page.locator('xpath=//*[@id="submit-btn"]').click();
await page.getByLabel('Email').fill('test@example.com');
await page.getByTestId('submit-button').click();
```

### Selenium (Python)
```python
# Best practice
driver.find_element(By.XPATH, "//*[@id='submit-btn']")
driver.find_element(By.NAME, "email")
driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-btn']")
```

### Cypress
```javascript
// Best practice
cy.get('#submit-btn');
cy.get('[name="email"]');
cy.get('[data-testid="submit-btn"]');
```

### Puppeteer
```javascript
// Best practice
await page.locator('xpath=//*[@id="submit-btn"]');
await page.$('#submit-btn');
```

---

## ✅ Validation Checklist

Before defining ANY selector in a Page Object:

- [ ] Did I verify Playwright MCP Server is available?
- [ ] Did I navigate to the real page with MCP browser?
- [ ] Did I use **Chrome DevTools MCP** to inspect the DOM?
- [ ] Did I capture the unique selector using DevTools?
- [ ] Did I test interacting with the element using MCP Server?
- [ ] Did I confirm the selector is unique and stable?
- [ ] Did I document the validation in the Page Object docstring?
- [ ] Did I follow the correct selector hierarchy (ID > data > XPath)?

---

## 📋 Selector Documentation Template

When adding a new selector to a Page Object, document it:

```pseudocode
class LoginPage:
    // SELECTOR: Email input field
    // PRIORITY: 1 (id)
    // VALIDATED: 2024-01-15 with Chrome DevTools MCP
    // UNIQUE: Yes - only one email input on login page
    // STABLE: Yes - id attribute doesn't change
    INPUT_EMAIL = "xpath=//*[@id='email']"
```

---

## 🔄 Selector Maintenance

### When a selector breaks:
1. Open Chrome DevTools MCP
2. Navigate to the page
3. Inspect the element
4. Find new unique attribute
5. Update the selector in Page Object
6. Document the change
7. Re-run tests to verify

### Regular validation:
- Run tests daily
- Check for selector warnings
- Review failed tests for selector issues
- Update selectors proactively

---

## ✅ Evidencia Reutilizable - AutomationTestStore (QA)

Caso validado en ejecución `ATSREG20260702171728` (registro E2E exitoso en 1 intento):

- `#AccountFrm_firstname`
- `#AccountFrm_loginname`
- `#AccountFrm_password`
- `#AccountFrm_agree`
- `button[title="Continue"]`

Se recomienda priorizar estos selectores como baseline para futuros flujos de registro mientras se mantenga estable el DOM.

---

## Referencias

- **POM Strategy**: Ver `POM/README.md`
- **Boilerplate**: Ver `Boilerplate/README.md`
- **Main Strategy**: Ver `Strategy/README.md`
