# Sealed Secrets Demo

Laboratorio para estudiar el patron de secretos sellados con `kubeseal`.

## Archivos

- `namespace.yaml`
- `deployment.yaml`
- `secret-plain.example.yaml`
- `sealedsecret.example.yaml`

## Idea del ejemplo

El repo incluye:

- un `Secret` normal como entrada
- un `SealedSecret` ilustrativo con estructura real

Importante:

- `sealedsecret.example.yaml` no es reutilizable tal cual
- debes regenerarlo con el certificado del controlador de tu cluster

## Flujo recomendado

1. Crea el namespace:

```bash
kubectl apply -f examples/k8s/sealed-secrets-demo/namespace.yaml
```

2. Instala el controlador siguiendo la release oficial de Sealed Secrets.

3. Obtiene el certificado publico:

```bash
kubeseal --fetch-cert > sealed-secrets.cert
```

4. Sella el secreto:

```bash
kubeseal --cert sealed-secrets.cert -o yaml \
  < examples/k8s/sealed-secrets-demo/secret-plain.example.yaml \
  > examples/k8s/sealed-secrets-demo/sealedsecret.yaml
```

5. Aplica el resultado y despliega la app consumidora:

```bash
kubectl apply -f examples/k8s/sealed-secrets-demo/sealedsecret.yaml
kubectl apply -f examples/k8s/sealed-secrets-demo/deployment.yaml
kubectl logs -n sealed-secrets-demo deploy/sealed-secret-consumer
```

## Nota importante

El resultado queda ligado al certificado del controlador que lo va a abrir. Si cambias de cluster, normalmente tendras que sellar de nuevo.
