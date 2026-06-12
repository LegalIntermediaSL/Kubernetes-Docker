# Backup Demo

Laboratorio sencillo para practicar copia, restauracion y flujo mental de `disaster recovery` sobre un volumen persistente.

## Archivos

- `namespace.yaml`
- `source-pvc.yaml`
- `backup-pvc.yaml`
- `writer-deployment.yaml`
- `backup-cronjob.yaml`
- `restore-job.yaml`

## Flujo recomendado

```bash
kubectl apply -f examples/k8s/backup-demo/namespace.yaml
kubectl apply -f examples/k8s/backup-demo/source-pvc.yaml
kubectl apply -f examples/k8s/backup-demo/backup-pvc.yaml
kubectl apply -f examples/k8s/backup-demo/writer-deployment.yaml
kubectl apply -f examples/k8s/backup-demo/backup-cronjob.yaml
kubectl create job --from=cronjob/backup-archive backup-now -n backup-demo
kubectl apply -f examples/k8s/backup-demo/restore-job.yaml
```

## Idea del ejemplo

- una app escribe datos en `source-data`
- un `CronJob` genera archivos `.tgz` en `backup-archive`
- un `Job` de restore recupera el backup mas reciente
