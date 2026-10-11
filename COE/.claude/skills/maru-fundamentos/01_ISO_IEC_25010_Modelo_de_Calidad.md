# ISO/IEC 25010 — Modelo de Calidad de Producto (Nivel 3)

> **Vigente**: ISO/IEC 25010:2023 (2ª edición, reemplaza a 2011).
> Pertenece a la familia **SQuaRE** (ISO/IEC 25000 a 25099).

## Las 9 características (2023)

| # | Característica (EN) | Traducción | Subcaracterísticas |
|---|---|---|---|
| 3.1 | Functional suitability | Idoneidad funcional | functional completeness, functional correctness, functional appropriateness |
| 3.2 | Performance efficiency | Eficiencia de desempeño | time behaviour, resource utilization, capacity |
| 3.3 | Compatibility | Compatibilidad | co-existence, interoperability |
| 3.4 | Interaction capability | Capacidad de interacción | appropriateness recognizability, learnability, operability, user error protection, **user engagement**, **inclusivity**, **user assistance**, **self-descriptiveness** |
| 3.5 | Reliability | Fiabilidad | faultlessness, availability, fault tolerance, recoverability |
| 3.6 | Security | Seguridad | confidentiality, integrity, non-repudiation, accountability, **authenticity**, **resistance** |
| 3.7 | Maintainability | Mantenibilidad | modularity, reusability, analysability, modifiability, testability, **changeability** |
| 3.8 | Flexibility | Flexibilidad | adaptability, scalability, **installability**, replaceability |
| 3.9 | Safety | Seguridad (operational) | operational constraint, risk identification, fail safe, hazard warning, safe integration |

## Cambios críticos 2011 → 2023

| 2011 | 2023 | Impacto en gobernanza |
|---|---|---|
| Usability | **Interaction capability** | Usability se movió al modelo *quality-in-use* (ISO/IEC 25019). No confundir. |
| Portability | **Flexibility** | Portabilidad → installability/replaceability/adaptability/scalability |
| — (no existía) | **Safety** agregada | Nueva característica completa: fail safe, hazard warning |
| Accessibility (subcaract.) | partida en **inclusivity** + **user assistance** | Alineado con ISO/IEC 25019 y WCAG |
| Maturity (fiabilidad) | **Faultlessness** | Renombrada |
| User interface aesthetics | **User engagement** | Renombrada |

## Reglas de aplicación

- **Todacharacteristic de calidad definida en el plan debe salir de este catálogo** (no inventar).
- Cada característica aplicable necesita: subcaracterística, métrica (ISO/IEC 2502x), umbral y criterio de aceptación.
- El modelo es de **producto**; el de **uso** es ISO/IEC 25019. No mezclarlos.
- Coexistencia vs interoperabilidad: coexistencia = compartir entorno; interoperabilidad = intercambiar información.

## Referencias
- ISO/IEC 25010:2023 — Product quality model (iso.org/standard/78176.html)
- ISO/IEC 25002:2023 — Quality models overview and usage
- ISO/IEC 25019:2023 — Quality-in-use model
- ISO/IEC 25030 — Uso de modelos para requisitos de calidad
- ISO/IEC 25040 — Uso de modelos para evaluación
- ISO/IEC/IEEE 12207 — Procesos de ciclo de vida
- ISO/IEC/IEEE 15288 — Procesos de ciclo de vida de sistemas