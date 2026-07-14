# Kubernetes-Docker

Curso practico completo de Docker y Kubernetes en espanol, con recorrido guiado, laboratorios reutilizables y validacion operativa.

<div class="hero-grid">
  <a class="hero-card" href="00-introduccion/">
    <strong>Empezar por la base</strong>
    <span>Introduccion, conceptos y primer mapa mental del curso.</span>
  </a>
  <a class="hero-card" href="docker/07-tutorial-docker-paso-a-paso/">
    <strong>Tutorial de Docker</strong>
    <span>Recorrido continuo desde imagenes hasta Compose y debugging.</span>
  </a>
  <a class="hero-card" href="kubernetes/08-tutorial-kubernetes-paso-a-paso/">
    <strong>Tutorial de Kubernetes</strong>
    <span>Cluster local, manifests, ConfigMap, Secret, Ingress, Job y diagnostico.</span>
  </a>
  <a class="hero-card" href="06-laboratorio-local-avanzado/">
    <strong>Laboratorio avanzado</strong>
    <span>Kustomize, Helm, cert-manager, Argo CD y observabilidad desde un solo flujo.</span>
  </a>
  <a class="hero-card" href="temario-completo/">
    <strong>Ver el mapa completo</strong>
    <span>Indice total del curso para orientarte antes de profundizar.</span>
  </a>
  <a class="hero-card" href="validacion-operativa/">
    <strong>Comprobar evidencia real</strong>
    <span>Resumen de validaciones ejecutadas en cluster local.</span>
  </a>
</div>

## Que incluye el repositorio

- Fundamentos de Docker y Kubernetes.
- Tutoriales paso a paso.
- Laboratorios base, intermedios y avanzados.
- Charts Helm y overlays Kustomize.
- Workflows de CI y validaciones end-to-end.
- Bitacora, changelog y trazabilidad del proyecto.

## Ruta recomendada

1. [Introduccion a Docker y Kubernetes](00-introduccion.md)
2. [Fundamentos de Docker](01-docker-fundamentos.md)
3. [Fundamentos de Kubernetes](02-kubernetes-fundamentos.md)
4. [Primer proyecto practico](03-primer-proyecto.md)
5. [Proyecto multiservicio](04-proyecto-multiservicio.md)
6. [Tutorial de Docker](docker/07-tutorial-docker-paso-a-paso.md)
7. [Tutorial de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)

## Capas del curso

### Base

- Docker, contenedores, imagenes y Compose
- Pods, Deployments, Services, ConfigMaps y Secrets
- Primeros despliegues locales con `kind` o `minikube`

### Plataforma

- RBAC, NetworkPolicies, recursos, probes y scheduling
- Helm, Kustomize, entornos y GitOps
- Persistencia, PostgreSQL, troubleshooting y hardening
- Disponibilidad con `PDB`, `PriorityClass`, cuotas y defaults por namespace
- Exposicion moderna con `Gateway API` y `HTTPRoute`

### Operacion aplicada

- Observabilidad con Prometheus y Grafana
- TLS con `cert-manager`
- `External Secrets`, KEDA y backup/restore
- Supply chain con escaneo, `SBOM` y firma de imagenes
- Progressive delivery con `blue-green` y `canary`
- GitOps seguro con `SOPS`, `Sealed Secrets` y operadores de secretos
- CI real con `kind`

## Recursos fuera del sitio

El sitio se construye desde `docs/`, pero el recorrido practico se apoya tambien en:

- `examples/docker/`
- `examples/k8s/`
- `examples/helm/`
- `notebooks/`

Usa esos directorios junto con la documentacion para ejecutar los laboratorios del curso.
