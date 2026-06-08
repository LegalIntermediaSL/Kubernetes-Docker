# Registro, seguridad y troubleshooting Docker

Cuando una imagen deja de ser local, necesitas saber compartirla, versionarla, endurecerla y depurarla.

## Publicar imágenes

Flujo habitual con Docker Hub:

```bash
docker login
docker tag mi-api:local usuario/mi-api:0.1.0
docker push usuario/mi-api:0.1.0
```

## Etiquetado recomendado

Evita usar solo `latest`. Combina etiquetas con significado:

- `0.1.0`
- `2026-06-08`
- `main-abc123`

## Seguridad básica

- Usa imágenes base confiables.
- Minimiza paquetes instalados.
- No ejecutes como root si puedes evitarlo.
- No almacenes secretos en la imagen.
- Escanea vulnerabilidades periódicamente.

## Ejemplo de usuario no root

```dockerfile
RUN useradd -r -u 1001 appuser
USER 1001
```

## Inspección y depuración

### Ver logs

```bash
docker logs <container_id>
docker logs -f <container_id>
```

### Entrar al contenedor

```bash
docker exec -it <container_id> sh
```

### Ver consumo

```bash
docker stats
```

### Ver configuración completa

```bash
docker inspect <container_id>
```

## Errores comunes y cómo pensarlos

### "Container exited immediately"

Suele significar que el proceso principal terminó. Revisa:

- `CMD`
- argumentos
- variables de entorno
- logs

### "Port already allocated"

El puerto del host ya está en uso.

Soluciones:

- Cambiar el puerto del host
- Parar el proceso que lo usa

### "Module not found" o dependencias ausentes

Probablemente el `Dockerfile` no copió o instaló algo necesario.

### "Works on my machine"

Puede que el build local esté usando caché o archivos no contemplados en el `Dockerfile`.

## Checklist antes de publicar

- La imagen construye desde cero.
- El contenedor arranca sin intervención manual.
- Los puertos y variables están documentados.
- No hay secretos en commits ni capas.
- Existe una estrategia básica de versionado.

## Puente hacia Kubernetes

En despliegues reales en Kubernetes, publicar imágenes de forma limpia importa mucho porque el clúster necesita descargarlas desde un registry accesible.
