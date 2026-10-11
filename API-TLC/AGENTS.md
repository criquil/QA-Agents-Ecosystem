# AGENTS.md

## What This Repo Is

This is a **knowledge base + agent configuration repository** for the **Intelligent API Test Orchestrator (API-TLC v1.0)**. It is NOT a traditional code project — there are no build commands, tests, or CI pipelines to run.

The repo defines:
- **1 orchestrator agent** (`.opencode/agents/api-tlc-orchestrator-api.agent.md`) — the single entry point
- **21 skills** (`.opencode/skills/`) — 6 phase skills (one per API-TLC phase) + 15 support/conversion skills

All process knowledge lives inside the skills. There is no external documentation tree to ingest: skills are loaded on demand, only when the phase or task requires them.

## Agent Architecture (API-TLC v1.0)

The orchestrator (`api-tlc-orchestrator-api`, conversational name **APU**) is the ONLY agent. It executes the 6 phases in strict order by loading one skill per phase:

```
1. skill api-tlc-intake-api         → Requirements gathering + single tool selection
2. skill api-tlc-diagnostics-api    → Environment readiness, risks, contract validation
3. skill api-tlc-procedure-plan-api → Test types, scenarios, test data strategy
4. skill api-tlc-test-plan-api      → Formal test plan document (ISTQB/IEEE-829)
5. skill api-tlc-execution-api      → Script generation + test execution
6. skill api-tlc-analysis-api       → Metrics, RCA, report with verdict (PASSED/CONDITIONAL/FAILED)
```

Support skills are loaded only when a phase requires them:
- Phase 1/3: `api-tool-selector`, `api-test-strategy`
- Phase 4/6: `api-metrics-analysis`, `api-diagnostics-rca`
- Phase 5: the selected tool's workflow skill (`restsharp-api-workflow`, `karate-api-workflow`, `playwright-api-workflow`, `rest-assured-api-workflow`)

Conversion skills (independent, usable standalone):
- `export-response-to-openapi` — JSON → OpenAPI contract
- `openapi-to-response-example` — OpenAPI → JSON example
- `generate-api-test-matrix` — Requirements + OpenAPI → test matrix
- `develop-detailed-test-cases` — Matrix → detailed test cases
- `export-test-cases-to-gherkin` — Detailed cases → Gherkin .feature
- `generate-test-artifacts` — Detailed cases → multi-format (Bruno, Postman, Karate, RestSharp, Playwright, REST Assured)
- `import-collection` — OpenAPI/Bruno/Postman → coded tests (4 frameworks)

## Key Conventions

### v1.0 Defaults
- **Single tool** by default: RestSharp, Karate, Playwright, or REST Assured — never multi-tool unless explicitly requested
- **Sequential execution** — parallel only if `parallel: true` is explicitly requested
- **3 analysis modes**: `individual` (current run), `vs_baseline` (compare to saved baseline), `vs_other_runs` (compare to prior runs)
- Plan state persists in `tests/{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/plan.yaml`

### File Locations (Obligatorio)
- **Plan state**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/plan.yaml`
- **Context envelope**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/context_envelope.json`
- **Test plan doc**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/performance-test-plan.md`
- **Test scripts**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/scripts/`
- **Test data**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/data/`
- **Test results**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/reports/reports_{datestamp}_{iteration}/`
- **Analysis report**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/reports/reports_{datestamp}_{iteration}/00_API-test-report.md`
- **Metrics report**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/reports/reports_{datestamp}_{iteration}/01_metrics-kpis-report.md`
- **RCA report**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/reports/reports_{datestamp}_{iteration}/03_rca-report.md`
- **Executive report**: `tests/{ApplicationName}/{Environment}/{selected_tool}/{project_name}/reports/reports_{datestamp}_{iteration}/05_executive-report.md`

### Tool Selection Rules
When selecting a tool, follow this decision matrix:
- **RestSharp**: .NET/C# teams, HTTP/REST, xUnit/NUnit
- **Karate**: BDD, multi-protocol (HTTP/gRPC/GraphQL), reporting
- **Playwright**: JS/TS teams, API + browser testing
- **REST Assured**: Java teams, Given/When/Then, Allure reports

## Pitfalls

- **Never execute a phase without loading its skill.** The phase skills (`api-tlc-*-api`) carry the workflow, output format, and rules for each phase. Do not improvise outside them.
- **Never skip the smoke test.** Execution always runs smoke first; if it fails, stop.
- **Never mark a phase complete without user confirmation** for execution-related decisions (especially phase 5).
- **Plan state is in `tests/{ApplicationName}/{Environment}/{selected_tool}/{plan_id}/`**, not in `.opencode/` or `docs/`. The `.opencode/todo.md` is for OpenCode session tracking, not API-TLC plan state.
- **NFRs must be numeric.** No "fast" or "acceptable" — use concrete thresholds (p95 ≤ 200ms, error rate ≤ 1%). Default targets live in the `api-metrics-analysis` skill.
- **This is a Spanish-language project.** Agent prompts and skill content are primarily in Spanish. Maintain this convention.
- **Load skills on demand.** Do not load support skills a phase does not need — avoid unnecessary token consumption.
- **NO usar `docs/` para planes.** La estructura obligatoria está en `tests/{ApplicationName}/{Environment}/{selected_tool}/` — ver `PROJECT_STRUCTURE.md`.
