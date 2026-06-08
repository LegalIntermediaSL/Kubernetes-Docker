# Fullstack Demo con Docker Compose

Este laboratorio levanta tres servicios:

- `web`: frontend estático servido con `nginx`
- `api`: backend Flask
- `redis`: contador persistente

## Arquitectura

```mermaid
flowchart LR
    U["Navegador"] --> W["web"]
    W --> A["api"]
    A --> R["redis"]
```

## Puesta en marcha

```bash
docker-compose -f examples/docker/fullstack-demo/docker-compose.yml up --build
```

## Endpoints

- `http://localhost:8080`
- `http://localhost:8000/api`
- `http://localhost:8000/api/health`
- `http://localhost:8000/api/stats`

## Pruebas útiles

```bash
curl -s http://localhost:8000/api
curl -s http://localhost:8000/api/health
curl -s -X POST http://localhost:8000/api/visits
curl -s http://localhost:8000/api/stats
```

## Reinicio del contador

```bash
curl -s -X POST \
  -H "X-Reset-Token: reset-demo" \
  http://localhost:8000/api/reset
```

## Limpieza

```bash
docker-compose -f examples/docker/fullstack-demo/docker-compose.yml down
```

Si quieres eliminar también el volumen persistente:

```bash
docker-compose -f examples/docker/fullstack-demo/docker-compose.yml down -v
```
