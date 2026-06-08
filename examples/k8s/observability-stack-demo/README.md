# Observability Stack Demo

Recursos de referencia para desplegar `kube-prometheus-stack` y conectar la `python-api` del curso con metricas, alertas y dashboard.

## Archivos

- `kube-prometheus-stack-values.yaml`
- `python-api-service-monitor.yaml`
- `python-api-prometheus-rule.yaml`
- `grafana-dashboard-python-api.yaml`

## Flujo sugerido

1. desplegar `python-api`
2. instalar `kube-prometheus-stack`
3. aplicar `ServiceMonitor`, `PrometheusRule` y dashboard
