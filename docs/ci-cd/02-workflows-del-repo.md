# Workflows del repositorio

Los workflows en `.github/workflows/` forman una CI mínima y educativa. No intentan cubrir todos los casos de un equipo grande, pero sí mostrar una base legible y útil.

## Workflows incluidos

- `ci.yml`: validaciones generales
- `docker-build.yml`: builds de imágenes principales
- `helm-validate.yml`: lint y render de charts
- `publish-images.yml`: publicacion versionada en GHCR a partir de tags Git

## Qué enseñan

- cómo validar antes de desplegar
- cómo detectar roturas de YAML o Helm
- cómo asegurar que ejemplos importantes siguen construyendo

## Qué comprueba cada workflow

- `ci.yml` valida notebooks JSON, manifiestos YAML, configuración Compose y ejemplos Python.
- `docker-build.yml` comprueba que las imágenes principales del curso siguen construyendo.
- `helm-validate.yml` ejecuta `helm lint` y `helm template` sobre los charts más importantes del repositorio.
- `publish-images.yml` construye y publica imágenes etiquetadas cuando el repositorio recibe un tag `v*`.
