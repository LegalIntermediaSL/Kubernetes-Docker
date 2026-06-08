# Kubernetes-Docker

Tutorial práctico de Docker y Kubernetes en español.

Este repositorio empieza como una base de curso para aprender a:

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
11. [Fundamentos de Kubernetes](docs/02-kubernetes-fundamentos.md)
12. [Arquitectura del clúster](docs/kubernetes/03-arquitectura-del-cluster.md)
13. [Workloads y actualizaciones](docs/kubernetes/04-workloads-y-actualizaciones.md)
14. [ConfigMaps, Secrets y almacenamiento](docs/kubernetes/05-configmaps-secrets-y-storage.md)
15. [Services, Ingress y red](docs/kubernetes/06-services-ingress-y-red.md)
16. [Observabilidad, seguridad y depuración](docs/kubernetes/07-observabilidad-seguridad-y-debug.md)
17. [Tutorial detallado de Kubernetes](docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md)
18. [Helm y plantillas](docs/kubernetes/09-helm-y-plantillas.md)
19. [Storage, PV y PVC](docs/kubernetes/10-storage-pv-pvc.md)
20. [Probes, recursos y scheduling](docs/kubernetes/11-probes-recursos-y-scheduling.md)
21. [RBAC, NetworkPolicies y aislamiento](docs/kubernetes/12-rbac-network-policies-y-aislamiento.md)
22. [StatefulSet, HPA y patrones de escalado](docs/kubernetes/13-statefulsets-hpa-y-patrones-de-escalado.md)
23. [Entornos, CI/CD y GitOps](docs/kubernetes/14-entornos-ci-cd-y-gitops.md)
24. [Postgres, PVC e inicialización](docs/kubernetes/15-postgres-pvc-y-inicializacion.md)
25. [Cookbook de troubleshooting](docs/kubernetes/16-cookbook-de-troubleshooting.md)
26. [Seguridad aplicada y hardening](docs/kubernetes/17-seguridad-aplicada-y-hardening.md)
27. [Observabilidad práctica](docs/kubernetes/18-observabilidad-practica.md)
28. [Helm tutorial paso a paso](docs/kubernetes/19-helm-tutorial-paso-a-paso.md)
29. [Ingress, TLS y exposicion avanzada](docs/kubernetes/20-ingress-tls-y-exposicion-avanzada.md)
30. [GitOps: Argo CD y Flux](docs/kubernetes/21-gitops-intro-argocd-y-flux.md)
31. [Prometheus, Grafana y metricas](docs/kubernetes/22-observabilidad-con-prometheus-y-grafana.md)
32. [Policies con Gatekeeper y Kyverno](docs/kubernetes/23-policies-con-gatekeeper-y-kyverno.md)
33. [Introduccion a service mesh](docs/kubernetes/24-service-mesh-introduccion.md)
34. [Introducción a CI/CD](docs/ci-cd/01-introduccion-ci-cd.md)
35. [Workflows del repositorio](docs/ci-cd/02-workflows-del-repo.md)
36. [Publicacion, promocion y releases](docs/ci-cd/03-publicacion-promocion-y-releases.md)
37. [Primer proyecto práctico](docs/03-primer-proyecto.md)
38. [Proyecto multiservicio](docs/04-proyecto-multiservicio.md)
39. [Retos prácticos](docs/05-retos-practicos.md)
40. [Temario completo](docs/temario-completo.md)

## Estructura del repositorio

```text
.
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── docker-build.yml
│       ├── helm-validate.yml
│       └── publish-images.yml
├── bitacora.md
├── changelog.md
├── docs/
│   ├── 00-introduccion.md
│   ├── 01-docker-fundamentos.md
│   ├── 02-kubernetes-fundamentos.md
│   ├── 03-primer-proyecto.md
│   ├── 04-proyecto-multiservicio.md
│   ├── 05-retos-practicos.md
│   ├── temario-completo.md
│   ├── ci-cd/
│   │   ├── 01-introduccion-ci-cd.md
│   │   ├── 02-workflows-del-repo.md
│   │   └── 03-publicacion-promocion-y-releases.md
│   ├── docker/
│   │   ├── 02-arquitectura-y-cli.md
│   │   ├── 03-dockerfiles-y-buenas-practicas.md
│   │   ├── 04-volumenes-redes-y-persistencia.md
│   │   ├── 05-docker-compose.md
│   │   ├── 06-registry-seguridad-troubleshooting.md
│   │   ├── 07-tutorial-docker-paso-a-paso.md
│   │   ├── 08-versionado-y-publicacion.md
│   │   └── 09-seguridad-de-contenedores-y-hardening.md
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
│       └── 24-service-mesh-introduccion.md
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
    │   └── compose-web-api/
    ├── helm/
    │   ├── python-api/
    │   └── fullstack-demo/
    └── k8s/
        ├── fullstack-demo/
        ├── gitops-demo/
        ├── helm-demo/
        ├── hola-nginx/
        ├── configmap-secret/
        ├── ingress-demo/
        ├── ingress-tls-demo/
        ├── job-cronjob/
        ├── network-policy-demo/
        ├── policy-demo/
        ├── prometheus-demo/
        ├── probes-demo/
        ├── postgres-demo/
        ├── python-api/
        ├── rbac-demo/
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

La forma recomendada es avanzar por los documentos en orden y ejecutar cada bloque práctico. El repositorio irá creciendo con:

- Más capítulos
- Ejercicios guiados
- Ejemplos de aplicaciones
- Manifiestos de Kubernetes más completos
- Proyectos prácticos comparables entre Docker Compose y Kubernetes
- Charts Helm listos para render y personalizar por entorno
- Workflows de CI/CD fáciles de leer y adaptar

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
- Documentación específica del bloque de CI/CD

## Material visual

Varios módulos del repositorio incluyen diagramas `Mermaid` para explicar:

- El flujo de build y ejecución con Docker
- La arquitectura de Docker y Docker Compose
- La arquitectura del clúster Kubernetes
- El tráfico entre `Service`, `Ingress` y `Pods`
- La relación entre `PVC`, `Deployment` y base de datos
- El aislamiento con RBAC y `NetworkPolicy`
- El flujo declarativo de GitOps y promoción por entornos
- El recorrido completo del primer proyecto práctico
- Los tutoriales paso a paso de Docker y Kubernetes

## Seguimiento del proyecto

- [Bitácora](bitacora.md)
- [Changelog](changelog.md)
- [Plan de expansión](docs/plan-expansion.md)

## Primer paso sugerido

Empieza por la [introducción](docs/00-introduccion.md), luego recorre el [temario completo](docs/temario-completo.md) y después alterna teoría con los directorios de `examples/` y `notebooks/`.

## Estado del plan de expansión

El roadmap detallado está en [docs/plan-expansion.md](docs/plan-expansion.md).

La parte principal del plan ya quedó materializada en el repositorio:

- bloques básicos, intermedios y superiores de Docker y Kubernetes
- ejemplos prácticos en Docker, Compose, Kubernetes y Helm
- CI/CD, publicación y promoción por entornos
- seguridad, observabilidad, troubleshooting y gobierno básico
- apéndices avanzados de GitOps, TLS, Prometheus/Grafana, policies y service mesh

Los siguientes saltos ya quedarían fuera del plan base y entrarían más en especialización o variantes por proveedor.
