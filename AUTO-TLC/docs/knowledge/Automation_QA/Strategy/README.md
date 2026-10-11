# Estrategia de Automation QA

> **Misión:** Definir estrategias, arquitectura y estándares para automatización de testing

---

## Estructura de Estrategia

```
Strategy/
├── README.md                    # Este archivo
├── Boilerplate/                 # Plantillas y templates
├── POM/                         # Page Object Model
│   └── README.md               # Reglas POM (framework-agnostic)
├── Selectors_Strategy/          # Estrategia de selectores
│   └── README.md               # Estrategia de localización con prioridad
├── Test_Categorization/         # Categorización y Tags
│   └── README.md               # Tags obligatorios para CI/CD
├── Data_Parametrization/        # Parametrización de datos
│   └── README.md               # Datos obligatorios desde archivos externos
└── Troubleshooting/             # Guía de troubleshooting
    └── README.md               # Lecciones aprendidas y patrones de solución
```

---

## Principios Fundamentales

### 1. Separación de Responsabilidades

```
✅ Pages: Solo interacción con UI
✅ Tests: Solo lógica de negocio
✅ Selectors: Solo localización de elementos
✅ Base: Solo funcionalidad compartida
```

### 2. Herencia vs Composición

```
✅ Usar composición sobre herencia
✅ BasePage como foundation
✅ Page Objects como composición
✅ Tests como orquestadores
```

### 3. Naming Conventions

```
✅ Pages: [Page].page.ts
✅ Selectors: [Page].selectors.ts
✅ Tests: [feature].[scenario].ts
✅ Base: Base[Type].ts
```

---

## Flujo de Trabajo

```
1. Definir Selectors
   ↓
2. Crear Page Object
   ↓
3. Implementar Tests
   ↓
4. Ejecutar y verificar
   ↓
5. Mantener y refactorizar
```

---

## Navegación

- **POM:** [POM/README.md](POM/README.md) - Page Object Model (framework-agnostic)
- **Boilerplate:** [Boilerplate/](Boilerplate/) - Plantillas y templates
- **Selectors:** [Selectors_Strategy/](Selectors_Strategy/) - Estrategia de localización
- **Test Categorization:** [Test_Categorization/](Test_Categorization/) - Tags obligatorios para CI/CD
- **Data Parametrization:** [Data_Parametrization/](Data_Parametrization/) - Datos obligatorios desde archivos externos
- **Troubleshooting:** [Troubleshooting/](Troubleshooting/) - Guía de troubleshooting y lecciones aprendidas

---

*MASTER-README - Automation Strategy*
