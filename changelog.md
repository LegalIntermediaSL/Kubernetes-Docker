# Changelog

Este archivo registra los cambios relevantes del repositorio.

## [1.1.1] - 2026-06-09

### Añadido

- `docs/validacion-operativa.md` con la validación real del repositorio sobre `minikube`.
- `Makefile` para automatizar validaciones locales, despliegues del laboratorio avanzado e instalaciones base.
- `docs/06-laboratorio-local-avanzado.md` como guía de ejecución local del bloque avanzado.

### Cambiado

- `examples/k8s/argocd-practical-demo/` actualizado para apuntar al remoto actual del repositorio y documentar mejor el uso local.
- `docs/kubernetes/27-argocd-practico-app-of-apps-y-sync.md` ajustado para reflejar que el ejemplo ya usa el remoto real y para aclarar los matices de GitOps e `Ingress` en local.
- `README.md` y `bitacora.md` actualizados para enlazar y resumir la validación operativa en vivo.
- `.github/workflows/kind-e2e.yml` refactorizado para usar objetivos del `Makefile`.

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

## [0.8.0] - 2026-06-08

### Añadido

- `examples/helm/fullstack-demo/` con chart Helm completo para `frontend`, `api`, `redis`, `ConfigMap`, `Secret`, `Service` e `Ingress`.
- `examples/helm/fullstack-demo/values-dev.yaml`, `values-demo.yaml` y `values-prod.yaml` para promoción por entorno.
- `docs/kubernetes/15-postgres-pvc-y-inicializacion.md`.
- `examples/k8s/postgres-demo/` con `PVC`, `ConfigMap`, `Secret`, `Deployment` y `Service`.
- `docs/kubernetes/16-cookbook-de-troubleshooting.md`.
- `docs/kubernetes/17-seguridad-aplicada-y-hardening.md`.
- `docs/kubernetes/18-observabilidad-practica.md`.
- `docs/ci-cd/01-introduccion-ci-cd.md`.
- `docs/ci-cd/02-workflows-del-repo.md`.
- `.github/workflows/ci.yml`.
- `.github/workflows/docker-build.yml`.
- `.github/workflows/helm-validate.yml`.
- `docs/05-retos-practicos.md`.

### Cambiado

- `README.md` ampliado para reflejar la nueva capa práctica avanzada, el bloque de CI/CD y los retos.
- `docs/temario-completo.md` reorganizado para incluir operación, automatización y retos como bloques explícitos.
- `docs/plan-expansion.md` alineado con los entregables ya materializados en Helm, CI/CD y operación.
- `bitacora.md` actualizada con el trabajo realizado y los siguientes saltos de expansión.

## [1.0.0] - 2026-06-08

### Añadido

- `docs/docker/08-versionado-y-publicacion.md`.
- `docs/docker/09-seguridad-de-contenedores-y-hardening.md`.
- `docs/ci-cd/03-publicacion-promocion-y-releases.md`.
- `.github/workflows/publish-images.yml`.
- `examples/helm/python-api/` con chart completo y `values` por entorno.
- `docs/kubernetes/19-helm-tutorial-paso-a-paso.md`.
- `docs/kubernetes/20-ingress-tls-y-exposicion-avanzada.md`.
- `docs/kubernetes/21-gitops-intro-argocd-y-flux.md`.
- `docs/kubernetes/22-observabilidad-con-prometheus-y-grafana.md`.
- `docs/kubernetes/23-policies-con-gatekeeper-y-kyverno.md`.
- `docs/kubernetes/24-service-mesh-introduccion.md`.
- `examples/k8s/ingress-tls-demo/`.
- `examples/k8s/gitops-demo/`.
- `examples/k8s/prometheus-demo/`.
- `examples/k8s/policy-demo/`.
- `examples/k8s/service-mesh-demo/`.
- `notebooks/06_generador_values_helm.ipynb`.
- `notebooks/07_checklist_release_ci_cd.ipynb`.

### Cambiado

- `README.md` y `docs/temario-completo.md` ampliados para reflejar el cierre del plan principal y la nueva capa de apéndices avanzados.
- `docs/plan-expansion.md` actualizado para indicar que el recorrido principal ya está materializado.
- `docs/ci-cd/01-introduccion-ci-cd.md` y `docs/ci-cd/02-workflows-del-repo.md` enlazados con el flujo de publicación.
- `.github/workflows/helm-validate.yml` ampliado para validar también el chart `examples/helm/python-api/`.

## [1.1.0] - 2026-06-08

### Añadido

- `docs/ci-cd/04-ci-end-to-end-con-kind.md`.
- `.github/workflows/kind-e2e.yml`.
- `docs/kubernetes/25-kustomize-bases-y-overlays.md`.
- `docs/kubernetes/26-cert-manager-y-tls-automatizado.md`.
- `docs/kubernetes/27-argocd-practico-app-of-apps-y-sync.md`.
- `docs/kubernetes/28-observabilidad-stack-completo.md`.
- `examples/k8s/kustomize-demo/`.
- `examples/k8s/cert-manager-demo/`.
- `examples/k8s/argocd-practical-demo/`.
- `examples/k8s/observability-stack-demo/`.

### Cambiado

- `examples/docker/python-api/app.py` y `requirements.txt` ampliados para exponer métricas Prometheus en `/metrics`.
- `examples/k8s/python-api/` y `examples/helm/python-api/` ajustados para usar puertos con nombre `http`, facilitando `ServiceMonitor`.
- `README.md`, `docs/temario-completo.md`, `bitacora.md` y `docs/plan-expansion.md` actualizados para reflejar la nueva fase avanzada posterior al plan base.
