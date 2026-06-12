# Python API Optimized

Variante de la `python-api` pensada para practicar:

- `BuildKit`
- `multi-stage build`
- comparacion de capas
- usuario no root en runtime

## Archivos

- `Dockerfile`
- `.dockerignore`
- `app.py`
- `requirements.txt`

## Uso

```bash
DOCKER_BUILDKIT=1 docker build -t python-api:optimized examples/docker/python-api-optimized
docker run --rm -p 8001:8000 python-api:optimized
```

## Comparacion sugerida

```bash
docker build -t python-api:baseline examples/docker/python-api
docker image ls | grep python-api
docker history python-api:baseline
docker history python-api:optimized
```
