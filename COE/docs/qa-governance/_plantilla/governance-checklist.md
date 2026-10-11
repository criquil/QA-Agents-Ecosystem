# Checklist de Gobernanza QA

> Verificar por disciplina. Marcar ✅ conforme · ⚠️ deviation · ❌ no conforme.

## Fundamentos
- [ ] Política de calidad publicada y vigente
- [ ] NFRs definidos con umbrales
- [ ] KPIs con dueño asignado
- [ ] Mapa de cumplimiento ISO/IEC 25010

## API Testing
- [ ] Contratos OpenAPI/Pact versionados
- [ ] Cobertura de endpoints críticos ≥ 95%
- [ ] OWASP API Top 10 validado en endpoints expuestos
- [ ] Pruebas de contrato ejecutadas en CI

## Manual Testing
- [ ] Casos de prueba trazables a requisitos
- [ ] Criterios de aceptación definidos por historia
- [ ] Exploración con charters registrados
- [ ] Cobertura de journeys críticos

## Automation Testing
- [ ] Framework estándar documentado (ADR)
- [ ] Quality gate en CI: coverage, lint, tests
- [ ] Flaky rate < 2%
- [ ] Tests independientes y paralelizables

## Performance Testing
- [ ] SLA/SLO por sistema crítico
- [ ] Modelo de carga derivado de datos de producción
- [ ] Prueba de saturación documentada
- [ ] Performance gate en CI para cambios críticos

## Accessibility
- [ ] Cumplimiento WCAG 2.2 AA verificado
- [ ] axe/Lighthouse en CI sin violaciones bloqueantes
- [ ] Pruebas manuales con teclado y lector de pantalla
- [ ] VPAT/ACR publicado

## Procesos SDLC
- [ ] Shift-Left: QA en refinamiento y diseño
- [ ] Code review con criterio de calidad
- [ ] Defect escape rate < 5%
- [ ] Retrospectivas con acciones de calidad

## Firma
**Revisor**: {} **Fecha**: {} **Veredicto**: {}