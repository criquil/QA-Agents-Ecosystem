# Data Parametrization - MANDATORY

> **NOTA**: Esta sección es **OBLIGATORIA** para todos los tests automatizados.

---

## 🔴 CRITICAL RULE: ALL Data Must Be Parameterized

**NEVER** hardcode data in tests or Page Objects. **ALL** data (input or output) must be parameterized and loaded from external files. This is a rule **WITHOUT EXCEPTION**.

---

## 🚫 What is Hardcoding Data?

### ❌ INCORRECT EXAMPLES (Hardcoded):

```javascript
// ❌ BAD: Hardcoded data directly in test
async function testLoginSuccess(page) {
  await page.fill('#username', '2225');  // ❌ HARDCODED
  await page.fill('#password', 'password123');  // ❌ HARDCODED
}

// ❌ BAD: Hardcoded URLs
async function testNavigateToModule(page) {
  await page.goto('http://example.bank.com/login');  // ❌ HARDCODED
}

// ❌ BAD: Hardcoded validation data
async function testValidateMessage(page) {
  const message = await page.locator('.message').textContent();
  assert.equal(message, 'Login successful');  // ❌ HARDCODED
}
```

### ✅ CORRECT EXAMPLES (Parameterized):

```javascript
// ✅ GOOD: Data loaded from external JSON/YAML
async function testLoginSuccess(page, dataLoader) {
  const user = await dataLoader.getData('users', 'validUser');
  await loginPage.login(user.username, user.password);
}

// ✅ GOOD: URLs from configuration
async function testNavigateToModule(page, config) {
  const baseUrl = config.environments.qa.baseUrl;
  await page.goto(baseUrl);
}

// ✅ GOOD: Validation data parameterized
async function testValidateMessage(page, dataLoader) {
  const expectedMessages = await dataLoader.getData('messages', 'login');
  const actualMessage = await page.locator('.message').textContent();
  assert.equal(actualMessage, expectedMessages.success);
}
```

---

## 📁 Project Data Structure

### Directory `data/`

```
data/
├── config.yaml              # General project configuration
├── users.json               # User data (credentials)
├── messages.json           # Expected messages (validations)
├── forms.json              # Form data
└── cases/                  # Test case-specific data
    ├── TC_001.json
    ├── TC_002.json
    └── ...
```

---

## 🔧 DataLoader - Parameterization Helper

### Supported Formats
- ✅ JSON (`.json`)
- ✅ CSV (`.csv`)
- ✅ YAML (`.yaml`, `.yml`)

### Usage Example

```javascript
import { DataLoader } from './helpers/data-loader.js';

class LoginTests {
  
  async setup() {
    this.dataLoader = new DataLoader({ dataDir: 'data' });
    this.config = await this.dataLoader.loadYaml('config');
  }
  
  async testLoginWithValidUser() {
    // Load user data
    const user = await this.dataLoader.getData('users', 'validUser');
    
    // Load environment config
    const baseUrl = this.config.environments.qa.baseUrl;
    
    // Navigate
    await this.page.goto(baseUrl);
    
    // Login with parameterized data
    await this.loginPage.login(user.username, user.password);
    
    // Validate with parameterized message
    const messages = await this.dataLoader.getData('messages', 'login');
    await this.loginPage.validateSuccess(messages.success);
  }
}
```

---

## 📋 Types of Data to Parameterize

### 1. User Credentials (`data/users.json`)

```json
{
  "users": {
    "valid": {
      "username": "user123",
      "password": "secure_password"
    },
    "invalid": {
      "username": "invalid_user",
      "password": "wrong_password"
    },
    "admin": {
      "username": "admin",
      "password": "admin_password"
    }
  }
}
```

**Usage**:
```javascript
const user = await dataLoader.getData('users', 'users.valid');
await loginPage.login(user.username, user.password);
```

### 2. Environment Configuration (`data/config.yaml`)

```yaml
environments:
  default: "qa"
  qa:
    baseUrl: "http://qa.example.com"
    timeout: 30000
  dev:
    baseUrl: "http://dev.example.com"
    timeout: 30000
  prod:
    baseUrl: "http://prod.example.com"
    timeout: 60000
```

**Usage**:
```javascript
const config = await dataLoader.loadYaml('config');
const environment = config.environments.qa;
await page.goto(environment.baseUrl);
```

### 3. Validation Messages (`data/messages.json`)

```json
{
  "login": {
    "success": "Welcome to the system",
    "failed": "Invalid username or password",
    "blocked": "User account blocked"
  },
  "forms": {
    "requiredField": "This field is required",
    "invalidFormat": "Invalid format",
    "savedSuccess": "Data saved successfully"
  }
}
```

**Usage**:
```javascript
const messages = await dataLoader.getData('messages', 'login');
assert(actualMessage === messages.success);
```

### 4. Form Data (`data/forms.json`)

```json
{
  "createDebit": {
    "valid": {
      "amount": "1000.00",
      "concept": "Payment services",
      "account": "0000003100010000000001",
      "description": "Monthly automatic debit"
    },
    "invalid": {
      "amount": "-500",
      "concept": "",
      "account": "123",
      "description": ""
    }
  }
}
```

**Usage**:
```javascript
const debitData = await dataLoader.getData('forms', 'createDebit.valid');
await debitPage.completeForm(
  amount=debitData.amount,
  concept=debitData.concept,
  account=debitData.account
);
```

### 5. Test Case-Specific Data (`data/cases/TC_001.json`)

```json
{
  "testCase": "TC_001",
  "description": "Login success with valid user",
  "input": {
    "username": "user123",
    "password": "password123"
  },
  "expectedOutput": {
    "message": "Welcome to the system",
    "targetUrl": "/dashboard",
    "visibleElements": ["mainMenu", "userProfile"]
  }
}
```

**Usage**:
```javascript
const tcData = await dataLoader.loadJson('cases/TC_001');
const inputData = tcData.input;
const expected = tcData.expectedOutput;

await loginPage.login(inputData.username, inputData.password);
assert(page.url().endsWith(expected.targetUrl));
```

---

## 🎯 Parameterization Patterns

### Pattern 1: Configuration Fixture

```javascript
// Framework-specific: pytest fixture equivalent in Playwright
async function config({}, use) {
  const loader = new DataLoader({ dataDir: 'data' });
  const config = await loader.loadYaml('config');
  await use(config);
}

async function dataLoader({}, use) {
  const loader = new DataLoader({ dataDir: 'data' });
  await use(loader);
}
```

### Pattern 2: Parametrization (Framework-Specific)

```javascript
// Example: pytest.mark.parametrize equivalent
const testCases = await dataLoader.getData('users_test', 'cases');

for (const userData of testCases) {
  test(`Login with ${userData.username}`, async ({ page }) => {
    await loginPage.login(userData.username, userData.password);
    assert(await page.textContent()).includes(userData.expectedResult);
  });
}
```

### Pattern 3: Data-Driven Testing

```javascript
class CreateDebitTests {
  
  async loadTestData() {
    this.testData = await this.dataLoader.loadJson('cases/createDebitCases');
  }
  
  async testCreateDebitCase1() {
    const testCase = this.testData.case1;
    await this.debitPage.createDebit(testCase.input);
    await this.debitPage.validateResult(testCase.expectedOutput);
  }
}
```

---

## ✅ Parameterization Checklist

Before creating or modifying any test, verify:

### Input Data:
- [ ] ✅ Credentials loaded from `data/users.json`
- [ ] ✅ URLs loaded from `data/config.yaml`
- [ ] ✅ Form data loaded from `data/forms.json`
- [ ] ✅ Timeout configuration loaded from `data/config.yaml`
- [ ] ✅ Test case-specific data from `data/cases/TC_XXX.json`

### Output Data (Validations):
- [ ] ✅ Expected messages loaded from `data/messages.json`
- [ ] ✅ Expected results parameterized
- [ ] ✅ Expected states defined in data files
- [ ] ✅ Validation values externalized

### Configuration:
- [ ] ✅ Test framework configuration from `data/config.yaml`
- [ ] ✅ Logging configuration from `data/config.yaml`
- [ ] ✅ Reporting configuration from `data/config.yaml`

---

## 🚫 Anti-Patterns: What NOT to Do

### ❌ ANTI-PATTERN 1: Hardcoding Credentials

```javascript
// ❌ BAD
async function testLogin() {
  await loginPage.login('user123', 'password123');
}
```

**Problems**:
- Credentials exposed in code
- Difficult to change credentials
- Cannot reuse across environments
- Security risk

### ❌ ANTI-PATTERN 2: Hardcoding URLs

```javascript
// ❌ BAD
async function testNavigate() {
  await page.goto('http://example.bank.com/login');
}
```

**Problems**:
- Doesn't work in different environments
- Difficult to maintain multiple URLs
- Changes require code modifications

### ❌ ANTI-PATTERN 3: Hardcoding Validation Messages

```javascript
// ❌ BAD
async function testValidateError() {
  const message = await page.locator('.error').textContent();
  assert(message === 'Invalid credentials');
}
```

**Problems**:
- Messages may change
- Doesn't support internationalization
- Difficult to maintain consistency

### ❌ ANTI-PATTERN 4: Hardcoding Form Data

```javascript
// ❌ BAD
async function testCreateDebit() {
  await debitPage.completeForm(
    amount: '1000.00',
    concept: 'Payment services',
    account: '0000003100010000000001'
  );
}
```

**Problems**:
- Test data not reusable
- Difficult to create variations
- Cannot execute data-driven tests

---

## ✅ Good Parameterization Practices

### 1. Separate Data by Type

```
data/
├── users.json        # Only credentials
├── messages.json    # Only messages
├── forms.json       # Only form data
└── config.yaml      # Only configuration
```

### 2. Use Descriptive Names

```json
{
  "users": {
    "valid_admin": { ... },
    "valid_operator": { ... },
    "invalid_blocked": { ... },
    "invalid_wrong_password": { ... }
  }
}
```

### 3. Document Data Structure

```json
{
  "_schema": {
    "description": "User data for login tests",
    "version": "1.0",
    "fields": {
      "username": "string - Username",
      "password": "string - User password",
      "role": "string - User role (admin, operator, etc.)"
    }
  },
  "users": {
    "valid": {
      "username": "user123",
      "password": "password123",
      "role": "admin"
    }
  }
}
```

### 4. Use Fixtures for DataLoader

```javascript
// Test framework specific: conftest.py equivalent
export async function dataLoader({}, use) {
  const loader = new DataLoader({ dataDir: 'data' });
  await use(loader);
}

export async function config({}, use) {
  const loader = new DataLoader({ dataDir: 'data' });
  const config = await loader.loadYaml('config');
  await use(config);
}
```

### 5. Validate Loaded Data

```javascript
async function testLoginWithValidUser(dataLoader) {
  const user = await dataLoader.getData('users', 'users.valid');
  
  // Validate data exists
  assert(user !== null, 'User data not found');
  assert('username' in user, 'Username not defined');
  assert('password' in user, 'Password not defined');
  
  // Use validated data
  await loginPage.login(user.username, user.password);
}
```

---

## ⚠️ FINAL REMINDER

**Data parameterization is NOT optional**. It is a **MANDATORY** rule for:

1. ✅ Keeping sensitive data out of code
2. ✅ Facilitating execution across multiple environments
3. ✅ Enabling data-driven testing
4. ✅ Improving code maintainability
5. ✅ Reusing data between tests
6. ✅ Meeting security standards

**If you find hardcoded data in tests or Page Objects, you MUST refactor to parameterize it.**

---

## ✅ Evidencia Reutilizable - Registro E2E AutomationTestStore (QA)

Para el flujo de registro, mantener credenciales y datos de alta en archivo externo:

- `application-files/AutomationTestStore/qa/test-data/credentials/automationteststore-account.json`

Resultado observado (ejecución `ATSREG20260702171728`): éxito en 1 intento sin reintentos, con trazabilidad completa entre datos de entrada y reporte final.

---

## 🎯 Executive Summary

| Data Type | File | Usage Example |
|-----------|------|---------------|
| **Credentials** | `data/users.json` | `dataLoader.getData('users', 'users.valid')` |
| **URLs/Environments** | `data/config.yaml` | `config.environments.qa.baseUrl` |
| **Messages** | `data/messages.json` | `dataLoader.getData('messages', 'login.success')` |
| **Forms** | `data/forms.json` | `dataLoader.getData('forms', 'createDebit.valid')` |
| **Specific Cases** | `data/cases/TC_XXX.json` | `dataLoader.loadJson('cases/TC_001')` |
| **Configuration** | `data/config.yaml` | `config.playwright.timeout` |

**Golden Rule**: If it's a value that can change, it must be parameterized. **NEVER hardcode**.

---

## Referencias

- **POM Strategy**: Ver `POM/README.md`
- **Selectors Strategy**: Ver `Selectors_Strategy/README.md`
- **Test Categorization**: Ver `Test_Categorization/README.md`
- **Main Strategy**: Ver `Strategy/README.md`
