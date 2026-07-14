# Job y CronJob

Laboratorio mínimo para distinguir entre trabajo batch puntual y tarea programada.

## Recursos incluidos

- `namespace.yaml`
- `job.yaml`
- `cronjob.yaml`

## Despliegue

```bash
kubectl apply -f examples/k8s/job-cronjob/
```

## Verificación

```bash
kubectl get jobs -n batch-demo
kubectl get cronjobs -n batch-demo
kubectl get pods -n batch-demo
kubectl logs -n batch-demo job/saludo-job
```

## Ejecución manual desde el CronJob

Si quieres disparar una ejecución bajo demanda:

```bash
kubectl create job -n batch-demo --from=cronjob/reporte-cada-cinco-min reporte-manual
kubectl logs -n batch-demo job/reporte-manual
```

## Qué practicar

- `Job` como tarea que termina.
- `CronJob` como planificación periódica.
- Consulta de logs en workloads batch.

## Limpieza

```bash
kubectl delete -f examples/k8s/job-cronjob/
kubectl delete -n batch-demo job reporte-manual --ignore-not-found
```
