# Probes Demo

Este directorio reúne varios casos para practicar:

- `startupProbe`
- `readinessProbe`
- `livenessProbe`
- `requests`
- `limits`
- diagnóstico de pods `Pending`

## Archivos

- `deployment-ok.yaml`
- `deployment-bad-readiness.yaml`
- `deployment-bad-liveness.yaml`
- `pod-unschedulable.yaml`
- `service-ok.yaml`

## Flujo sugerido

### Caso correcto

```bash
kubectl apply -f examples/k8s/probes-demo/deployment-ok.yaml
kubectl apply -f examples/k8s/probes-demo/service-ok.yaml
kubectl get pods -w
```

### Caso de readiness rota

```bash
kubectl apply -f examples/k8s/probes-demo/deployment-bad-readiness.yaml
kubectl describe pod -l app=probes-bad-readiness
```

### Caso de liveness rota

```bash
kubectl apply -f examples/k8s/probes-demo/deployment-bad-liveness.yaml
kubectl describe pod -l app=probes-bad-liveness
```

### Caso de scheduling fallido

```bash
kubectl apply -f examples/k8s/probes-demo/pod-unschedulable.yaml
kubectl describe pod unschedulable-demo
```
