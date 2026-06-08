# Python API en Kubernetes

Este ejemplo despliega la API Flask del directorio `examples/docker/python-api/` en un cluster local.

## Flujo recomendado

1. Construir la imagen local:

```bash
docker build -t python-api:local examples/docker/python-api
```

2. Cargar la imagen en `kind`:

```bash
kind load docker-image python-api:local --name curso-k8s
```

3. Aplicar los manifiestos:

```bash
kubectl apply -f examples/k8s/python-api/
```

4. Exponer el servicio localmente:

```bash
kubectl port-forward service/python-api 8000:80
```

5. Probar la API:

```bash
curl -s http://localhost:8000/
curl -s http://localhost:8000/health
curl -s http://localhost:8000/metrics
```

## Endpoints utiles

- `/`: respuesta principal
- `/health`: sonda de salud
- `/metrics`: metricas Prometheus basicas para los laboratorios de observabilidad
