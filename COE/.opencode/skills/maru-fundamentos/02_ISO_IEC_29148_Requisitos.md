# ISO/IEC 29148 — Requisitos (Nivel 3)

> Requisitos del sistema y del software. Procesos de ciclo de vida.
> Última edición: **ISO/IEC/IEEE 29148:2018**.

## Especificaciones de requisitos

| Tipo | Contenido | Verificabilidad |
|---|---|---|
| **Stakeholder requirements** | Necesidades del stakeholder ("el usuario necesita X") | No verificable directamente |
| **System requirements** | Comportamiento del sistema | Verificable |
| **Software requirements** | Comportamiento del software | Verificable |

**Regla clave de gobernanza**: los requisitos de **nivel stakeholder no son verificables por prueba**. La trazabilidad hacia abajo solo puede iniciarse cuando se llega a requisitos de sistema/software verificables. Un hallazgo frecuente en auditoría: casos de prueba trazados a stakeholder requirements sin intermedios.

## Atributos obligatorios de un requisito (ISO/IEC/IEEE 29148)

1. **Único** (identificador)
2. **Completo** (una sola interpretación, sin ambigüedad)
3. **Consistente** (sin contradicciones con otros)
4. **Modificable** (con trazabilidad de cambios)
5. **Trazable** (origen → destino)
6. **Verificable** (hay forma de comprobarlo)
7. **No redundante**
8. **Priorizado** (negocio > usuario > calidad)
9. **Libre de ambigüedad**

## Defectos de requisitos frecuentes (hallazgos de auditoría)

| Defecto | Impacto | Acción correctiva |
|---|---|---|
| Ambigüedad ("rápido", "fácil", "robusto") | Tests no concluyentes | Sustituir por umbral medible |
| Sin criterio de aceptación | Cobertura no verificable | Añadir measurable (ver `03_Umbrales_y_Criterios.md`) |
| Requisito no trazable a fuente | Gap de análisis | Enlazar a stakeholder/usecase |
| Requisito no testeable | Defecto que se fuga a producción | Marcar como no-funcional o rediseñar |
| Requisito duplicado | Esfuerzo duplicado | Consolidar |

## Relación con pruebas

- Requisito de software verificable → debe tener al menos un caso de prueba.
- Cobertura de requisitos (requisitos con prueba / total) es métrica de auditoría.
- **Testability** es subcaracterística ISO/IEC 25010 §3.7.

## Referencias
- ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering
- ISO/IEC/IEEE 15288:2023 — Life cycle processes
- ISO/IEC/IEEE 12207:2017 — Life cycle processes (software)