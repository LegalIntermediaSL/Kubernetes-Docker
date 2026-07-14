# Fundamentos de Kubernetes

Kubernetes trabaja de forma declarativa: no le dices "haz esto paso a paso", sino "quiero que el sistema termine en este estado".

## Idea central

En lugar de levantar manualmente contenedores uno por uno, escribimos manifiestos YAML que describen el estado deseado.

Luego Kubernetes intenta mantener ese estado:

- Si un pod muere, lo recrea.
- Si pedimos tres réplicas, intenta mantener tres.
- Si actualizamos la imagen, aplica la nueva versión siguiendo la estrategia configurada.

## Objetos básicos

### Pod

Es la unidad mínima desplegable. Un pod suele contener uno o varios contenedores muy relacionados.

### Deployment

Gestiona pods de forma declarativa. Es el recurso típico para desplegar aplicaciones stateless.

### Service

Da una identidad de red estable a un conjunto de pods. Esto evita depender de IPs efímeras.

## Cómo piensa Kubernetes

Kubernetes compara dos cosas:

- El estado deseado
- El estado real

Su trabajo consiste en reconciliar ambos.

## Comandos esenciales con `kubectl`

### Aplicar manifiestos

```bash
kubectl apply -f examples/k8s/hola-nginx/
```

Este ejemplo crea sus recursos en el namespace `hola-nginx-demo`.

### Ver pods

```bash
kubectl get pods -n hola-nginx-demo
```

### Ver deployments

```bash
kubectl get deployments -n hola-nginx-demo
```

### Ver services

```bash
kubectl get services -n hola-nginx-demo
```

### Describir un recurso

```bash
kubectl describe pod -n hola-nginx-demo <pod_name>
```

### Ver logs

```bash
kubectl logs -n hola-nginx-demo <pod_name>
```

## Qué contiene nuestro ejemplo

En este repositorio el ejemplo de Kubernetes tiene:

- Un `Deployment` con dos réplicas
- Un `Service` de tipo `ClusterIP`

Esto nos permite aprender una topología básica y luego acceder a la app con `port-forward`.

## Acceso local con port-forward

```bash
kubectl port-forward -n hola-nginx-demo service/hola-nginx 8080:80
```

Después puedes abrir:

```text
http://localhost:8080
```

## Errores típicos al empezar

- La imagen no existe en el clúster local.
- El selector del `Service` no coincide con las etiquetas del pod.
- El contenedor escucha en un puerto distinto al declarado.
- Se aplica un YAML correcto sintácticamente pero incorrecto conceptualmente.

## Siguiente paso

Continúa con el [primer proyecto práctico](03-primer-proyecto.md), donde usaremos Docker y Kubernetes juntos.

## Siguientes módulos de Kubernetes

Después de esta base, sigue con:

- [Arquitectura del clúster](kubernetes/03-arquitectura-del-cluster.md)
- [Workloads y actualizaciones](kubernetes/04-workloads-y-actualizaciones.md)
- [ConfigMaps, Secrets y almacenamiento](kubernetes/05-configmaps-secrets-y-storage.md)
- [Services, Ingress y red](kubernetes/06-services-ingress-y-red.md)
- [Observabilidad, seguridad y depuración](kubernetes/07-observabilidad-seguridad-y-debug.md)
- [Tutorial detallado de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)
- [Helm y plantillas](kubernetes/09-helm-y-plantillas.md)
- [Storage, PV y PVC](kubernetes/10-storage-pv-pvc.md)
- [Probes, recursos y scheduling](kubernetes/11-probes-recursos-y-scheduling.md)
- [Entornos, CI/CD y GitOps](kubernetes/14-entornos-ci-cd-y-gitops.md)
- [Helm tutorial paso a paso](kubernetes/19-helm-tutorial-paso-a-paso.md)
- [GitOps: Argo CD y Flux](kubernetes/21-gitops-intro-argocd-y-flux.md)
- [Kustomize: bases y overlays](kubernetes/25-kustomize-bases-y-overlays.md)
- [cert-manager y TLS automatizado](kubernetes/26-cert-manager-y-tls-automatizado.md)
- [Argo CD practico: app-of-apps y sync](kubernetes/27-argocd-practico-app-of-apps-y-sync.md)
- [Observabilidad completa con Prometheus y Grafana](kubernetes/28-observabilidad-stack-completo.md)
- [Backup, restore y disaster recovery](kubernetes/29-backup-restore-y-disaster-recovery.md)
- [External Secrets y Secret Stores](kubernetes/30-external-secrets-y-secret-stores.md)
- [KEDA y event-driven autoscaling](kubernetes/31-keda-y-event-driven-autoscaling.md)
- [Disponibilidad, scheduling y cuotas](kubernetes/32-disponibilidad-scheduling-y-cuotas.md)
- [Supply chain, Trivy, SBOM y firma](kubernetes/33-supply-chain-trivy-sbom-y-firma.md)
- [Gateway API y HTTPRoute](kubernetes/34-gateway-api-y-httproute.md)
- [Progressive delivery con Argo Rollouts](kubernetes/35-progressive-delivery-con-argo-rollouts.md)
- [SOPS, Sealed Secrets y GitOps seguro](kubernetes/36-sops-sealed-secrets-y-gitops-seguro.md)
