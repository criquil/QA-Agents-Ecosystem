---
name: kb-01-recopilacion-de-requisitos-manual
description: Skill autónoma de conocimiento sobre recopilación de requisitos para pruebas manuales. No depende de archivos externos.
---

# Recopilación de Requisitos para Pruebas Manuales

## Dimensiones de Requisitos

### 1. Sistema Bajo Prueba (SUT)
- Nombre y descripción del sistema
- Tipo de aplicación (e-commerce, banca, ERP, portal interno, SaaS)
- Módulos y funcionalidades principales
- Flujos críticos de negocio y su frecuencia de uso
- Roles de usuario (admin, operador, cliente, auditor, invitado)
- Plataformas y navegadores soportados
- Idiomas, locales, monedas y formatos de fecha
- Integraciones visibles al usuario (pago, SSO, correo, SMS, mapas, chat)

### 2. Objetivos de Testing
- Tipos de prueba manual requeridos (funcionales, sistema, regresión, smoke, sanity, exploratorias, UAT)
- Cobertura mínima objetivo (%)
- Criterios de aceptación numéricos (tiempo de carga, tasa de error)
- Matriz de compatibilidad obligatoria
- Requisitos de accesibilidad (WCAG 2.1 AA, teclado, contraste)

### 3. Contexto del Equipo
- Tamaño y experiencia del equipo de QA manual
- Gestor de casos y defectos (Jira, TestRail, Zephyr, Xray, hoja de cálculo)
- Disponibilidad del usuario de negocio para UAT y su ventana de tiempo
- Ventanas permitidas de ejecución y congelamiento de build
- Proceso de reporte y escalamiento de defectos

### 4. Datos de Prueba
- Catálogo de cuentas de prueba por rol y su vigencia
- Datos semilla requeridos por cada flujo
- Datos que deben crearse durante la sesión
- Datos sensibles (PII, tarjetas) y su tratamiento
- Proceso de reset y de cleanup del entorno

### 5. Entorno y Herramienta
- Entorno objetivo y URL base
- Build/versión a probar y cómo verificarla en la UI
- Navegador objetivo y modo headless/headed
- Evidencia exigida (screenshot, video, traza, PDF, consola, red)
- Restricciones de acceso (VPN, MFA, captcha, IP allowlist)

## Preguntas Tipo

1. ¿Cuáles son los 3 flujos de negocio más críticos y cada cuánto se usan?
2. ¿Qué roles de usuario existen y qué se espera que pueda (y no pueda) hacer cada uno?
3. ¿Cuál es el entorno de pruebas y qué build está desplegado ahí?
4. ¿Qué criterios de aceptación usaría el negocio para firmar el pase a producción?
5. ¿Qué datos y cuentas ya existen y cuáles hay que crear?
6. ¿Qué navegadores y resoluciones son obligatorios?
7. ¿Qué evidencia exige el proceso de aprobación?

## Criterios de calidad de un requisito

- **Completo**: incluye el flujo feliz, los casos negativos y los límites.
- **Consistente**: no contradice otro requisito.
- **Verificable**: un tester humano puede decidir si pasó o falló observando la UI.
- **Trazable**: tiene un identificador que permite ligarlo a un caso de prueba.
- **Acordado**: validado por negocio y por tecnología.
