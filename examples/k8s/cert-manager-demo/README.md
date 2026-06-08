# cert-manager Demo

Ejemplo de certificados automatizados con `cert-manager` para una app pequeña publicada con `Ingress`.

## Archivos

- `namespace.yaml`
- `deployment.yaml`
- `service.yaml`
- `clusterissuer-selfsigned.yaml`
- `clusterissuer-letsencrypt-staging.yaml`
- `certificate.yaml`
- `ingress.yaml`

## Nota

Antes de aplicarlo necesitas tener `cert-manager` y un `Ingress Controller`.
