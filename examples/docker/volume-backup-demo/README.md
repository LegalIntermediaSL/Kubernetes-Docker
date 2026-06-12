# Volume Backup Demo

Laboratorio para practicar persistencia local, backup y restore sobre un volumen Docker nombrado.

## Archivos

- `docker-compose.yml`

## Uso

```bash
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml up -d
docker compose -f examples/docker/volume-backup-demo/docker-compose.yml logs -f
```

## Backup simple

```bash
docker run --rm \
  -v course-volume-backup-demo-data:/source \
  -v "$PWD/examples/docker/volume-backup-demo":/backup \
  busybox:1.36 \
  sh -c 'tar -czf /backup/demo-data.tgz -C /source .'
```

## Restore a otro volumen

```bash
docker volume create course-volume-backup-restore
docker run --rm \
  -v course-volume-backup-restore:/target \
  -v "$PWD/examples/docker/volume-backup-demo":/backup \
  busybox:1.36 \
  sh -c 'tar -xzf /backup/demo-data.tgz -C /target'
```
