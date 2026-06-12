# Volumenes, backup y limpieza operativa

Los datos locales suelen ser el punto donde una demo pasa de ser efimera a empezar a parecerse a un sistema real.

Este modulo completa la parte de persistencia en Docker con una mirada mas operativa:

- donde viven los datos
- como hacer una copia simple
- como limpiar sin borrar lo importante por accidente

## Que problema resuelve este bloque

Sin una idea clara de persistencia local:

- confundes imagen con datos
- borras volúmenes al limpiar contenedores
- no sabes hacer un backup sencillo antes de tocar algo

## Mapa mental

```mermaid
flowchart LR
    APP["Contenedor"] --> VOL["Volumen nombrado"]
    VOL --> BK["Backup .tgz"]
    BK --> REST["Restore a otro volumen"]
```

## Imagen, contenedor y volumen no son lo mismo

- la imagen describe el filesystem base
- el contenedor es la instancia en ejecucion
- el volumen guarda datos fuera del ciclo de vida del contenedor

Eso explica por que puedes:

- borrar un contenedor
- crear otro desde la misma imagen
- y seguir viendo los datos si el volumen es el mismo

## Bind mount vs volumen nombrado

### Bind mount

Ventajas:

- ves los archivos directamente en tu host
- muy util para desarrollo interactivo

Limites:

- mas dependiente de rutas del host
- menos portable

### Volumen nombrado

Ventajas:

- mas limpio para datos de aplicacion
- mas portable entre maquinas y proyectos

Limites:

- no ves tan facilmente la ruta real en el host

## Ejemplo del repositorio

Revisa:

- `examples/docker/volume-backup-demo/docker-compose.yml`
- `examples/docker/volume-backup-demo/README.md`

El laboratorio usa:

- un servicio `writer`
- un volumen nombrado
- un flujo de backup a `.tgz`
- un restore sobre otro volumen

## Recorrido recomendado

### 1. Levantar el escritor

```bash
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml up -d
```

### 2. Ver que el volumen recibe datos

```bash
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml logs -f
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml exec writer sh
```

### 3. Crear un backup simple

```bash
docker run --rm \
  -v course-volume-backup-demo-data:/source \
  -v "$PWD/examples/docker/volume-backup-demo":/backup \
  busybox:1.36 \
  sh -c 'tar -czf /backup/demo-data.tgz -C /source .'
```

### 4. Restaurar a otro volumen

```bash
docker volume create course-volume-backup-restore
docker run --rm \
  -v course-volume-backup-restore:/target \
  -v "$PWD/examples/docker/volume-backup-demo":/backup \
  busybox:1.36 \
  sh -c 'tar -xzf /backup/demo-data.tgz -C /target'
```

## Limpieza con criterio

Comandos utiles:

```bash
docker volume ls
docker volume inspect course-volume-backup-demo-data
docker system df
```

Limpieza parcial:

```bash
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml down
```

Limpieza con borrado del volumen:

```bash
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml down -v
```

Hay una diferencia enorme entre ambas.

## Mucho cuidado con `prune`

Comandos como:

```bash
docker system prune
docker volume prune
```

son utiles, pero hay que ejecutarlos entendiendo que pueden borrar datos o caches que aun necesitas.

## Errores frecuentes

### Pensar que reconstruir una imagen recupera los datos

No los recupera si vivian en un volumen borrado.

### Usar `down -v` por costumbre

En demos pequeñas parece inocente, pero en un entorno con datos ya no lo es.

### No probar el restore

Un backup no comprobado vale mucho menos de lo que parece.

## Conexiones importantes

- [Volúmenes, redes y persistencia](04-volumenes-redes-y-persistencia.md)
- [Docker Compose](05-docker-compose.md)
- [Backup, restore y disaster recovery](../kubernetes/29-backup-restore-y-disaster-recovery.md)
