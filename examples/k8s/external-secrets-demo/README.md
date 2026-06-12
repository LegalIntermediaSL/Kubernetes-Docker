# External Secrets Demo

Laboratorio para sincronizar un secreto desde un namespace origen hacia un namespace consumidor usando External Secrets Operator.

## Archivos

- `source-namespace.yaml`
- `target-namespace.yaml`
- `source-secret.yaml`
- `serviceaccount.yaml`
- `role.yaml`
- `rolebinding.yaml`
- `secretstore.yaml`
- `externalsecret.yaml`
- `deployment.yaml`

## Nota

Antes de aplicar `SecretStore` y `ExternalSecret` necesitas tener instalado External Secrets Operator.

## Flujo recomendado

```bash
kubectl apply -f examples/k8s/external-secrets-demo/source-namespace.yaml
kubectl apply -f examples/k8s/external-secrets-demo/target-namespace.yaml
kubectl apply -f examples/k8s/external-secrets-demo/source-secret.yaml
kubectl apply -f examples/k8s/external-secrets-demo/serviceaccount.yaml
kubectl apply -f examples/k8s/external-secrets-demo/role.yaml
kubectl apply -f examples/k8s/external-secrets-demo/rolebinding.yaml
kubectl apply -f examples/k8s/external-secrets-demo/secretstore.yaml
kubectl apply -f examples/k8s/external-secrets-demo/externalsecret.yaml
kubectl apply -f examples/k8s/external-secrets-demo/deployment.yaml
```
