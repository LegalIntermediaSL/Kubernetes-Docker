# Compose Web + API

Este ejemplo levanta dos servicios:

- `api`: una API Flask simple
- `web`: un `nginx` que hace proxy a la API

## Uso

```bash
docker compose up --build
```

## Endpoints

- `http://localhost:8000/`
- `http://localhost:8000/health`
- `http://localhost:8080/`
