# Introducción a CI/CD

Este bloque describe cómo el repositorio empieza a pasar de “curso con ejemplos” a “curso con validación automatizada”.

## Objetivo

Enseñar una progresión simple:

- validar archivos
- construir imágenes
- validar charts y Compose
- preparar el terreno para promoción por entorno

## Qué se automatiza aquí

- parseo YAML
- validación de notebooks JSON
- `docker-compose config`
- `helm lint`
- `helm template`
- builds Docker principales
- publicacion versionada de imagenes

## Relación con el curso

Estos pasos no sustituyen la práctica manual. La complementan.

## Continuidad recomendada

Para seguir el flujo completo de este repositorio:

1. empieza por esta introduccion
2. revisa los workflows reales en [Workflows del repositorio](02-workflows-del-repo.md)
3. conecta despues con [Publicacion, promocion y releases](03-publicacion-promocion-y-releases.md)
