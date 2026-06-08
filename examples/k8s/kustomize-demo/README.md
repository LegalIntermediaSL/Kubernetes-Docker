# Kustomize Demo

Ejemplo de `base` y `overlays` para desplegar la `python-api` con diferencias claras entre entornos.

## Estructura

- `base/`
- `overlays/dev/`
- `overlays/demo/`
- `overlays/prod/`

## Comandos utiles

```bash
kubectl kustomize examples/k8s/kustomize-demo/overlays/dev
kubectl apply -k examples/k8s/kustomize-demo/overlays/dev
kubectl delete -k examples/k8s/kustomize-demo/overlays/dev
```

## Que cambia por entorno

- namespace
- replicas
- valores de entorno
- imagen y tag
- recursos
