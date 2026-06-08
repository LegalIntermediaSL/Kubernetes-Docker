# Python API Helm Chart

Chart mas completo para desplegar la API Python con valores parametrizables, recursos e Ingress opcional.

## Requisitos

- `helm`
- imagen `python-api:local` o una imagen publicada en registry
- cluster local si quieres instalarlo de verdad

## Render rapido

```bash
helm template python-api examples/helm/python-api
```

## Render por entorno

```bash
helm template python-api-dev examples/helm/python-api -f examples/helm/python-api/values-dev.yaml
helm template python-api-demo examples/helm/python-api -f examples/helm/python-api/values-demo.yaml
helm template python-api-prod examples/helm/python-api -f examples/helm/python-api/values-prod.yaml
```

## Instalacion local

```bash
docker build -t python-api:local examples/docker/python-api
kind load docker-image python-api:local --name curso-k8s
helm install python-api examples/helm/python-api -f examples/helm/python-api/values-dev.yaml
kubectl get deployments
kubectl get services
```

## Upgrade de version

```bash
helm upgrade python-api examples/helm/python-api --set image.tag=0.2.0
```

## Rollback

```bash
helm history python-api
helm rollback python-api 1
```
