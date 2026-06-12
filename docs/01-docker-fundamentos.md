# Fundamentos de Docker

Docker gira alrededor de una idea muy poderosa: convertir una aplicación en una unidad portable y reproducible.

## Flujo mental básico

El flujo más habitual es este:

1. Escribes un `Dockerfile`.
2. Construyes una imagen con `docker build`.
3. Ejecutas un contenedor con `docker run`.
4. Inspeccionas logs, puertos y procesos.

## Imagen vs contenedor

Conviene distinguirlos muy bien:

- La `imagen` es el molde.
- El `contenedor` es la instancia viva.

Puedes lanzar muchos contenedores a partir de la misma imagen.

## Comandos esenciales

### Construir una imagen

```bash
docker build -t hola-nginx:local examples/docker/hola-nginx
```

### Ejecutar un contenedor

```bash
docker run --rm -p 8080:80 hola-nginx:local
```

### Ver contenedores en ejecución

```bash
docker ps
```

### Ver todas las imágenes locales

```bash
docker images
```

### Parar un contenedor

Si el contenedor está corriendo en primer plano, puedes detenerlo con `Ctrl+C`.

Si está en segundo plano:

```bash
docker stop <container_id>
```

## Anatomía de un Dockerfile

En este repositorio usamos un ejemplo muy pequeño basado en `nginx`:

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

Qué significa cada línea:

- `FROM`: imagen base.
- `COPY`: copia archivos del proyecto dentro de la imagen.
- `EXPOSE`: documenta el puerto que usa la aplicación.

## Buenas prácticas iniciales

- Empieza con imágenes base pequeñas si tiene sentido.
- Mantén el contexto de build lo más limpio posible.
- No metas secretos dentro de la imagen.
- Intenta que la imagen haga una sola cosa bien.

## Ejercicio guiado

1. Construye la imagen `hola-nginx:local`.
2. Levanta el contenedor en el puerto `8080`.
3. Abre `http://localhost:8080`.
4. Cambia el contenido de `index.html`.
5. Reconstruye la imagen y repite la prueba.

## Qué aprender antes de seguir

Antes de pasar a Kubernetes, asegúrate de que ya controlas estas ideas:

- Diferencia entre imagen y contenedor
- Qué hace `docker build`
- Qué hace `docker run`
- Cómo publicar puertos con `-p`

## Siguientes módulos de Docker

Cuando este documento ya te resulte natural, continúa con:

- [Arquitectura y CLI de Docker](docker/02-arquitectura-y-cli.md)
- [Dockerfiles y buenas prácticas](docker/03-dockerfiles-y-buenas-practicas.md)
- [Volúmenes, redes y persistencia](docker/04-volumenes-redes-y-persistencia.md)
- [Docker Compose](docker/05-docker-compose.md)
- [Registro, seguridad y troubleshooting](docker/06-registry-seguridad-troubleshooting.md)
- [Tutorial detallado de Docker](docker/07-tutorial-docker-paso-a-paso.md)
- [Versionado y publicacion de imagenes](docker/08-versionado-y-publicacion.md)
- [Seguridad de contenedores y hardening](docker/09-seguridad-de-contenedores-y-hardening.md)
- [BuildKit, multi-stage y optimizacion](docker/10-buildkit-multi-stage-y-optimizacion.md)
- [Debugging de runtime, redes y señales](docker/11-debugging-runtime-redes-y-senales.md)
- [Volumenes, backup y limpieza operativa](docker/12-volumenes-backup-y-limpieza-operativa.md)
