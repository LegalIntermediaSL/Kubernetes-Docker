# Temario completo

Este documento reúne el mapa general del curso para que puedas ver el recorrido completo antes de entrar en cada módulo.

## Bloque 1: fundamentos

1. [Introducción a Docker y Kubernetes](00-introduccion.md)
2. [Fundamentos de Docker](01-docker-fundamentos.md)
3. [Fundamentos de Kubernetes](02-kubernetes-fundamentos.md)
4. [Primer proyecto práctico](03-primer-proyecto.md)

## Bloque 2: Docker en profundidad

1. [Arquitectura y CLI de Docker](docker/02-arquitectura-y-cli.md)
2. [Dockerfiles y buenas prácticas](docker/03-dockerfiles-y-buenas-practicas.md)
3. [Volúmenes, redes y persistencia](docker/04-volumenes-redes-y-persistencia.md)
4. [Docker Compose](docker/05-docker-compose.md)
5. [Registro, seguridad y troubleshooting](docker/06-registry-seguridad-troubleshooting.md)
6. [Tutorial detallado de Docker](docker/07-tutorial-docker-paso-a-paso.md)

### Objetivos del bloque

- Entender el modelo mental de imágenes, capas, contenedores y registros.
- Saber construir imágenes pequeñas y mantenibles.
- Dominar persistencia, red y ejecución de múltiples servicios.
- Diagnosticar errores frecuentes en tiempo de build y runtime.

## Bloque 3: Kubernetes en profundidad

1. [Arquitectura del clúster](kubernetes/03-arquitectura-del-cluster.md)
2. [Workloads y actualizaciones](kubernetes/04-workloads-y-actualizaciones.md)
3. [ConfigMaps, Secrets y almacenamiento](kubernetes/05-configmaps-secrets-y-storage.md)
4. [Services, Ingress y red](kubernetes/06-services-ingress-y-red.md)
5. [Observabilidad, seguridad y depuración](kubernetes/07-observabilidad-seguridad-y-debug.md)
6. [Tutorial detallado de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)

### Objetivos del bloque

- Comprender cómo Kubernetes reconcilia el estado deseado.
- Desplegar aplicaciones stateless y batch.
- Gestionar configuración externa y recursos persistentes.
- Exponer servicios con topologías de red claras.
- Diagnosticar pods, eventos, logs y errores de scheduling.

## Bloque 4: tutoriales guiados

- [Tutorial detallado de Docker](docker/07-tutorial-docker-paso-a-paso.md)
- [Tutorial detallado de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)

Estos tutoriales sirven como recorrido continuo y practico. La idea es que no solo leas conceptos sueltos, sino que completes una secuencia de comandos y verificaciones de principio a fin.

## Bloque 5: ejemplos y laboratorio

### Docker

- `examples/docker/hola-nginx/`
- `examples/docker/python-api/`
- `examples/docker/compose-web-api/`

### Kubernetes

- `examples/k8s/hola-nginx/`
- `examples/k8s/python-api/`
- `examples/k8s/configmap-secret/`
- `examples/k8s/ingress-demo/`
- `examples/k8s/job-cronjob/`

## Bloque 6: notebooks de utilidades

- `notebooks/01_generador_dockerfile.ipynb`
- `notebooks/02_generador_manifiestos_k8s.ipynb`
- `notebooks/03_planificador_recursos_k8s.ipynb`

## Bloque 7: roadmap del repositorio

- [Plan de expansión](plan-expansion.md)

Este bloque sirve para orientar el crecimiento del curso y priorizar nuevos módulos, ejemplos y automatizaciones.

### Qué contiene el roadmap

- fases de crecimiento por prioridad
- malla temática futura de Docker
- malla temática futura de Kubernetes
- banco de laboratorios y ejercicios
- ruta sugerida por semanas y por perfil de alumno
- métricas, riesgos, hitos y criterios de aceptación

## Sugerencia de estudio

Si aprendes mejor construyendo:

1. Lee un módulo corto.
2. Ejecuta el ejemplo correspondiente.
3. Modifica algo pequeño.
4. Documenta lo aprendido en `bitacora.md`.

Si aprendes mejor desde sistemas:

1. Lee primero los fundamentos de Docker y Kubernetes.
2. Estudia arquitectura, redes y almacenamiento.
3. Termina con troubleshooting y seguridad.

## Evaluación sugerida

Al final del temario deberías poder:

- Escribir un `Dockerfile` razonable sin copiarlo de memoria.
- Construir y ejecutar una aplicación con múltiples servicios.
- Crear manifiestos YAML básicos sin depender de un generador.
- Entender por qué un pod no arranca o por qué un service no enruta.
- Diseñar un despliegue simple con configuración externa y health checks.
