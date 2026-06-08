# RBAC Demo

Este laboratorio muestra una `ServiceAccount` con permisos mínimos de lectura sobre pods y services en un namespace dedicado.

## Recursos

- `namespace.yaml`
- `serviceaccount.yaml`
- `role.yaml`
- `rolebinding.yaml`
- `pod.yaml`

## Aplicación

```bash
kubectl apply -f examples/k8s/rbac-demo/
```

## Verificación

```bash
kubectl get sa -n rbac-demo
kubectl get role -n rbac-demo
kubectl get rolebinding -n rbac-demo
kubectl auth can-i list pods \
  --as=system:serviceaccount:rbac-demo:rbac-reader \
  -n rbac-demo
kubectl auth can-i delete pods \
  --as=system:serviceaccount:rbac-demo:rbac-reader \
  -n rbac-demo
```
