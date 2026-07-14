# Ejemplos Kubernetes

Estos laboratorios acompañan el recorrido práctico de Kubernetes del repositorio.

## Ruta base

1. [hola-nginx](hola-nginx/README.md): primer `Deployment` y `Service`.
2. [python-api](python-api/README.md): despliegue de la API Flask con probes y recursos.
3. [configmap-secret](configmap-secret/README.md): configuración externa y secretos.
4. [ingress-demo](ingress-demo/README.md): enrutamiento HTTP con `Ingress`.
5. [job-cronjob](job-cronjob/README.md): trabajo batch y tareas programadas.

## Ruta intermedia y avanzada

- [fullstack-demo](fullstack-demo/README.md)
- [storage-demo](storage-demo/README.md)
- [probes-demo](probes-demo/README.md)
- [rbac-demo](rbac-demo/README.md)
- [network-policy-demo](network-policy-demo/README.md)
- [scaling-demo](scaling-demo/README.md)
- [postgres-demo](postgres-demo/README.md)
- [kustomize-demo](kustomize-demo/README.md)
- [cert-manager-demo](cert-manager-demo/README.md)
- [argocd-practical-demo](argocd-practical-demo/README.md)
- [observability-stack-demo](observability-stack-demo/README.md)
- [backup-demo](backup-demo/README.md)
- [external-secrets-demo](external-secrets-demo/README.md)
- [keda-demo](keda-demo/README.md)
- [scheduling-policy-demo](scheduling-policy-demo/README.md)
- [gateway-api-demo](gateway-api-demo/README.md)
- [argo-rollouts-demo](argo-rollouts-demo/README.md)
- [sops-demo](sops-demo/README.md)
- [sealed-secrets-demo](sealed-secrets-demo/README.md)

## Recomendación de uso

- Empieza por `kind` o `minikube`.
- Reutiliza las imágenes construidas en `examples/docker/`.
- Los laboratorios base ya usan namespaces explícitos para acercarse más a un cluster real.
- Haz siempre una verificación con `kubectl get`, `describe`, `logs` o `port-forward`.
