# Ingress TLS Demo

Ejemplo de exposicion HTTPS basica con un `Ingress`, un `Service` y un secreto TLS de muestra.

## Archivos

- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`
- `tls-secret.yaml`

## Nota importante

El secreto TLS usa datos de ejemplo. Debes reemplazarlo por un certificado real o generado para tu entorno.

## Flujo sugerido

```bash
kubectl apply -f examples/k8s/ingress-tls-demo/
kubectl get ingress
kubectl describe ingress tls-demo
```
