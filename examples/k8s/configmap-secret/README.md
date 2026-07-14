# ConfigMap y Secret

Laboratorio para ver cómo un contenedor recibe configuración externa y datos sensibles sin quemarlos en la imagen.

## Recursos incluidos

- `namespace.yaml`
- `configmap.yaml`
- `secret.yaml`
- `deployment.yaml`
- `service.yaml`

## Despliegue

```bash
kubectl apply -f examples/k8s/configmap-secret/
```

## Verificación

```bash
kubectl get configmap env-demo-config -n config-demo
kubectl get secret env-demo-secret -n config-demo
kubectl get deployment env-demo -n config-demo
kubectl get service env-demo -n config-demo
kubectl port-forward -n config-demo service/env-demo 8081:80
```

En otra terminal:

```bash
curl -s http://localhost:8081
```

Deberías ver valores procedentes de:

- `ConfigMap`: `APP_NAME` y `APP_MODE`
- `Secret`: `API_TOKEN`

## Qué practicar

- `envFrom` con `configMapRef`
- `envFrom` con `secretRef`
- separación entre imagen, configuración y secretos

## Limpieza

```bash
kubectl delete -f examples/k8s/configmap-secret/
```
