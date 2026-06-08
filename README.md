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
9. [Fundamentos de Kubernetes](docs/02-kubernetes-fundamentos.md)
10. [Arquitectura del clúster](docs/kubernetes/03-arquitectura-del-cluster.md)
11. [Workloads y actualizaciones](docs/kubernetes/04-workloads-y-actualizaciones.md)
12. [ConfigMaps, Secrets y almacenamiento](docs/kubernetes/05-configmaps-secrets-y-storage.md)
13. [Services, Ingress y red](docs/kubernetes/06-services-ingress-y-red.md)
14. [Observabilidad, seguridad y depuración](docs/kubernetes/07-observabilidad-seguridad-y-debug.md)
15. [Tutorial detallado de Kubernetes](docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md)
16. [Helm y plantillas](docs/kubernetes/09-helm-y-plantillas.md)
17. [Storage, PV y PVC](docs/kubernetes/10-storage-pv-pvc.md)
18. [Probes, recursos y scheduling](docs/kubernetes/11-probes-recursos-y-scheduling.md)
19. [RBAC, NetworkPolicies y aislamiento](docs/kubernetes/12-rbac-network-policies-y-aislamiento.md)
20. [StatefulSet, HPA y patrones de escalado](docs/kubernetes/13-statefulsets-hpa-y-patrones-de-escalado.md)
21. [Entornos, CI/CD y GitOps](docs/kubernetes/14-entornos-ci-cd-y-gitops.md)
22. [Primer proyecto práctico](docs/03-primer-proyecto.md)
23. [Proyecto multiservicio](docs/04-proyecto-multiservicio.md)
24. [Temario completo](docs/temario-completo.md)

## Estructura del repositorio

```text
.
├── bitacora.md
├── changelog.md
├── docs/
│   ├── 00-introduccion.md
│   ├── 01-docker-fundamentos.md
│   ├── 02-kubernetes-fundamentos.md
│   ├── 03-primer-proyecto.md
│   ├── 04-proyecto-multiservicio.md
│   ├── temario-completo.md
│   ├── docker/
│   │   ├── 02-arquitectura-y-cli.md
│   │   ├── 03-dockerfiles-y-buenas-practicas.md
│   │   ├── 04-volumenes-redes-y-persistencia.md
│   │   ├── 05-docker-compose.md
│   │   ├── 06-registry-seguridad-troubleshooting.md
│   │   └── 07-tutorial-docker-paso-a-paso.md
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
│       └── 14-entornos-ci-cd-y-gitops.md
├── notebooks/
│   ├── 01_generador_dockerfile.ipynb
│   ├── 02_generador_manifiestos_k8s.ipynb
│   ├── 03_planificador_recursos_k8s.ipynb
│   ├── 04_generador_configmaps_y_secrets.ipynb
│   ├── 05_generador_pvc_y_resources.ipynb
│   └── README.md
└── examples/
    ├── docker/
    │   ├── hola-nginx/
    │   ├── fullstack-demo/
    │   ├── python-api/
    │   └── compose-web-api/
    └── k8s/
        ├── fullstack-demo/
        ├── helm-demo/
        ├── hola-nginx/
        ├── configmap-secret/
        ├── ingress-demo/
        ├── job-cronjob/
        ├── network-policy-demo/
        ├── probes-demo/
        ├── python-api/
        ├── rbac-demo/
        ├── scaling-demo/
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

### Kubernetes

- Arquitectura del clúster y objetos fundamentales
- Pods, Deployments, StatefulSets, Jobs y CronJobs
- ConfigMaps, Secrets, volúmenes y almacenamiento
- Services, Ingress y comunicación interna
- Probes, recursos, seguridad y troubleshooting
- Helm, PV/PVC y laboratorios de scheduling
- RBAC, segmentación de red y patrones de escalado
- Entornos, CI/CD y GitOps como temas de nivel superior
- Tutorial guiado desde clúster local hasta despliegues más completos
- Proyecto fullstack comparable con Docker Compose

### Utilidades

- Notebooks para generar Dockerfiles
- Notebooks para construir manifiestos YAML
- Notebooks para estimar capacidad y requests
- Guía de uso en `notebooks/README.md`

## Material visual

Varios módulos del repositorio incluyen diagramas `Mermaid` para explicar:

- El flujo de build y ejecución con Docker
- La arquitectura de Docker y Docker Compose
- La arquitectura del clúster Kubernetes
- El tráfico entre `Service`, `Ingress` y `Pods`
- El recorrido completo del primer proyecto práctico
- Los tutoriales paso a paso de Docker y Kubernetes

## Seguimiento del proyecto

- [Bitácora](bitacora.md)
- [Changelog](changelog.md)
- [Plan de expansión](docs/plan-expansion.md)

## Primer paso sugerido

Empieza por la [introducción](docs/00-introduccion.md), luego recorre el [temario completo](docs/temario-completo.md) y después alterna teoría con los directorios de `examples/` y `notebooks/`.

## Próximos temas a añadir

El roadmap detallado del crecimiento del repositorio está en [docs/plan-expansion.md](docs/plan-expansion.md).

Ese documento ya incluye:

- fases de crecimiento
- entregables por etapa
- sprints sugeridos
- malla temática futura de Docker y Kubernetes
- banco de laboratorios y ejercicios
- rutas sugeridas por tipo de alumno
- riesgos y mitigaciones
- métricas de avance y calidad
- criterios de aceptación por bloque
