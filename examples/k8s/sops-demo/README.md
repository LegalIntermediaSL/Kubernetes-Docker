# SOPS Demo

Laboratorio para estudiar el patron de secretos cifrados en Git con `SOPS`.

## Archivos

- `namespace.yaml`
- `deployment.yaml`
- `secret-plain.example.yaml`
- `secret.enc.example.yaml`
- `sops-config.example.txt`

## Idea del ejemplo

El repositorio incluye:

- un `Secret` plano de entrada
- una plantilla de configuracion `SOPS`
- una version cifrada ilustrativa

Importante:

- `secret.enc.example.yaml` no esta pensado para descifrarse tal cual
- debes regenerarlo con tus propias claves o recipients

## Flujo recomendado

1. Crea el namespace:

```bash
kubectl apply -f examples/k8s/sops-demo/namespace.yaml
```

2. Genera o elige tu recipient `age`.

3. Cifra el secreto de ejemplo:

```bash
export SOPS_AGE_RECIPIENTS="age1reemplaza-por-tu-clave-publica"
sops encrypt --age "$SOPS_AGE_RECIPIENTS" \
  examples/k8s/sops-demo/secret-plain.example.yaml \
  > examples/k8s/sops-demo/secret.enc.yaml
```

4. Para comprobar localmente el flujo sin GitOps:

```bash
sops -d examples/k8s/sops-demo/secret.enc.yaml | kubectl apply -f -
kubectl apply -f examples/k8s/sops-demo/deployment.yaml
kubectl logs -n sops-demo deploy/sops-secret-consumer
```

## Nota GitOps

Con Flux, el valor de este patron es que el repo guarda ciphertext y el reconciliador descifra justo antes de aplicar.
