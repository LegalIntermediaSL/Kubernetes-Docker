# Fullstack Demo en Kubernetes

Este laboratorio despliega la misma idea del demo de Compose:

- `web`: frontend con `nginx`
- `api`: backend Flask
- `redis`: almacenamiento del contador

## Requisitos

- Docker
- `kubectl`
- `kind`

## Construcción de imágenes

```bash
docker build -t fullstack-api:local examples/docker/fullstack-demo/api
docker build -t fullstack-web:local examples/docker/fullstack-demo/web
kind load docker-image fullstack-api:local --name curso-k8s
kind load docker-image fullstack-web:local --name curso-k8s
```

## Despliegue

```bash
kubectl apply -f examples/k8s/fullstack-demo/
```

## Verificación

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress
```

## Acceso local

```bash
kubectl port-forward service/web 8080:80
```

La aplicación quedará en:

- `http://localhost:8080`

## Pruebas de la API desde el frontend o con curl

```bash
curl -s http://localhost:8080/api
curl -s http://localhost:8080/api/health
curl -s -X POST http://localhost:8080/api/visits
curl -s http://localhost:8080/api/stats
```

## Limpieza

```bash
kubectl delete -f examples/k8s/fullstack-demo/
```
