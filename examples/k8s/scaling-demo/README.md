# Scaling Demo

Este laboratorio reúne dos patrones:

- `StatefulSet` con identidad estable
- `HorizontalPodAutoscaler` para un deployment stateless

## Recursos

- `headless-service.yaml`
- `statefulset.yaml`
- `api-deployment.yaml`
- `api-service.yaml`
- `hpa.yaml`

## Aplicación

```bash
kubectl apply -f examples/k8s/scaling-demo/headless-service.yaml
kubectl apply -f examples/k8s/scaling-demo/statefulset.yaml
kubectl apply -f examples/k8s/scaling-demo/api-deployment.yaml
kubectl apply -f examples/k8s/scaling-demo/api-service.yaml
kubectl apply -f examples/k8s/scaling-demo/hpa.yaml
```

## Verificación

```bash
kubectl get pods
kubectl get statefulsets
kubectl get hpa
kubectl describe statefulset demo-store
```

El HPA requiere métricas disponibles en el clúster para escalar de verdad.
