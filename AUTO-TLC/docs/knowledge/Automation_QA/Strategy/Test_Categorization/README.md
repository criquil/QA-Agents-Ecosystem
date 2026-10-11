# Test Categorization - MANDATORY

> **NOTA**: Esta sección es **OBLIGATORIA** para todos los tests automatizados.

---

## 🚀 Framework Integration

Test frameworks use categorization marks/tags to:
- **Filter tests** for selective execution
- **Control CI/CD pipelines** - determine which tests run at each stage
- **Organize test suites** - group by environment, feature, or priority
- **Generate reports** - categorize results by tags

---

## 🏷️ Test Tags - MANDATORY

### 🔴 CRITICAL RULE: All Tests MUST Have Tags

**NO test can be created or executed without the mandatory tags.**

---

### 🎯 Criticality: Use in CI/CD Pipelines

The **mandatory tags are NOT arbitrary** - they are **CRITICAL** because **CI/CD pipelines use them to filter and selectively execute tests**.

#### 🚀 Real Pipeline Usage:

Tags are the **only way** to control which tests run at each pipeline stage:

```yaml
# CI/CD Pipeline Example
stages:
  - smoke_tests
  - regression_qa
  - regression_prod
  - deployment

# Stage 1: Smoke tests on every commit
smoke_tests:
  script:
    # Only runs tests tagged with smoke + qa
    npx playwright test --grep "@smoke and @qa"
  # Without these tags, nothing runs

# Stage 2: Full regression in QA (nightly)
regression_qa:
  script:
    # Runs all QA tests except slow ones
    npx playwright test --grep "@qa and not @slow"
  # Without @qa tag, test doesn't run in this environment

# Stage 3: Production tests (pre-deploy)
regression_prod:
  script:
    # Only validated tests for production
    npx playwright test --grep "@prod and @critical"
  # Without @prod tag, test NEVER reaches production

# Stage 4: Tests by functionality (partial deploy)
deploy_transferencias:
  script:
    # Selective deploy of one functionality
    npx playwright test --grep "@transferencias and @prod"
  # Without functionality tag, no partial deploy possible
```

#### 💥 Consequences of NOT Using Tags:

1. **Test NOT executed in pipelines** - Filters won't find the test
2. **Deploy blocked** - Without validation, deploy stops
3. **Lost visibility** - Consolidated reports don't categorize the test
4. **Impossible selective execution** - Can't run by environment or feature
5. **CI/CD failure** - Pipeline may fail due to missing minimum tests

---

### ✅ MANDATORY Tags (All tests must include):

#### 1️⃣ **Project Tag** (ALWAYS)
- **Mandatory on ALL tests without exception**
- **Pipeline Use**: Filters tests in shared repositories
- Identifies that the test belongs to the project
- Allows filtering tests in mixed suites
- **Pipeline Command**: `npx playwright test --grep "project-name"`

#### 2️⃣ **Environment Tag** (MANDATORY)
- **Pipeline Use**: **CRITICAL** - determines which environment the test runs in
- Indicates the target environment
- Allowed values: `dev`, `qa`, `uat`, `prod`
- Enables selective execution by environment
- **Pipeline Commands**:
  ```bash
  npx playwright test --grep "@dev"      # Development pipeline
  npx playwright test --grep "@qa"       # QA/testing pipeline
  npx playwright test --grep "@uat"      # UAT/staging pipeline
  npx playwright test --grep "@prod"     # Production pipeline
  ```
- **Without this tag**: Test NOT executed in ANY environment

#### 3️⃣ **Functionality Tag** (MANDATORY)
- **Pipeline Use**: Enables feature-based deploys (feature toggles)
- Identifies the functionality under test
- Must be descriptive and lowercase
- Allows grouping tests by feature
- **Pipeline Commands**:
  ```bash
  npx playwright test --grep "@login"           # Login deploy
  npx playwright test --grep "@transferencias"  # Transfers deploy
  npx playwright test --grep "@payment"         # Partial payment deploy
  ```
- **Without this tag**: Impossible to do feature-selective deploys

#### 4️⃣ **Specific Case Tag** (MANDATORY)
- **Pipeline Use**: Enables granular execution and specific debugging
- Describes the specific test case
- Must be unique and descriptive
- Format: `{functionality}_{variant}`
- **Pipeline Commands**:
  ```bash
  npx playwright test --grep "@login_success"                    # Only success cases
  npx playwright test --grep "@transfer_insufficient_funds"     # Only specific case
  ```
- **Without this tag**: Difficulty isolating and debugging specific tests

---

### 🎯 Optional Tags (But Important for Pipeline Control):

| Tag | Pipeline Use | Description |
|-----|-------------|-------------|
| `@smoke` | Runs on every commit | Fast smoke tests |
| `@regression` | Runs nightly/weekly | Full regression suite |
| `@critical` | Blocks deploy if fails | Critical path tests |
| `@slow` | Excluded from fast runs | Excluded from quick runs |
| `@skip` | Temporarily disabled | Temporarily disabled |
| `@wip` | Work in progress | Not ready for execution |

**Pipeline Usage**:
```bash
# Fast smoke tests on every commit (< 5 min)
npx playwright test --grep "@smoke and not @slow"

# Critical tests that block production
npx playwright test --grep "@critical and @prod"

# Full regression excluding slow tests
npx playwright test --grep "@regression and not @slow"
```

---

### 📝 Complete Tag Structure:

```javascript
// Framework-specific: Playwright example
import { test, expect } from '@playwright/test';

test.describe('Login Functionality', () => {
  test('login with valid credentials', {
    tag: ['@project-name', '@qa', '@login', '@login_success', '@smoke']
  }) => {
    // Test implementation
  });
});

// Or using test annotations
test('login with valid credentials', {
  annotations: [
    { type: 'project', description: 'project-name' },
    { type: 'environment', description: 'qa' },
    { type: 'feature', description: 'login' },
    { type: 'case', description: 'login_success' }
  ]
}, async ({ page }) => {
  // Test implementation
});
```

---

### 🚫 PROHIBITED:

- **Creating tests without the 4 mandatory tags** → Test will NOT run in pipeline
- **Using generic or ambiguous tags** (`@test1`) → Pipeline cannot filter
- **Duplicating tags on the same test** → Confusion in pipeline filters
- **Using spaces in tag names** → Invalid syntax
- **Using uppercase in tags** → Convention: lowercase and underscores only
- **Omitting environment tag** → Pipeline will NOT execute test in ANY environment

---

### 💡 Important Reminder:

**Without the correct tags, your test will be IGNORED by the pipeline and NEVER execute.**

CI/CD pipelines run commands like:
```bash
npx playwright test --grep "@qa"           # Only tests with @qa tag
npx playwright test --grep "@smoke"         # Only tests with @smoke tag
npx playwright test --grep "@prod and @critical"  # Combination of tags
```

**If your test doesn't have these tags, the filter won't find it and it will NOT RUN.**

---

### ✅ Correct Examples:

```javascript
// Example 1: Successful login
test('successful login', {
  tag: ['@project-name', '@qa', '@login', '@login_success', '@smoke']
}, async ({ page }) => {
  // Test implementation
});

// Example 2: Transfer with insufficient funds
test('transfer with insufficient funds', {
  tag: ['@project-name', '@qa', '@transfer', '@transfer_insufficient_funds']
}, async ({ page }) => {
  // Test implementation
});

// Example 3: Recent transactions query
test('query recent transactions', {
  tag: ['@project-name', '@prod', '@queries', '@query_recent_transactions', '@regression']
}, async ({ page }) => {
  // Test implementation
});
```

### ❌ INCORRECT Examples:

```javascript
// ❌ INCORRECT: Missing mandatory tags
test('login', async ({ page }) => {
  // Test implementation
});

// ❌ INCORRECT: Tags with spaces
test('login', {
  tag: ['@login successful']
}, async ({ page }) => {
  // Test implementation
});

// ❌ INCORRECT: Tags with uppercase
test('login', {
  tag: ['@LOGIN_SUCCESS']
}, async ({ page }) => {
  // Test implementation
});

// ❌ INCORRECT: Generic tags
test('login', {
  tag: ['@test1', '@prueba']
}, async ({ page }) => {
  // Test implementation
});
```

---

### 🔍 Selective Execution with Tags (Real Pipeline Usage):

```bash
# ========================================
# CI/CD PIPELINES - REAL COMMANDS
# ========================================

# Pipeline Stage 1: Smoke tests on every commit (development)
npx playwright test --grep "@smoke and @qa and @project-name"

# Pipeline Stage 2: Login tests in QA
npx playwright test --grep "@login and @qa"

# Pipeline Stage 3: Critical tests before production
npx playwright test --grep "@critical and @prod"

# Pipeline Stage 4: Full QA regression (nightly)
npx playwright test --grep "@qa and not @slow"

# Pipeline Stage 5: Selective transfer deploy
npx playwright test --grep "@transfer and @prod"

# Pipeline Stage 6: Only smoke tests excluding slow ones
npx playwright test --grep "@smoke and not @slow"

# Pipeline Stage 7: Full production validation
npx playwright test --grep "@prod and @project-name"

# ========================================
# MANUAL EXECUTIONS / DEBUGGING
# ========================================

# Run only tests of a specific functionality
npx playwright test --grep "@payment_services"

# Run tests of multiple functionalities in QA
npx playwright test --grep "@login|@transfer" --grepFlags "i"

# Run all tests except slow ones
npx playwright test --grep "not @slow"

# Run only critical smoke tests
npx playwright test --grep "@smoke and @critical"
```

---

### 📊 Integration with Reporting

Tags are automatically included in:
- **JSON of each test** → Enables post-filtering
- **Individual run report** → Groups by tags
- **Consolidated historical report** → Trends by environment/feature
- **HTML dashboard filters** → Interactive filters
- **Trend analysis** → Comparison between environments
- **Pipeline metrics** → % success by environment/feature

---

### ⚠️ Automatic Validation

The system must validate:
1. **All tests have the 4 mandatory tags** → Without them, pipeline ignores them
2. **Tags follow naming convention** → Lowercase, no spaces
3. **No duplicates** → Avoid confusion in filters
4. **Valid environment values** → Only: dev, qa, uat, prod
5. **Project tag is present** → Global project filter

**If a test doesn't comply with mandatory tags:**
- ❌ Should NOT run locally
- ❌ Won't be found by pipeline filters
- ❌ Won't appear in categorized reports
- ❌ WILL GENERATE a validation error
- ❌ WILL BLOCK merge/commit in quality control

---

### 🎯 Criticality Summary:

| Tag | Pipeline Use | Consequence if Missing |
|-----|-------------|----------------------|
| `{project}` | Global project filter | Test NOT executed in project pipeline |
| `{environment}` | Determines WHERE to run | Test NOT executed in ANY environment |
| `{functionality}` | Feature-selective deploy | NO partial deploy possible |
| `{specific_case}` | Granular execution | CANNOT isolate for debugging |

**Conclusion**: Tags are NOT decorative - they are the **control mechanism** that the pipeline uses to decide **WHAT to run, WHEN and WHERE**.

---

## Referencias

- **POM Strategy**: Ver `POM/README.md`
- **Selectors Strategy**: Ver `Selectors_Strategy/README.md`
- **Main Strategy**: Ver `Strategy/README.md`
