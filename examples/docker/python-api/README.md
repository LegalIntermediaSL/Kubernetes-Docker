# Python API

API Flask pequeña para practicar imágenes propias, variables de entorno y métricas básicas.

## Archivos

- `Dockerfile`
- `requirements.txt`
- `app.py`

## Construcción

```bash
docker build -t python-api:local examples/docker/python-api
```

## Ejecución

```bash
docker run --rm -p 8000:8000 python-api:local
```

## Endpoints

- `http://localhost:8000/`
- `http://localhost:8000/health`
- `http://localhost:8000/metrics`

## Variables de entorno

```bash
docker run --rm \
  -e APP_NAME="Curso Docker" \
  -e APP_ENV=demo \
  -e PORT=8000 \
  -p 8000:8000 \
  python-api:local
```

## Verificación

```bash
curl -s http://localhost:8000/
curl -s http://localhost:8000/health
curl -s http://localhost:8000/metrics | sed -n '1,10p'
```

## Continuidad

Esta API se reutiliza en:

- [examples/k8s/python-api/README.md](../../k8s/python-api/README.md)
- [examples/helm/python-api/README.md](../../helm/python-api/README.md)
- los laboratorios de observabilidad del repositorio
