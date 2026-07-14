# Scheduling Policy Demo

Laboratorio para practicar decisiones de plataforma alrededor de:

- reparto de replicas
- prioridad relativa
- proteccion ante interrupciones voluntarias
- presupuestos de recursos por namespace

## Archivos

- `namespace.yaml`
- `priorityclass.yaml`
- `limitrange.yaml`
- `resourcequota.yaml`
- `deployment.yaml`
- `pdb.yaml`
- `pod-defaults.yaml`
- `pod-overquota.yaml`

## Flujo recomendado

```bash
kubectl apply -f examples/k8s/scheduling-policy-demo/namespace.yaml
kubectl apply -f examples/k8s/scheduling-policy-demo/priorityclass.yaml
kubectl apply -f examples/k8s/scheduling-policy-demo/limitrange.yaml
kubectl apply -f examples/k8s/scheduling-policy-demo/resourcequota.yaml
kubectl apply -f examples/k8s/scheduling-policy-demo/deployment.yaml
kubectl apply -f examples/k8s/scheduling-policy-demo/pdb.yaml
kubectl -n scheduling-demo rollout status deployment/spread-demo
```

## Comprobaciones utiles

```bash
kubectl get pods -n scheduling-demo -o wide
kubectl get pdb -n scheduling-demo
kubectl get limitrange,resourcequota -n scheduling-demo
kubectl get priorityclass platform-medium
```

## Ver `LimitRange` en accion

Aplica un pod sin recursos declarados:

```bash
kubectl apply -f examples/k8s/scheduling-policy-demo/pod-defaults.yaml
kubectl get pod -n scheduling-demo defaults-demo -o yaml
```

Busca `resources.requests` y `resources.limits` para ver los defaults del namespace.

## Forzar un rechazo por cuota

```bash
kubectl apply -f examples/k8s/scheduling-policy-demo/pod-overquota.yaml
```

Deberia fallar porque el namespace ya consume parte de la cuota con el `Deployment`.

## Nota importante sobre clusters pequenos

El ejemplo usa:

- `podAntiAffinity` en modo `preferred`
- `topologySpreadConstraints` con `ScheduleAnyway`

Eso mantiene el laboratorio util incluso en `kind` o `minikube` de un solo nodo.
