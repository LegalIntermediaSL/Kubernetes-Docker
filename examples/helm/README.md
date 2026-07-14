# Ejemplos Helm

Esta carpeta reúne los charts reutilizables del curso.

## Charts disponibles

- [python-api](python-api/README.md): chart parametrizable para la API Flask con `Service`, `ConfigMap`, recursos e `Ingress` opcional.
- [fullstack-demo](fullstack-demo/README.md): chart completo para frontend, API y Redis con valores por entorno.

## Flujo recomendado

1. Renderiza primero con `helm template`.
2. Revisa `values.yaml` y luego los `values-*.yaml` por entorno.
3. Instala en local solo despues de tener la imagen cargada en el cluster.

## Comandos base

```bash
helm template demo examples/helm/python-api
helm template fullstack examples/helm/fullstack-demo
```
