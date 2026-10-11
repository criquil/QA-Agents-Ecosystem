# Cheat Sheet — Fundamentos de Gobernanza (consulta rápida)

## ISO/IEC 25010:2023 — 9 características de calidad
functional suitability · performance efficiency · compatibility · interaction capability · reliability · security · maintainability · flexibility · safety

⚠️ **No usar** la nomenclatura 2011: *usability* → ahora es *quality-in-use* (ISO/IEC 25019) y aparece *interaction capability* en el modelo de producto. *Portability* → ahora *flexibility*.

## ISO 9001:2015 — cláusulas queimportan al QA
§6.1 riesgos · §7.5 información documentada · §8.x operación · §9.2 auditoría interna · §9.3 revisión por dirección · §10.2 no conformidades y acción correctiva (CAPA)

## ISO/IEC 27001:2022 — control de seguridad
Anexo A: organizacionales (37) · personas (8) · físicos (14) · **tecnológicos (34)** → §8.25-8.29 secure development

## Certificaciones
## ISO 9001:2015 — clausulas que importan al QA
- **CMMI**: niveles 1-5 (Initial→Managed→Defined→Quant Managed→Optimizing). Procesos organizacionales.
- **TMMi**: niveles 1-5. Madurez específica de testing.

## Buenas prácticas
- **Agile Testing**: 4 cuadrantes; testing no es una fase; automation ≠ testing.
- **DevSecOps**: SAST/DAST/SCA/IAST/SBOM integrated en CI con quality gates.
- **DAMA-DMBOK2**: 11 knowledge areas, KA5 Data Quality, KA6 Data Governance.

## Triple enlace (regla clave de auditoría)
```
ISO/IEC 27001  → qué debe protegerse
OWASP          → cómo verificar
ISO/IEC 25010 §3.6 → cómo medir (Security)
```
