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
16. [Primer proyecto práctico](docs/03-primer-proyecto.md)
17. [Temario completo](docs/temario-completo.md)

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
│       └── 08-tutorial-kubernetes-paso-a-paso.md
├── notebooks/
│   ├── 01_generador_dockerfile.ipynb
│   ├── 02_generador_manifiestos_k8s.ipynb
│   ├── 03_planificador_recursos_k8s.ipynb
│   └── README.md
└── examples/
    ├── docker/
    │   ├── hola-nginx/
    │   ├── python-api/
    │   └── compose-web-api/
    └── k8s/
        ├── hola-nginx/
        ├── python-api/
        ├── configmap-secret/
        ├── ingress-demo/
        └── job-cronjob/
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

## Módulos principales

### Docker

- Conceptos base, imágenes, contenedores y ciclo de vida
- CLI diaria y flujos de inspección
- Dockerfiles, capas, caché y builds reproducibles
- Volúmenes, bind mounts y redes
- Docker Compose para aplicaciones multi-servicio
- Registros, seguridad, escaneo y depuración
- Tutorial guiado paso a paso con ejercicios y verificación

### Kubernetes

- Arquitectura del clúster y objetos fundamentales
- Pods, Deployments, StatefulSets, Jobs y CronJobs
- ConfigMaps, Secrets, volúmenes y almacenamiento
- Services, Ingress y comunicación interna
- Probes, recursos, seguridad y troubleshooting
- Tutorial guiado desde clúster local hasta despliegues más completos

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
