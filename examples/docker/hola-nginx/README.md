# Hola Nginx

Ejemplo mínimo para construir una imagen propia y servir una página estática con `nginx`.

## Archivos

- `Dockerfile`
- `index.html`

## Construcción

```bash
docker build -t hola-nginx:local examples/docker/hola-nginx
```

## Ejecución

```bash
docker run --rm -p 8080:80 hola-nginx:local
```

## Verificación

- Abre `http://localhost:8080`
- O prueba con:

```bash
curl -s http://localhost:8080
```

## Qué practicar

- Diferencia entre imagen y contenedor.
- Copia de archivos al filesystem de la imagen.
- Exposición de puertos.

## Continuidad

Este mismo ejemplo reaparece en [examples/k8s/hola-nginx/README.md](../../k8s/hola-nginx/README.md) para explicar el salto de Docker a Kubernetes.
