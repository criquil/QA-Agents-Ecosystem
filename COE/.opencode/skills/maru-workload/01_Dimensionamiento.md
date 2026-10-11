# Dimensionamiento (Nivel 3)

## 1. Recopilar datos de producción
- Analytics web (Google Analytics, Adobe).
- APM (Datadog, New Relic, Dynatrace): throughput real por endpoint.
- Logs de servidor: peticiones/segundo por franja horaria.
- Entrevistas con negocio: proyecciones de crecimiento y eventos (black friday, balance).

## 2. Calcular carga objetivo

```
TPS_objetivo = TPS_actual_peak × factor_proyección
VUs = TPS_objetivo × think_time_segundos
```

Ejemplo:
- TPS peak actual = 500
- Proyección 6 meses = ×1.5
- TPS objetivo = 750
- Think time medio = 4s
- VUs = 750 × 4 = 3000 usuarios concurrentes

## 3. Validar capacidad del generador
- Ejecutar prueba de calibración: 500 VU, 2 min, medir latencia del propio generador.
- Si latencia del generador >50ms → distribuir carga en múltiples instancias.

## 4. Supuestos a documentar
Cuando no hay datos de producción, declarar:
- Usuarios activos concurrentes estimados.
- Distribución de journeys (qué porcentaje hace login vs checkout).
- Think time por journey.
- Picos eventos de negocio.

## Errores frecuentes
- Usar el número total de usuarios registrados en vez de concurrentes.
- No considerar journeys (un usuario = múltiples requests).
- Ignorar tráfico de background jobs y APIs internas.