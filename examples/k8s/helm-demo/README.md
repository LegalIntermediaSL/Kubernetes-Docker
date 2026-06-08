# Helm Demo

Chart mínimo para desplegar la API Python del curso con Helm.

## Requisitos

- `helm`
- un clúster local si quieres instalarlo
- imagen `python-api:local` disponible si quieres ejecutarlo con `kind`

## Flujo recomendado

### Renderizar sin instalar

```bash
helm template python-api-demo examples/k8s/helm-demo
```

### Cambiar valores

```bash
helm template python-api-demo examples/k8s/helm-demo --set replicaCount=3
```

### Instalar en clúster local

```bash
docker build -t python-api:local examples/docker/python-api
kind load docker-image python-api:local --name curso-k8s
helm install python-api-demo examples/k8s/helm-demo
kubectl get deployments
kubectl get services
```

### Limpiar

```bash
helm uninstall python-api-demo
```
