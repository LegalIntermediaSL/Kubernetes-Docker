# Changelog

Este archivo registra los cambios relevantes del repositorio.

## [0.1.0] - 2026-06-08

### Añadido

- `README.md` ampliado con objetivos, estructura del repositorio y ruta de aprendizaje.
- Documentación inicial en `docs/00-introduccion.md`.
- Documentación inicial en `docs/01-docker-fundamentos.md`.
- Documentación inicial en `docs/02-kubernetes-fundamentos.md`.
- Documentación inicial en `docs/03-primer-proyecto.md`.
- Ejemplo Docker en `examples/docker/hola-nginx/`.
- Manifiestos Kubernetes en `examples/k8s/hola-nginx/`.
- `bitacora.md` para seguimiento narrativo del proyecto.
- `changelog.md` para historial de cambios.

## [0.2.0] - 2026-06-08

### Añadido

- `docs/temario-completo.md` como mapa global del curso.
- Módulos avanzados de Docker en `docs/docker/`.
- Módulos avanzados de Kubernetes en `docs/kubernetes/`.
- Ejemplo de API Python contenedorizada en `examples/docker/python-api/`.
- Ejemplo multi-servicio con Docker Compose en `examples/docker/compose-web-api/`.
- Ejemplos de ConfigMap y Secret en `examples/k8s/configmap-secret/`.
- Ejemplo de Ingress en `examples/k8s/ingress-demo/`.
- Ejemplos de Job y CronJob en `examples/k8s/job-cronjob/`.
- Notebooks de utilidades en `notebooks/`.

### Cambiado

- `README.md` reorganizado para reflejar el temario ampliado.
- Documentos introductorios enlazados con los nuevos módulos profundos.
- Se añadieron diagramas Mermaid en documentación clave de Docker y Kubernetes.

## [0.3.0] - 2026-06-08

### Añadido

- Tutorial completo de Docker en `docs/docker/07-tutorial-docker-paso-a-paso.md`.
- Tutorial completo de Kubernetes en `docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md`.
- Ejemplo `examples/k8s/python-api/` para desplegar la API Python del bloque Docker.

### Cambiado

- `README.md` y `docs/temario-completo.md` actualizados para incluir los tutoriales guiados.
- `docs/01-docker-fundamentos.md` y `docs/02-kubernetes-fundamentos.md` enlazados con los tutoriales detallados.

## [0.4.0] - 2026-06-08

### Añadido

- `docs/plan-expansion.md` con una hoja de ruta detallada de crecimiento del curso.

### Cambiado

- `README.md` actualizado para enlazar el plan de expansión.
- `docs/temario-completo.md` ampliado con una sección de roadmap del repositorio.

## [0.4.1] - 2026-06-08

### Cambiado

- `docs/plan-expansion.md` ampliado con bastante más detalle operativo, pedagógico y técnico.
- `README.md` actualizado para resumir mejor el contenido del roadmap.

## [0.4.2] - 2026-06-08

### Cambiado

- `docs/plan-expansion.md` ampliado con malla temática futura, laboratorios, ejercicios, rutas de estudio, matrices de capacidades y herramientas recomendadas.
- `docs/temario-completo.md` y `README.md` actualizados para reflejar mejor la profundidad del roadmap.

## [0.5.0] - 2026-06-08

### Añadido

- `docs/kubernetes/09-helm-y-plantillas.md`.
- `docs/kubernetes/10-storage-pv-pvc.md`.
- `docs/kubernetes/11-probes-recursos-y-scheduling.md`.
- `examples/k8s/helm-demo/`.
- `examples/k8s/storage-demo/`.
- `examples/k8s/probes-demo/`.
- `notebooks/04_generador_configmaps_y_secrets.ipynb`.
- `notebooks/05_generador_pvc_y_resources.ipynb`.

### Cambiado

- `README.md`, `docs/temario-completo.md` y `docs/02-kubernetes-fundamentos.md` ampliados para incluir los nuevos módulos y laboratorios de la Fase 1.
- `docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md` enlazado con los nuevos módulos avanzados.

## [0.6.0] - 2026-06-08

### Añadido

- `docs/04-proyecto-multiservicio.md` como guía práctica comparando Compose y Kubernetes.
- `examples/docker/fullstack-demo/` con frontend, API Flask y Redis.
- `examples/k8s/fullstack-demo/` con frontend, API, Redis, `ConfigMap`, `Secret` e `Ingress`.

### Cambiado

- `README.md`, `docs/temario-completo.md`, `docs/03-primer-proyecto.md`, `docs/docker/05-docker-compose.md` y `docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md` actualizados para enlazar el nuevo laboratorio fullstack.

## [0.7.0] - 2026-06-08

### Añadido

- `docs/kubernetes/12-rbac-network-policies-y-aislamiento.md`.
- `docs/kubernetes/13-statefulsets-hpa-y-patrones-de-escalado.md`.
- `docs/kubernetes/14-entornos-ci-cd-y-gitops.md`.
- `examples/k8s/rbac-demo/`.
- `examples/k8s/network-policy-demo/`.
- `examples/k8s/scaling-demo/`.

### Cambiado

- `README.md` y `docs/temario-completo.md` reorganizados para abrir explícitamente un bloque de nivel superior.
- `docs/kubernetes/11-probes-recursos-y-scheduling.md` y `docs/04-proyecto-multiservicio.md` enlazados con los nuevos temas avanzados.
