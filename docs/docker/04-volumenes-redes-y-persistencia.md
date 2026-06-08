# Volúmenes, redes y persistencia

Cuando los contenedores dejan de ser un ejemplo trivial, aparecen dos preguntas inevitables:

- Dónde vive la información persistente
- Cómo se comunican los servicios

## Volúmenes

Los volúmenes desacoplan datos y contenedor.

### Crear un volumen

```bash
docker volume create datos-demo
```

### Usarlo en un contenedor

```bash
docker run --rm -v datos-demo:/data alpine sh -c "echo hola > /data/mensaje.txt"
```

### Ver volúmenes

```bash
docker volume ls
docker volume inspect datos-demo
```

## Bind mounts

Montan una carpeta del host dentro del contenedor:

```bash
docker run --rm -v "$PWD":/workspace python:3.12-slim ls /workspace
```

Útiles para desarrollo, pero menos portables que los volúmenes gestionados.

## Cuándo usar cada uno

- `volumes`: persistencia gestionada por Docker
- `bind mounts`: desarrollo local, live reload, compartir código
- `tmpfs`: datos temporales en memoria

## Redes Docker

Por defecto Docker crea redes bridge. También puedes crear redes propias:

```bash
docker network create app-net
```

Lanzar dos contenedores en la misma red:

```bash
docker run -d --name web --network app-net nginx:alpine
docker run --rm --network app-net alpine ping -c 2 web
```

## Resolución por nombre

Dentro de una red Docker, los contenedores pueden hablar por nombre si comparten esa red. Esto simplifica mucho aplicaciones multi-servicio.

## Ejemplo mental típico

- `api` escucha en `8000`
- `db` escucha en `5432`
- `nginx` hace proxy hacia `api`

Todos esos servicios se conectan por una red común, sin usar `localhost` entre contenedores.

## Persistencia en bases de datos

Si corres PostgreSQL o MySQL sin volumen, perderás los datos al borrar el contenedor.

Ejemplo:

```bash
docker run -d \
  --name postgres-demo \
  -e POSTGRES_PASSWORD=demo \
  -v pgdata-demo:/var/lib/postgresql/data \
  postgres:16
```

## Problemas frecuentes

- Usar `localhost` dentro del contenedor para llegar a otro contenedor.
- Montar un bind mount que sobrescribe archivos generados en la imagen.
- Dar por hecho que los datos persisten sin volumen.
- Reutilizar puertos del host que ya están ocupados.

## Relación con Kubernetes

Estos conceptos se trasladan luego a Kubernetes:

- Volumen Docker -> volumen/PVC
- Red entre contenedores -> networking del pod y del cluster
- Variables de entorno -> ConfigMaps y Secrets

## Práctica sugerida

1. Crea una red `curso-net`.
2. Ejecuta una API y un cliente en esa red.
3. Monta un volumen para persistir archivos generados.
4. Borra y vuelve a crear el contenedor.
5. Comprueba qué datos permanecen.
