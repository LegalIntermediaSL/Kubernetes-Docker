# KEDA Demo

Laboratorio para practicar autoscaling con KEDA usando dos rutas:

- `cron`, para activar o apagar segun horario
- `prometheus`, para escalar por una metrica externa

## Archivos

- `namespace.yaml`
- `deployment.yaml`
- `service.yaml`
- `service-monitor.yaml`
- `scaledobject-cron.yaml`
- `scaledobject-prometheus.yaml`
- `traffic-generator-deployment.yaml`

## Nota

Antes de aplicar los `ScaledObject` necesitas tener instalado KEDA.

## Recomendacion

- usa `scaledobject-cron.yaml` si quieres un laboratorio simple y que pueda bajar a `0`
- usa `scaledobject-prometheus.yaml` si ya tienes la pila de observabilidad del repositorio levantada
- si tu release de Prometheus usa otro nombre de servicio, ajusta `serverAddress` en `scaledobject-prometheus.yaml`
- si varias apps exponen `python_api_requests_total`, ajusta tambien la `query`

No apliques los dos `ScaledObject` a la vez sobre el mismo `Deployment`.
