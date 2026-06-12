# Runtime Debug Demo

Laboratorio pequeño para practicar diagnostico de runtime y señales.

## Archivos

- `Dockerfile`
- `entrypoint.sh`

## Uso

```bash
docker build -t runtime-debug-demo:local examples/docker/runtime-debug-demo
docker run --name runtime-debug-demo -e APP_MODE=debug runtime-debug-demo:local
```

## Comandos utiles

```bash
docker logs -f runtime-debug-demo
docker inspect runtime-debug-demo
docker exec -it runtime-debug-demo sh
docker top runtime-debug-demo
docker stop runtime-debug-demo
```
