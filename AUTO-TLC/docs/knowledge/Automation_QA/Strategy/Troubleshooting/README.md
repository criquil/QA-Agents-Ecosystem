# Troubleshooting Guide

> **Lecciones aprendidas de proyectos de migración, metodologías, técnicas, errores comunes y patrones de solución.**

---

## Table of Contents

1. [Selector Validation](#selector-validation---critical-lesson)
2. [Dropdown Handling](#dropdown-handling---performance-lesson)
3. [Execution Reporting](#execution-reporting---configuration-lesson)
4. [Migration Methodology](#migration-methodology-overview)
5. [Common Error Categories](#common-error-categories)
6. [Best Practices](#best-practices)

---

## SELECTOR VALIDATION - Critical Lesson

### The Problem: Assuming Selectors Without Validation

**Real Issue Found:**
During initial boilerplate creation, selectors were defined based on assumptions or visual HTML inspection without validating them using browser automation tools:

```javascript
// ❌ INCORRECT - Selectors assumed without validation
const btnContinuar = "xpath=//button[@id='btnContinuar']";  // ID assumed - doesn't exist
const inputClave = "xpath=//*[@id='textFieldClave']";      // ID assumed - doesn't exist
```

**Real Consequences:**
- Tests consistently failed with `TimeoutError` (elements not found)
- 2+ hours lost in debugging and multiple iterations
- 7+ failed executions before identifying root cause
- Frustration in development process

### Solution: Validate FIRST with Browser Tools

**GOLDEN RULE:**
> **NEVER define a selector without validating it FIRST with browser DevTools**

**Correct Process:**

1. **Explore with Browser Automation Tool BEFORE coding:**
   - Navigate to the page using automation tool
   - Use DevTools to inspect the DOM
   - Capture real selectors

2. **Capture Real Selectors (Real Example):**
   ```javascript
   // ✅ CORRECT - Validated selectors
   // Discovered: button has id="login" NOT "btnContinuar"
   const BTN_CONTINUAR = "xpath=//button[@id='login']";
   
   // Discovered: password input has id="textFieldPassword" NOT "textFieldClave"
   const INPUT_CLAVE = "xpath=//*[@id='textFieldPassword']";
   
   // Discovered: submit button has id="actionButtonIngresar" NOT "btnIngresar"
   const BTN_INGRESAR = "xpath=//button[@id='actionButtonIngresar']";
   ```

3. **Document the Validation:**
   ```javascript
   /**
    * Page Object for login functionality
    * Validated with DevTools: 2025-11-11
    */
   class LoginPage extends BasePage {
       // Selectors - Validated with DevTools
       BTN_CONTINUAR = "xpath=//button[@id='login']";       // ✅ Validated
       INPUT_CLAVE = "xpath=//*[@id='textFieldPassword']";  // ✅ Validated
   }
   ```

### Selector Validation Checklist

Before defining ANY selector in a Page Object:

- [ ] Did I use browser automation tool to navigate to the real page?
- [ ] Did I use DevTools to inspect the DOM?
- [ ] Did I capture the unique selector using DevTools?
- [ ] Did I test interacting with the element using automation tool?
- [ ] Is the selector unique and stable?
- [ ] Did I document the validation in the Page Object docstring?
- [ ] Did I use the correct selector hierarchy (ID > attribute > XPath)?

### Warning Signs - Invalid Selectors

If you see these symptoms, you probably have invalid selectors:

1. **Consistent timeouts** when searching for elements (>30 seconds)
2. **Elements not found** at specific steps
3. **Tests that work manually** but fail automated
4. **"Generic" selectors** like `btn_continuar` without validation
5. **Lack of documentation** on how selectors were obtained
6. **Multiple iterations** of trial and error with selectors

### Performance Impact

| Scenario | Time | Success Rate | Iterations |
|----------|------|--------------|------------|
| **Before (no validation)** | 2-3 hours | 0% (7/7 failed) | 7+ |
| **After (validation first)** | 30-45 min | 100% (1/1 success) | 1 |

---

## DROPDOWN HANDLING - Performance Lesson

### The Problem: Using Standard Selection Methods on JavaScript Dropdowns

**Real Issue Found:**
JavaScript-based dropdowns (like Select2, Chosen, Bootstrap Select) don't respond correctly to standard selection methods. The method blocks execution until timeout (~20 seconds) and then fails silently or selects wrong values.

**Problematic Code:**
```javascript
// ❌ INCORRECT - Standard selection doesn't work with Select2
async function selectTipoGarantia(tipo) {
    await page.locator(SELECT_TIPO_GARANTIA).selectOption({
        label: tipo,
        timeout: 20000  // High timeout because it always fails
    });
}
```

**Real Consequences:**
- Test took **92 seconds** (too slow)
- Frequent timeouts (20s per dropdown)
- Complex code with multiple fallback attempts

### Solution: Click + Type Pattern for JavaScript Dropdowns

**GOLDEN RULE:**
> **JavaScript dropdowns require user interaction simulation: CLICK to open + TYPE to filter + ENTER to select**

**Optimized Code:**
```javascript
// ✅ CORRECT - Click + Type pattern for Select2
async function selectTipoGarantia(tipo) {
    // 1. Click the select to open Select2 dropdown
    await page.locator(SELECT_TIPO_GARANTIA).click();
    
    // 2. Type to filter options (Select2 filters automatically)
    await page.keyboard.type(tipo);
    
    // 3. Wait a moment for Select2 to process filtering
    await page.waitForTimeout(300);
    
    // 4. Enter to select the filtered option
    await page.keyboard.press("Enter");
}
```

### How to Identify JavaScript Dropdowns

**HTML Signals:**
1. Class `select2` on the `<select>` element
2. Container with class `select2-container`
3. JavaScript initializing: `$('#selector').select2()`
4. Search input with class `select2-search__field`

### Performance Impact

| Method | Time per Dropdown | Total Test (12 dropdowns) | Success Rate |
|--------|-------------------|---------------------------|--------------|
| **selectOption with fallbacks** | ~15-20s | 92 seconds | 60% |
| **Click + Type (basic)** | ~3-5s | 47 seconds | 95% |
| **Click + Type (optimized)** | ~1-2s | 31 seconds | 100% |

**Total Improvement: 92s → 31s = 65% faster** 🚀

### JavaScript Dropdown Checklist

Before implementing dropdown selection:

- [ ] Did I check if dropdown uses JavaScript (Select2, Chosen, etc.)?
- [ ] Did I test standard selection method and confirm it fails or is slow?
- [ ] Did I implement Click + Type + Enter pattern?
- [ ] Did I add wait after type for filtering?
- [ ] Did I measure execution time before and after optimization?

---

## EXECUTION REPORTING - Configuration Lesson

### The Problem: Video and Screenshots Always Enabled

**Issue Found:**
Video and screenshots were generated automatically on ALL executions, causing:

1. **Excessive disk usage**: ~3.5 MB video + ~500 KB screenshots per test
2. **Increased execution time**: ~3-5 seconds additional per capture/encoding
3. **Heavy reports**: Always present
4. **No flexibility**: Couldn't disable for quick runs (smoke tests)

### Solution: Optional Flags with Configurability

**GOLDEN RULE:**
> **Video and screenshots must be OPTIONAL and configurable via command-line to allow different execution scenarios**

**Implementation:**

1. **Add Command-Line Flags:**
   ```bash
   # Disable video
   pytest --no-video
   
   # Disable screenshots
   pytest --no-screenshots
   
   # Custom video resolution (CI/CD optimization)
   pytest --video-resolution=1280x720
   
   # Smoke tests - fastest execution
   pytest --no-video --no-screenshots
   ```

2. **Execution Scenarios:**

   | Configuration | Time | Video | Screenshots | Space | Use Case |
   |---------------|------|-------|--------------|-------|----------|
   | **Default** | ~30s | ✅ 1920x1080 | ✅ | ~4 MB | Local Dev |
   | **--no-video** | ~33s | ❌ | ✅ | ~500 KB | Visual Debug |
   | **--no-screenshots** | ~30s | ✅ 1920x1080 | ❌ | ~3.5 MB | Quick Review |
   | **--no-video --no-screenshots** | ~6s | ❌ | ❌ | ~50 KB | **Smoke Tests** |
   | **--video-resolution=1280x720** | ~32s | ✅ 1280x720 | ✅ | ~2.6 MB | **CI/CD** |

**Maximum Improvement: 30s → 6s = 80% faster** (without video/screenshots)

---

## Migration Methodology Overview

### Phase-Based Approach

Successful migrations follow a **5-phase structured methodology**:

#### Phase 1: Analysis and Planning
- **Objective**: Understand source test structure, identify complexity
- **Activities**:
  - Read and analyze Excel case specifications (if applicable)
  - Review existing test code (external migrations)
  - Identify test dependencies and shared data
  - Map business flows to technical steps
- **Output**: Migration plan with step-by-step breakdown

#### Phase 2: Exploration with Browser Tools
- **Objective**: Validate selectors and understand live application behavior
- **Activities**:
  - **MANDATORY**: Launch browser automation tool for navigation
  - Navigate through entire flow manually
  - **Capture and validate ALL selectors using DevTools**
  - Document dynamic behaviors (overlays, loading states)
  - Identify timing issues and wait requirements
- **Output**: Validated selector list with context

#### Phase 3: Page Object Model (POM) Implementation
- **Objective**: Build reusable, maintainable page abstractions
- **Activities**:
  - **ALWAYS** inherit from Base class
  - Define selectors as **class constants** (UPPERCASE)
  - One class per page/module
  - Create action methods (fill, click, navigate)
  - Create verification methods (verify*, is*)
  - **SEARCH FIRST**: Check if Page Object exists before creating new
- **Output**: Complete Page Object class with validated selectors

#### Phase 4: Test Implementation
- **Objective**: Build executable test with proper logging and reporting
- **Activities**:
  - **ALWAYS** inherit test class from TestBase
  - Implement test steps using logging wrapper
  - Add mandatory test categorization marks/tags
  - Implement shared data system for test chaining
  - Configure strategic screenshot capture
- **Output**: Functional test with comprehensive logging

#### Phase 5: Validation and Troubleshooting
- **Objective**: Ensure test passes consistently
- **Activities**:
  - Execute test and capture detailed logs
  - Analyze failures using reports and screenshots
  - Apply troubleshooting patterns
  - Iterate with documented fixes
  - Validate performance
- **Output**: Passing test with complete documentation

---

## Common Error Categories

### Error 1: Selector Issues
**Problem**: Element not found, strict mode violations, timeout errors

**Symptoms**:
- `Timeout exceeded`
- `strict mode violation: locator resolved to X elements`
- `Element not visible` or `Element not found`

**Troubleshooting**:
1. Launch browser automation tool and navigate to exact page/state
2. Use DevTools to inspect the DOM
3. Validate selector works and is unique
4. Check selector specificity - add more context
5. Verify element state - may be hidden, disabled, or covered
6. Add wait conditions

### Error 2: Timing Issues
**Problem**: Race conditions, elements not ready, premature interactions

**Symptoms**:
- Intermittent test failures
- "Element is not visible" despite being present
- Actions performed before page loads
- Empty data when grid should have content

**Troubleshooting**:
1. Identify async operations
2. Use wait for function for custom conditions
3. Replace sleep with explicit waits
4. Wait for network idle when appropriate
5. Increase timeout for slow operations

### Error 3: Type/Attribute Errors
**Problem**: Incorrect data types or missing object attributes

**Symptoms**:
- `TypeError: 'NoneType' object is not subscriptable`
- `AttributeError: 'dict' object has no attribute`
- `TypeError: expected string, got int`

**Troubleshooting**:
1. Add defensive checks
2. Validate data types
3. Inspect actual data structure

### Error 4: Strict Mode Violations
**Problem**: Selector matches multiple elements

**Symptoms**:
- `Error: strict mode violation: locator resolved to 5 elements`

**Troubleshooting**:
1. Make selector more specific
2. Use first/last/nth if multiple valid targets exist
3. Filter by text content

### Error 5: Overlay/Modal Blocking
**Problem**: Elements cannot be clicked due to overlays

**Symptoms**:
- `Error: Element is outside of the viewport`
- `Error: Element is covered by another element`

**Troubleshooting**:
1. Wait for overlay to disappear
2. Force click (use cautiously)
3. Scroll element into view
4. Wait for animations to complete

### Error 6: Shared Data Not Available
**Problem**: Test chaining fails because shared data is missing

**Symptoms**:
- Returns null or default value
- Test depends on previous test but data not persisted

**Troubleshooting**:
1. Verify data was stored in previous test
2. Check fixture configuration
3. Validate JSON/file persistence
4. Add defensive checks

---

## Best Practices

### DO's ✅

1. **ALWAYS use browser automation tools + DevTools before coding**
   - Launch tool for navigation
   - Use DevTools for selector capture
   - Navigate through entire flow manually
   - Capture evidence for documentation

2. **ALWAYS search for existing Page Objects before creating new ones**
   - Check existing classes
   - Check if methods exist in similar Page Objects
   - Extend existing classes rather than duplicate

3. **ALWAYS inherit from Base classes (Page Objects and Tests)**
   - Provides critical infrastructure
   - No exceptions

4. **ALWAYS use logging wrappers for test actions**
   - Provides automatic logging, timing, capture
   - Enables detailed reports and troubleshooting

5. **ALWAYS include test categorization marks/tags**
   - Project identifier
   - Environment (dev/qa/uat/prod)
   - Functionality (module/feature)
   - Specific test case

6. **ALWAYS define selectors as class constants in UPPERCASE**
   - Define at class level, not in methods
   - Use descriptive names

7. **ALWAYS use XPath with priority hierarchy**
   - Priority: id > name > data-testid > ARIA > text > class > complex
   - Validate every selector

8. **ALWAYS use native framework methods over JavaScript**
   - Better integration and reliability

9. **ALWAYS implement fallback strategies for fragile interactions**
   - Retry mechanisms
   - Descriptive error messages

10. **ALWAYS document migration process**
    - Include: purpose, source, steps, selectors, troubleshooting
    - Document every fix attempt

### DON'Ts ❌

1. **NEVER create tests without explicit user request**
2. **NEVER use selectors directly in test files** - Use Page Objects
3. **NEVER use unvalidated selectors** - Always validate first
4. **NEVER use absolute XPath from root** - Use context-based
5. **NEVER hardcode test data** - Use external data files
6. **NEVER use sleep for waiting** - Use explicit waits
7. **NEVER ignore StrictMode violations**

---

## Referencias

- **POM Strategy**: Ver `POM/README.md`
- **Selectors Strategy**: Ver `Selectors_Strategy/README.md`
- **Test Categorization**: Ver `Test_Categorization/README.md`
- **Data Parametrization**: Ver `Data_Parametrization/README.md`
- **Main Strategy**: Ver `Strategy/README.md`
