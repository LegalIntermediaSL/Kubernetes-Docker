# Helm Fullstack Demo

Chart Helm para desplegar la aplicación fullstack del curso:

- `web`: frontend con `nginx`
- `api`: backend Flask
- `redis`: contador simple

## Archivos principales

- `Chart.yaml`
- `values.yaml`
- `values-dev.yaml`
- `values-demo.yaml`
- `values-prod.yaml`
- `templates/`

## Render local

```bash
helm template fullstack-demo examples/helm/fullstack-demo
```

## Render por entorno

```bash
helm template fullstack-dev examples/helm/fullstack-demo -f examples/helm/fullstack-demo/values-dev.yaml
helm template fullstack-demo examples/helm/fullstack-demo -f examples/helm/fullstack-demo/values-demo.yaml
helm template fullstack-prod examples/helm/fullstack-demo -f examples/helm/fullstack-demo/values-prod.yaml
```

## Instalación

Antes de instalar en `kind`, carga las imágenes:

```bash
docker build -t fullstack-api:local examples/docker/fullstack-demo/api
docker build -t fullstack-web:local examples/docker/fullstack-demo/web
kind load docker-image fullstack-api:local --name curso-k8s
kind load docker-image fullstack-web:local --name curso-k8s
```

Instala el chart:

```bash
helm install fullstack-demo examples/helm/fullstack-demo -f examples/helm/fullstack-demo/values-dev.yaml
```

## Limpieza

```bash
helm uninstall fullstack-demo
```
