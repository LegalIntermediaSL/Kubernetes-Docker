# Network Policy Demo

Este laboratorio crea una API y un frontend lógico en un namespace dedicado, junto con una `NetworkPolicy` que permite tráfico a la API solo desde pods etiquetados como frontend.

## Recursos

- `namespace.yaml`
- `api-deployment.yaml`
- `api-service.yaml`
- `frontend-deployment.yaml`
- `frontend-service.yaml`
- `network-policy.yaml`

## Aplicación

```bash
kubectl apply -f examples/k8s/network-policy-demo/
```

## Verificación conceptual

```bash
kubectl get pods -n network-policy-demo
kubectl get svc -n network-policy-demo
kubectl get networkpolicy -n network-policy-demo
kubectl describe networkpolicy api-only-from-frontend -n network-policy-demo
```

La aplicación efectiva de la política depende del plugin de red del clúster.
