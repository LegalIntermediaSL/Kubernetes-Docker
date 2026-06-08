# Storage Demo

Este ejemplo muestra persistencia básica en Kubernetes usando:

- `PersistentVolume`
- `PersistentVolumeClaim`
- `Deployment`
- `Service`

La aplicación incrementa un contador guardado en `/data/visitas.txt`.

## Flujo recomendado

```bash
kubectl apply -f examples/k8s/storage-demo/pv.yaml
kubectl apply -f examples/k8s/storage-demo/pvc.yaml
kubectl apply -f examples/k8s/storage-demo/deployment.yaml
kubectl apply -f examples/k8s/storage-demo/service.yaml
```

## Verificación

```bash
kubectl get pv
kubectl get pvc
kubectl get pods
kubectl port-forward service/storage-demo 8082:80
```

En otra terminal:

```bash
curl -s http://localhost:8082
curl -s http://localhost:8082
curl -s http://localhost:8082/health
```

## Prueba de persistencia

```bash
kubectl delete -f examples/k8s/storage-demo/deployment.yaml
kubectl apply -f examples/k8s/storage-demo/deployment.yaml
```

Luego consulta otra vez el endpoint y comprueba si el contador se mantiene.
