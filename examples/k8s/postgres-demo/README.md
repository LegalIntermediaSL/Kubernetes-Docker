# Postgres Demo

Este laboratorio despliega PostgreSQL con:

- `Secret` para credenciales
- `ConfigMap` con script de inicialización
- `PersistentVolumeClaim`
- `Deployment` y `Service`

## Aplicación

```bash
kubectl apply -f examples/k8s/postgres-demo/
```

## Verificación

```bash
kubectl get pods
kubectl get pvc
kubectl get svc
```

## Acceso local

```bash
kubectl port-forward service/postgres-demo 5432:5432
```

## Prueba con psql

```bash
PGPASSWORD=postgres-demo psql -h 127.0.0.1 -U curso -d curso_demo -c "SELECT * FROM demo_items;"
```
