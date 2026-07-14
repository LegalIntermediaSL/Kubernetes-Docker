# Kubernetes-Docker

Curso práctico completo de Docker y Kubernetes en español.

Este repositorio reúne un recorrido guiado y ejecutable para aprender a:

- Entender qué problema resuelve Docker.
- Construir imágenes y ejecutar contenedores.
- Comprender los conceptos centrales de Kubernetes.
- Desplegar una aplicación sencilla en un clúster local.
- Diseñar entornos reproducibles, manifiestos declarativos y utilidades de apoyo.

## Para quién es este tutorial

Este material está pensado para:

- Personas que ya programan y quieren dar el salto a contenedores.
- Equipos que usan Docker pero todavía no dominan Kubernetes.
- Estudiantes que prefieren aprender con ejemplos pequeños y ejecutables.

## Estado actual

El plan base del proyecto ya está cerrado. El repositorio incluye:

- Una ruta principal completa de Docker, Kubernetes y CI/CD.
- Tutoriales guiados de principio a fin.
- Laboratorios reutilizables en Docker, Compose, Kubernetes y Helm.
- Validación estructural en CI y validación operativa documentada.

## Ruta de aprendizaje

1. [Introducción a Docker y Kubernetes](docs/00-introduccion.md)
2. [Fundamentos de Docker](docs/01-docker-fundamentos.md)
3. [Arquitectura y CLI de Docker](docs/docker/02-arquitectura-y-cli.md)
4. [Dockerfiles y buenas prácticas](docs/docker/03-dockerfiles-y-buenas-practicas.md)
5. [Volúmenes, redes y persistencia](docs/docker/04-volumenes-redes-y-persistencia.md)
6. [Docker Compose](docs/docker/05-docker-compose.md)
7. [Registro, seguridad y troubleshooting Docker](docs/docker/06-registry-seguridad-troubleshooting.md)
8. [Tutorial detallado de Docker](docs/docker/07-tutorial-docker-paso-a-paso.md)
9. [Versionado y publicacion de imagenes](docs/docker/08-versionado-y-publicacion.md)
10. [Seguridad de contenedores y hardening](docs/docker/09-seguridad-de-contenedores-y-hardening.md)
11. [BuildKit, multi-stage y optimizacion](docs/docker/10-buildkit-multi-stage-y-optimizacion.md)
12. [Debugging de runtime, redes y señales](docs/docker/11-debugging-runtime-redes-y-senales.md)
13. [Volumenes, backup y limpieza operativa](docs/docker/12-volumenes-backup-y-limpieza-operativa.md)
14. [Fundamentos de Kubernetes](docs/02-kubernetes-fundamentos.md)
15. [Arquitectura del clúster](docs/kubernetes/03-arquitectura-del-cluster.md)
16. [Workloads y actualizaciones](docs/kubernetes/04-workloads-y-actualizaciones.md)
17. [ConfigMaps, Secrets y almacenamiento](docs/kubernetes/05-configmaps-secrets-y-storage.md)
18. [Services, Ingress y red](docs/kubernetes/06-services-ingress-y-red.md)
19. [Observabilidad, seguridad y depuración](docs/kubernetes/07-observabilidad-seguridad-y-debug.md)
20. [Tutorial detallado de Kubernetes](docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md)
21. [Helm y plantillas](docs/kubernetes/09-helm-y-plantillas.md)
22. [Storage, PV y PVC](docs/kubernetes/10-storage-pv-pvc.md)
23. [Probes, recursos y scheduling](docs/kubernetes/11-probes-recursos-y-scheduling.md)
24. [RBAC, NetworkPolicies y aislamiento](docs/kubernetes/12-rbac-network-policies-y-aislamiento.md)
25. [StatefulSet, HPA y patrones de escalado](docs/kubernetes/13-statefulsets-hpa-y-patrones-de-escalado.md)
26. [Entornos, CI/CD y GitOps](docs/kubernetes/14-entornos-ci-cd-y-gitops.md)
27. [Postgres, PVC e inicialización](docs/kubernetes/15-postgres-pvc-y-inicializacion.md)
28. [Cookbook de troubleshooting](docs/kubernetes/16-cookbook-de-troubleshooting.md)
29. [Seguridad aplicada y hardening](docs/kubernetes/17-seguridad-aplicada-y-hardening.md)
30. [Observabilidad práctica](docs/kubernetes/18-observabilidad-practica.md)
31. [Helm tutorial paso a paso](docs/kubernetes/19-helm-tutorial-paso-a-paso.md)
32. [Ingress, TLS y exposicion avanzada](docs/kubernetes/20-ingress-tls-y-exposicion-avanzada.md)
33. [GitOps: Argo CD y Flux](docs/kubernetes/21-gitops-intro-argocd-y-flux.md)
34. [Prometheus, Grafana y metricas](docs/kubernetes/22-observabilidad-con-prometheus-y-grafana.md)
35. [Policies con Gatekeeper y Kyverno](docs/kubernetes/23-policies-con-gatekeeper-y-kyverno.md)
36. [Introduccion a service mesh](docs/kubernetes/24-service-mesh-introduccion.md)
37. [Kustomize: bases y overlays](docs/kubernetes/25-kustomize-bases-y-overlays.md)
38. [cert-manager y TLS automatizado](docs/kubernetes/26-cert-manager-y-tls-automatizado.md)
39. [Argo CD practico: app-of-apps y sync](docs/kubernetes/27-argocd-practico-app-of-apps-y-sync.md)
40. [Observabilidad completa con Prometheus y Grafana](docs/kubernetes/28-observabilidad-stack-completo.md)
41. [Backup, restore y disaster recovery](docs/kubernetes/29-backup-restore-y-disaster-recovery.md)
42. [External Secrets y Secret Stores](docs/kubernetes/30-external-secrets-y-secret-stores.md)
43. [KEDA y event-driven autoscaling](docs/kubernetes/31-keda-y-event-driven-autoscaling.md)
44. [Disponibilidad, scheduling y cuotas](docs/kubernetes/32-disponibilidad-scheduling-y-cuotas.md)
45. [Supply chain, Trivy, SBOM y firma](docs/kubernetes/33-supply-chain-trivy-sbom-y-firma.md)
46. [Gateway API y HTTPRoute](docs/kubernetes/34-gateway-api-y-httproute.md)
47. [Progressive delivery con Argo Rollouts](docs/kubernetes/35-progressive-delivery-con-argo-rollouts.md)
48. [SOPS, Sealed Secrets y GitOps seguro](docs/kubernetes/36-sops-sealed-secrets-y-gitops-seguro.md)
49. [Introducción a CI/CD](docs/ci-cd/01-introduccion-ci-cd.md)
50. [Workflows del repositorio](docs/ci-cd/02-workflows-del-repo.md)
51. [Publicacion, promocion y releases](docs/ci-cd/03-publicacion-promocion-y-releases.md)
52. [CI end-to-end con kind](docs/ci-cd/04-ci-end-to-end-con-kind.md)
53. [Laboratorio local avanzado](docs/06-laboratorio-local-avanzado.md)
54. [Primer proyecto práctico](docs/03-primer-proyecto.md)
55. [Proyecto multiservicio](docs/04-proyecto-multiservicio.md)
56. [Retos prácticos](docs/05-retos-practicos.md)
57. [Temario completo](docs/temario-completo.md)

## Estructura del repositorio

```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-build.yml
│       ├── helm-validate.yml
│       ├── kind-e2e.yml
│       └── publish-images.yml
├── Makefile
├── bitacora.md
├── changelog.md
├── docs/
│   ├── 00-introduccion.md
│   ├── 01-docker-fundamentos.md
│   ├── 02-kubernetes-fundamentos.md
│   ├── 03-primer-proyecto.md
│   ├── 04-proyecto-multiservicio.md
│   ├── 05-retos-practicos.md
│   ├── 06-laboratorio-local-avanzado.md
│   ├── temario-completo.md
│   ├── validacion-operativa.md
│   ├── ci-cd/
│   │   ├── 01-introduccion-ci-cd.md
│   │   ├── 02-workflows-del-repo.md
│   │   ├── 03-publicacion-promocion-y-releases.md
│   │   └── 04-ci-end-to-end-con-kind.md
│   ├── docker/
│   │   ├── 02-arquitectura-y-cli.md
│   │   ├── 03-dockerfiles-y-buenas-practicas.md
│   │   ├── 04-volumenes-redes-y-persistencia.md
│   │   ├── 05-docker-compose.md
│   │   ├── 06-registry-seguridad-troubleshooting.md
│   │   ├── 07-tutorial-docker-paso-a-paso.md
│   │   ├── 08-versionado-y-publicacion.md
│   │   ├── 09-seguridad-de-contenedores-y-hardening.md
│   │   ├── 10-buildkit-multi-stage-y-optimizacion.md
│   │   ├── 11-debugging-runtime-redes-y-senales.md
│   │   └── 12-volumenes-backup-y-limpieza-operativa.md
│   └── kubernetes/
│       ├── 03-arquitectura-del-cluster.md
│       ├── 04-workloads-y-actualizaciones.md
│       ├── 05-configmaps-secrets-y-storage.md
│       ├── 06-services-ingress-y-red.md
│       ├── 07-observabilidad-seguridad-y-debug.md
│       ├── 08-tutorial-kubernetes-paso-a-paso.md
│       ├── 09-helm-y-plantillas.md
│       ├── 10-storage-pv-pvc.md
│       ├── 11-probes-recursos-y-scheduling.md
│       ├── 12-rbac-network-policies-y-aislamiento.md
│       ├── 13-statefulsets-hpa-y-patrones-de-escalado.md
│       ├── 14-entornos-ci-cd-y-gitops.md
│       ├── 15-postgres-pvc-y-inicializacion.md
│       ├── 16-cookbook-de-troubleshooting.md
│       ├── 17-seguridad-aplicada-y-hardening.md
│       ├── 18-observabilidad-practica.md
│       ├── 19-helm-tutorial-paso-a-paso.md
│       ├── 20-ingress-tls-y-exposicion-avanzada.md
│       ├── 21-gitops-intro-argocd-y-flux.md
│       ├── 22-observabilidad-con-prometheus-y-grafana.md
│       ├── 23-policies-con-gatekeeper-y-kyverno.md
│       ├── 24-service-mesh-introduccion.md
│       ├── 25-kustomize-bases-y-overlays.md
│       ├── 26-cert-manager-y-tls-automatizado.md
│       ├── 27-argocd-practico-app-of-apps-y-sync.md
│       ├── 28-observabilidad-stack-completo.md
│       ├── 29-backup-restore-y-disaster-recovery.md
│       ├── 30-external-secrets-y-secret-stores.md
│       ├── 31-keda-y-event-driven-autoscaling.md
│       ├── 32-disponibilidad-scheduling-y-cuotas.md
│       ├── 33-supply-chain-trivy-sbom-y-firma.md
│       ├── 34-gateway-api-y-httproute.md
│       ├── 35-progressive-delivery-con-argo-rollouts.md
│       └── 36-sops-sealed-secrets-y-gitops-seguro.md
├── notebooks/
│   ├── 01_generador_dockerfile.ipynb
│   ├── 02_generador_manifiestos_k8s.ipynb
│   ├── 03_planificador_recursos_k8s.ipynb
│   ├── 04_generador_configmaps_y_secrets.ipynb
│   ├── 05_generador_pvc_y_resources.ipynb
│   ├── 06_generador_values_helm.ipynb
│   ├── 07_checklist_release_ci_cd.ipynb
│   └── README.md
└── examples/
    ├── docker/
    │   ├── hola-nginx/
    │   ├── fullstack-demo/
    │   ├── python-api/
    │   ├── python-api-optimized/
    │   ├── runtime-debug-demo/
    │   ├── volume-backup-demo/
    │   └── compose-web-api/
    ├── helm/
    │   ├── python-api/
    │   └── fullstack-demo/
    └── k8s/
        ├── backup-demo/
        ├── argocd-practical-demo/
        ├── cert-manager-demo/
        ├── gateway-api-demo/
        ├── external-secrets-demo/
        ├── fullstack-demo/
        ├── gitops-demo/
        ├── sops-demo/
        ├── helm-demo/
        ├── hola-nginx/
        ├── configmap-secret/
        ├── ingress-demo/
        ├── ingress-tls-demo/
        ├── job-cronjob/
        ├── kustomize-demo/
        ├── keda-demo/
        ├── network-policy-demo/
        ├── observability-stack-demo/
        ├── policy-demo/
        ├── prometheus-demo/
        ├── probes-demo/
        ├── postgres-demo/
        ├── python-api/
        ├── argo-rollouts-demo/
        ├── rbac-demo/
        ├── scheduling-policy-demo/
        ├── sealed-secrets-demo/
        ├── scaling-demo/
        ├── service-mesh-demo/
        └── storage-demo/
```

## Requisitos recomendados

- Docker Desktop o Docker Engine
- `kubectl`
- Un clúster local: `kind` o `minikube`
- Terminal y editor de texto
- JupyterLab o VS Code con soporte para notebooks

## Cómo usar este repositorio

La forma recomendada es avanzar por los documentos en orden y ejecutar cada bloque práctico. El recorrido base ya está completo y se apoya en:

- Capítulos progresivos de Docker, Kubernetes y CI/CD.
- Tutoriales guiados con ejercicios y verificaciones.
- Ejemplos ejecutables comparables entre Docker Compose, Kubernetes y Helm.
- Notebooks de apoyo para generar borradores y checklists.
- Una capa avanzada adicional para disponibilidad, cuotas y supply chain.
- Extension hacia routing moderno con `Gateway API` y despliegues progresivos con Argo Rollouts.
- Una especializacion de GitOps seguro con `SOPS`, `Sealed Secrets` y `External Secrets`.
- Workflows y automatizaciones para repetir validaciones clave.

## Navegación rápida por laboratorios

- [Índice general de ejemplos](examples/README.md)
- [Ejemplos Docker](examples/docker/README.md)
- [Ejemplos Kubernetes](examples/k8s/README.md)
- [Ejemplos Helm](examples/helm/README.md)

## Sitio de documentación con MkDocs

El repositorio incluye configuración para servir la documentación como sitio estático con MkDocs.

Instalación:

```bash
pip install -r requirements-docs.txt
```

Comandos útiles:

```bash
make docs-serve
make docs-build
make docs-check
```

El sitio se construye a partir de `docs/`, usa navegación manual en `mkdocs.yml` y mantiene soporte para los diagramas `Mermaid` del curso.

## Módulos principales

### Docker

- Conceptos base, imágenes, contenedores y ciclo de vida
- CLI diaria y flujos de inspección
- Dockerfiles, capas, caché y builds reproducibles
- Volúmenes, bind mounts y redes
- Docker Compose para aplicaciones multi-servicio
- Registros, seguridad, escaneo y depuración
- Tutorial guiado paso a paso con ejercicios y verificación
- Proyecto fullstack con frontend, API y Redis
- Versionado, tags, registries y publicación automatizable
- Hardening de imágenes y seguridad de contenedores
- BuildKit, multi-stage builds y optimización de capas
- Debugging de runtime, redes internas y señales de parada
- Persistencia local, backup simple y limpieza operativa de volúmenes

### Kubernetes

- Arquitectura del clúster y objetos fundamentales
- Pods, Deployments, StatefulSets, Jobs y CronJobs
- ConfigMaps, Secrets, volúmenes y almacenamiento
- Services, Ingress y comunicación interna
- Probes, recursos, seguridad y troubleshooting
- Helm, PV/PVC y laboratorios de scheduling
- RBAC, segmentación de red y patrones de escalado
- Persistencia con PostgreSQL, inicialización y `readinessProbe`
- Cookbook de troubleshooting y observabilidad operativa
- Entornos, CI/CD y GitOps como temas de nivel superior
- TLS, Prometheus/Grafana, policy-as-code y service mesh como apéndices avanzados
- Kustomize, cert-manager, Argo CD práctico y observabilidad completa como fase avanzada
- Backups, restore, secret operators y autoscaling orientado a eventos como continuidad operativa
- Tutorial guiado desde clúster local hasta despliegues más completos
- Proyecto fullstack comparable con Docker Compose

### Utilidades

- Notebooks para generar Dockerfiles
- Notebooks para construir manifiestos YAML
- Notebooks para estimar capacidad y requests
- Retos prácticos para modificar, romper y depurar laboratorios
- Guía de uso en `notebooks/README.md`
- Notebooks para values Helm y checklist de release

### Automatización

- Workflows de GitHub Actions para validación general del repo
- Build de imágenes Docker principales
- Lint y render de charts Helm
- Publicación versionada de imágenes por tag
- CI end-to-end con cluster efímero en `kind`
- Automatización local con `Makefile` para repetir el laboratorio avanzado
- Documentación específica del bloque de CI/CD

## Material visual

Varios módulos del repositorio incluyen diagramas `Mermaid` para explicar:

- El flujo de build y ejecución con Docker
- La arquitectura de Docker y Docker Compose
- La separacion entre etapa de build y etapa de runtime
- El flujo de diagnostico de runtime y señales de cierre
- La arquitectura del clúster Kubernetes
- El tráfico entre `Service`, `Ingress` y `Pods`
- La relación entre `PVC`, `Deployment` y base de datos
- El aislamiento con RBAC y `NetworkPolicy`
- El flujo declarativo de GitOps y promoción por entornos
- La transición desde YAML base hacia overlays y reconciliación GitOps
- El recorrido de backup, restore y recuperación operativa
- La sincronizacion entre `SecretStore`, `ExternalSecret` y `Secret`
- El puente entre fuentes de eventos, KEDA y `HPA`
- El recorrido completo del primer proyecto práctico
- Los tutoriales paso a paso de Docker y Kubernetes

## Seguimiento y trazabilidad

- [Bitácora](bitacora.md)
- [Changelog](changelog.md)
- [Plan de expansión](docs/plan-expansion.md)
- [Validacion operativa](docs/validacion-operativa.md)

## Primer paso sugerido

Empieza por la [introducción](docs/00-introduccion.md), luego recorre el [temario completo](docs/temario-completo.md) y después alterna teoría con los directorios de `examples/` y `notebooks/`.

## Estado del plan de expansión

El roadmap detallado está en [docs/plan-expansion.md](docs/plan-expansion.md).

Ese documento se conserva como trazabilidad del diseño y de las decisiones de crecimiento. La parte principal del plan ya quedó materializada en el repositorio:

- bloques básicos, intermedios y superiores de Docker y Kubernetes
- ejemplos prácticos en Docker, Compose, Kubernetes y Helm
- CI/CD, publicación y promoción por entornos
- seguridad, observabilidad, troubleshooting y gobierno básico
- una fase avanzada adicional con `kind`, `Kustomize`, `cert-manager`, Argo CD práctico y observabilidad más completa
- apéndices avanzados de GitOps, TLS, Prometheus/Grafana, policies y service mesh

Ademas, la validacion en vivo ejecutada el 2026-06-09 quedo resumida en [docs/validacion-operativa.md](docs/validacion-operativa.md), con pruebas reales sobre `minikube` para Kustomize, Helm, `cert-manager`, Argo CD y observabilidad.

Los siguientes saltos ya quedan fuera del plan base y entran mas en especializacion o variantes por proveedor.
