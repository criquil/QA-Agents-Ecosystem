# MANUAL-TLC — Manual Test Life Cycle Orchestrator (MANU)

## What This Repo Is

This is a **knowledge base + agent configuration repository** for the **Manual Test Life Cycle Orchestrator (MANUAL-TLC v1.0)**. It is NOT a traditional code project — there are no build commands, tests, or CI pipelines to run.

The repo defines:
- **1 MANUAL-TLC agent** (`.claude/agents/`) as the conversational entry point and orchestrator, assisted by the **Playwright MCP Server**
- **42 skills** (`.claude/skills/`): 6 lifecycle-phase skills, 10 tool/domain skills and 26 autonomous knowledge skills
- **Knowledge base** (`.claude/skills/kb-*`) with autonomous manual-testing knowledge

## Scope: Manual Testing

The orchestrator drives **manual testing of a web system**, using the Playwright MCP Server as the single support tool for navigating the real UI and capturing evidence. Seven manual test types are covered:

| Test type | Purpose |
|---|---|
| **Pruebas Funcionales** | Verify every function behaves as its functional requirements state |
| **Pruebas de Sistema (System Testing)** | Validate the fully integrated system end-to-end against system requirements |
| **Pruebas de Regresión** | Confirm that changes did not break previously working behaviour |
| **Smoke Testing** | Minimum build-acceptance check executed before any deeper testing |
| **Sanity Testing** | Narrow, focused check that a specific fix works as intended |
| **Pruebas Exploratorias** | Simultaneous learning, test design and execution (charters / SBTM) |
| **Pruebas de Aceptación (UAT)** | Business and user validation against agreed acceptance criteria |

## Agent Architecture (MANUAL-TLC v1.0)

The orchestrator (`manual-tlc-orchestrator-manual`, conversational name **MANU**) loads 6 specialized skills in strict order:

```
1. manual-tlc-intake-manual         → Requirements gathering + single support-tool selection
2. manual-tlc-diagnostics-manual    → Environment readiness, risks, build validation
3. manual-tlc-procedure-plan-manual → Test types, scenarios, test data strategy
4. manual-tlc-test-plan-manual      → Formal test plan document (ISTQB/IEEE-829)
5. manual-tlc-execution-manual      → MCP-assisted manual sessions + evidence capture
6. manual-tlc-analysis-manual       → Metrics, RCA, report with verdict (PASSED/CONDITIONAL/FAILED)
```

Each skill is autonomous and must operate from its own embedded instructions.

## Key Conventions

### v1.0 Defaults
- **Single support tool** by default: the **Playwright MCP Server** — never multi-tool unless explicitly requested
- **Sequential execution** — parallel only if `parallel: true` is explicitly requested
- **3 analysis modes**: `individual` (current run), `vs_baseline` (compare to saved baseline), `vs_other_runs` (compare to prior runs)
- Plan state persists in `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/plan.yaml`

### File Locations
- **Plan state**: `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/plan.yaml`
- **Test plan doc**: `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/Test_Plan_{proyecto}_{ambiente}_{YYYY-MM-DD}.md`
- **Test cases**: `PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/`
- **BDD scenarios (Gherkin)**: `PRJ-{proyecto}/{ambiente}/Test_Cases/BDD/`
- **Test case templates (mandatory, read-only source)**: `templates/` (repo root) — `tc_template.md` (manual/executable cases), `bdd_template.md` (Gherkin scenarios), `tc_example.md` (worked example)
- **Test data**: `PRJ-{proyecto}/{ambiente}/Test_Data/`
- **Selector catalogue** (validated XPath): `PRJ-{proyecto}/{ambiente}/Test_Data/Selectors/`
- **Evidence** (screenshots, snapshots, traces, video): `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/Evidence/`
- **Test results**: `PRJ-{proyecto}/{ambiente}/Test_Results/{YYYY-MM-DD}/`
- **Defect registry**: `PRJ-{proyecto}/{ambiente}/Issues&Bugs/{YYYY-MM-DD}/Issues_Bugs_{YYYY-MM-DD}.md`
- **Analysis report**: `PRJ-{proyecto}/{ambiente}/Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Test_Report_{proyecto}_{ambiente}_{YYYY-MM-DD}.md`
- **Structure governance**: the `manual-project-structure` skill creates and enforces this tree — no artifact may live outside it

### Playwright MCP Server Setup

Configured as an MCP server in `.claude/settings.json` under the key `playwright`:

```json
{
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "@playwright/mcp@latest"],
      "enabled": true
    }
  }
}
```

Core tools used during execution: `browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_press_key`, `browser_hover`, `browser_wait_for`, `browser_take_screenshot`, `browser_console_messages`, `browser_network_requests`, `browser_tabs`, `browser_handle_dialog`, `browser_file_upload`, `browser_start_tracing` / `browser_stop_tracing`, `browser_start_video` / `browser_stop_video`, `browser_close`.

### Knowledge Base Structure (`.claude/skills/kb-*`)

The knowledge base is distributed across standalone autonomous knowledge skills, numbered by theme prefix: `kb-00` (indexes and tool comparisons), `kb-01` (fundamentals, requirements, data, metrics, MCP guide), `kb-02` (functional testing, system testing, planning, roles), `kb-03` (standards, regression, formal plan, UAT), `kb-04` (defects, environment, smoke/sanity), `kb-05` (analysis/closure, test design techniques), `kb-06` (exploratory testing).

### Tool Selection Rules
When an agent selects a support tool, it follows this decision matrix:
- **Playwright MCP Server** — default and only tool: drives a real browser through accessibility snapshots, enables step-by-step manual session execution and evidence capture (screenshots, traces, video)
- A different tool is used **only** if the user explicitly requests it, and the rationale must be recorded in `selected_tool.rationale`

### Selector Strategy (XPath)

Element localization is governed by the `manual-selector-strategy` skill. Priority rules:

1. **Playwright MCP Server only.** **Chrome DevTools MCP is forbidden** (`chrome-devtools-mcp` or any other DevTools inspection MCP server). Every selector is discovered and validated inside the Playwright MCP session.
2. **XPath is mandatory** for any selector that is written or documented.
3. **Attribute priority**: `id` → `name` → `data-testid` / `data-*` → ARIA (`role`, `aria-label`) → unique stable text → `class` → complex XPath (last resort).
4. **No selector may be used or documented until validated** with the Playwright MCP Server: uniqueness (`browser_evaluate` → `snapshotLength === 1`) plus functional confirmation.
5. **Never invent selectors** and never use dynamically generated or frequently changing selectors (auto ids, hashes, utility classes).
6. Validated selectors are recorded in `PRJ-{proyecto}/{ambiente}/Test_Data/Selectors/{module}.md`.

Supporting tools used for validation: `browser_navigate`, `browser_snapshot`, `browser_find`, `browser_evaluate`, plus the interaction tool itself (`browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_check`).

### Mandatory Test Case Templates

Every test case — whether **generated** by a skill, **created** on request or **imported** from an external source (Excel, legacy docs, another repo) — MUST be built from the standard templates in the repo-root `templates/` folder. Enforced by `manual-project-structure` and applied by every skill that produces cases:

| Template | Use for | Output target |
|---|---|---|
| `templates/tc_template.md` | Manual/executable test cases | `PRJ-{proyecto}/{ambiente}/Test_Cases/TestScript/TC-{TIPO}-{NNN}.md` |
| `templates/bdd_template.md` | Gherkin/BDD scenarios | `PRJ-{proyecto}/{ambiente}/Test_Cases/BDD/` |
| `templates/tc_example.md` | Worked example — reference of a correctly completed `tc_template.md` | Reference only — never copied as a real case |

Rules:
1. **No test case is created from scratch.** Each case starts as a copy of the matching template, preserving its full section structure (`Propósito`, `Descripción`, `Data I/O`, `Precondiciones`, `Steps` / `Especificación Gherkin`, `Resultado Esperado`, `Observaciones generales`, `Postcondiciones / Limpieza`, `Flujo`).
2. Fill the template by replacing placeholders and remove the instructional HTML comments (`<!-- ... -->`) from the final artifact.
3. **Imported cases must be normalized** into the template structure before being saved under `Test_Cases/`; the external format is never accepted as-is.
4. The templates are **read-only sources**: never modify, rename, move or copy them inside `PRJ-{proyecto}/{ambiente}/`.

### Project Folder Structure

All artifacts live inside a single governed tree, created and enforced by the `manual-project-structure` skill:

```
PRJ-{proyecto}/
└── {ambiente}/
    ├── DOCs/{TipoDocumento}/          ← one folder per document type
    ├── Test_Cases/
    │   ├── TestScript/                ← manual/executable test cases
    │   └── BDD/                       ← Gherkin scenarios
    ├── Test_Results/{YYYY-MM-DD}/     ← one folder per execution date
    ├── Test_Data/                     ← test data, accounts, selector catalogue
    ├── Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/
    └── Issues&Bugs/{YYYY-MM-DD}/      ← one folder per execution date
```

Rules:
1. The structure is created at cycle start (Phase 1), before writing any artifact.
2. Standard folder names are exact and immutable: `DOCs`, `Test_Cases`, `TestScript`, `BDD`, `Test_Results`, `Test_Data`, `Test_Results_Analisis_&_RCA`, `Issues&Bugs`.
3. `DOCs/{TipoDocumento}` uses a controlled catalogue (`Test_Plan`, `Test_Strategy`, `Requirements`, `Test_Design`, `Environment`, `Session_Reports`, `UAT`, `Sign_Off`, `Metrics`, `Manuals`); folders are created on demand and extensions must follow PascalCase with underscores.
4. `{YYYY-MM-DD}` is the ISO date of the execution; additional runs on the same day use the suffix `_r{NN}`.
5. Nothing is written outside `PRJ-{proyecto}/{ambiente}/` except `.claude/`, `CLAUDE.md`, `.claude/settings.json` and the read-only `templates/` folder (mandatory source of the test case templates — never edited or copied in place). Creation is idempotent (`New-Item -Force`): never delete or overwrite existing content.

### Mandatory Output Package

Every execution run — full, partial, `smoke_failed` or blocked — must end with a documented output package. The run is **not complete** until all applicable artifacts exist (base: `PRJ-{proyecto}/{ambiente}/`):

| # | Output | Path | When |
|---|---|---|---|
| 1 | **Result** (execution summary) | `Test_Results/{YYYY-MM-DD}/Execution_Summary.yaml` (+ `.md`) | Always, even on `smoke_failed` |
| 2 | **Evidence** | `Test_Results/{YYYY-MM-DD}/Evidence/{CASE-ID}/` | Every executed case |
| 3 | **Defect registry** | `Issues&Bugs/{YYYY-MM-DD}/Issues_Bugs_{YYYY-MM-DD}.md` | If any FAIL/BLOCKED |
| 4 | **Analysis** | `Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Analysis_{YYYY-MM-DD}.md` | Always (Phase 6) |
| 5 | **RCA** | `Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/RCA_{DEF-NNNN}.md` | Every P1 defect; if none, "RCA: no aplica" is documented in the Analysis |
| 6 | **Documentation** (metrics + plan state) | `DOCs/Metrics/Metrics_{YYYY-MM-DD}.md` + `DOCs/Test_Plan/plan.yaml` | Always |
| 7 | **Test report with verdict** | `Test_Results_Analisis_&_RCA/{YYYY-MM-DD}/Test_Report_{...}.md` | Cycle close (Phase 6) |

## Pitfalls

- **Every skill is autonomous.** Skills must operate from their embedded instructions and knowledge.
- **Never skip the smoke test.** Execution always runs smoke first; if it fails, stop and report.
- **Never mark a phase complete without user confirmation** for execution-related decisions (especially phase 5).
- **Plan state is in `PRJ-{proyecto}/{ambiente}/DOCs/Test_Plan/plan.yaml`**, not in `.claude/`.
- **Evidence is mandatory.** A manual test case without evidence (screenshot, snapshot, trace or log) cannot be reported as PASS.
- **No execution ends undocumented.** Every run — full, partial, `smoke_failed` or blocked — must finish with the mandatory output package (Result, Evidence, Defects, Analysis, RCA, Documentation); an undocumented run cannot be reported as completed.
- **Selectors must be validated.** Never use, document or "invent" an element selector that has not been validated with the Playwright MCP Server (`snapshotLength === 1` + functional confirmation). Never use Chrome DevTools MCP.
- **No case without its template.** Every test case — generated, created or imported — must be built from the mandatory templates in `templates/` (`tc_template.md` for cases, `bdd_template.md` for BDD). A case written from scratch without the template is invalid and must be regenerated from it.
- **NFRs must be numeric.** No "fast" or "acceptable" — use concrete thresholds (load time ≤ 3s, error rate ≤ 1%).
- **Only one Playwright MCP session at a time.** Browser state is shared; do not interleave sessions silently.
- **Never act on sensitive data.** Do not create, modify or delete production records without explicit written user approval.
- **This is a Spanish-language project.** Agent prompts and docs are primarily in Spanish. Maintain this convention.
