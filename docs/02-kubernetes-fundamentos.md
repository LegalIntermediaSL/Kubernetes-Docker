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

### Ver pods

```bash
kubectl get pods
```

### Ver deployments

```bash
kubectl get deployments
```

### Ver services

```bash
kubectl get services
```

### Describir un recurso

```bash
kubectl describe pod <pod_name>
```

### Ver logs

```bash
kubectl logs <pod_name>
```

## Qué contiene nuestro ejemplo

En este repositorio el ejemplo de Kubernetes tiene:

- Un `Deployment` con dos réplicas
- Un `Service` de tipo `ClusterIP`

Esto nos permite aprender una topología básica y luego acceder a la app con `port-forward`.

## Acceso local con port-forward

```bash
kubectl port-forward service/hola-nginx 8080:80
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
