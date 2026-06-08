# Kubernetes-Docker

Tutorial práctico de Docker y Kubernetes en español.

Este repositorio empieza como una base de curso para aprender a:

- Entender qué problema resuelve Docker.
- Construir imágenes y ejecutar contenedores.
- Comprender los conceptos centrales de Kubernetes.
- Desplegar una aplicación sencilla en un clúster local.

## Para quién es este tutorial

Este material está pensado para:

- Personas que ya programan y quieren dar el salto a contenedores.
- Equipos que usan Docker pero todavía no dominan Kubernetes.
- Estudiantes que prefieren aprender con ejemplos pequeños y ejecutables.

## Ruta de aprendizaje

1. [Introducción a Docker y Kubernetes](docs/00-introduccion.md)
2. [Fundamentos de Docker](docs/01-docker-fundamentos.md)
3. [Fundamentos de Kubernetes](docs/02-kubernetes-fundamentos.md)
4. [Primer proyecto práctico](docs/03-primer-proyecto.md)

## Estructura del repositorio

```text
.
├── bitacora.md
├── changelog.md
├── docs/
│   ├── 00-introduccion.md
│   ├── 01-docker-fundamentos.md
│   ├── 02-kubernetes-fundamentos.md
│   └── 03-primer-proyecto.md
└── examples/
    ├── docker/
    │   └── hola-nginx/
    │       ├── Dockerfile
    │       └── index.html
    └── k8s/
        └── hola-nginx/
            ├── deployment.yaml
            └── service.yaml
```

## Requisitos recomendados

- Docker Desktop o Docker Engine
- `kubectl`
- Un clúster local: `kind` o `minikube`
- Terminal y editor de texto

## Cómo usar este repositorio

La forma recomendada es avanzar por los documentos en orden y ejecutar cada bloque práctico. El repositorio irá creciendo con:

- Más capítulos
- Ejercicios guiados
- Ejemplos de aplicaciones
- Manifiestos de Kubernetes más completos

## Seguimiento del proyecto

- [Bitácora](bitacora.md)
- [Changelog](changelog.md)

## Primer paso sugerido

Empieza por la [introducción](docs/00-introduccion.md) y luego sigue con el [primer ejemplo práctico](docs/03-primer-proyecto.md) si prefieres aprender construyendo desde el principio.

## Próximos temas a añadir

- Volúmenes y persistencia en Docker
- Redes entre contenedores
- ConfigMaps y Secrets
- Ingress
- Helm
- CI/CD para contenedores
