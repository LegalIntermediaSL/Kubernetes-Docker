# Temario completo

Este documento reúne el mapa general del curso para que puedas ver el recorrido completo antes de entrar en cada módulo.

## Bloque 1: fundamentos

1. [Introducción a Docker y Kubernetes](00-introduccion.md)
2. [Fundamentos de Docker](01-docker-fundamentos.md)
3. [Fundamentos de Kubernetes](02-kubernetes-fundamentos.md)
4. [Primer proyecto práctico](03-primer-proyecto.md)
5. [Proyecto multiservicio](04-proyecto-multiservicio.md)

## Bloque 2: Docker en profundidad

1. [Arquitectura y CLI de Docker](docker/02-arquitectura-y-cli.md)
2. [Dockerfiles y buenas prácticas](docker/03-dockerfiles-y-buenas-practicas.md)
3. [Volúmenes, redes y persistencia](docker/04-volumenes-redes-y-persistencia.md)
4. [Docker Compose](docker/05-docker-compose.md)
5. [Registro, seguridad y troubleshooting](docker/06-registry-seguridad-troubleshooting.md)
6. [Tutorial detallado de Docker](docker/07-tutorial-docker-paso-a-paso.md)
7. [Versionado y publicacion de imagenes](docker/08-versionado-y-publicacion.md)
8. [Seguridad de contenedores y hardening](docker/09-seguridad-de-contenedores-y-hardening.md)

### Objetivos del bloque

- Entender el modelo mental de imágenes, capas, contenedores y registros.
- Saber construir imágenes pequeñas y mantenibles.
- Dominar persistencia, red y ejecución de múltiples servicios.
- Diagnosticar errores frecuentes en tiempo de build y runtime.
- Versionar y publicar imágenes con mejor trazabilidad.
- Entender el hardening básico de una imagen contenedorizada.

## Bloque 3: Kubernetes en profundidad

1. [Arquitectura del clúster](kubernetes/03-arquitectura-del-cluster.md)
2. [Workloads y actualizaciones](kubernetes/04-workloads-y-actualizaciones.md)
3. [ConfigMaps, Secrets y almacenamiento](kubernetes/05-configmaps-secrets-y-storage.md)
4. [Services, Ingress y red](kubernetes/06-services-ingress-y-red.md)
5. [Observabilidad, seguridad y depuración](kubernetes/07-observabilidad-seguridad-y-debug.md)
6. [Tutorial detallado de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)
7. [Helm y plantillas](kubernetes/09-helm-y-plantillas.md)
8. [Storage, PV y PVC](kubernetes/10-storage-pv-pvc.md)
9. [Probes, recursos y scheduling](kubernetes/11-probes-recursos-y-scheduling.md)

### Objetivos del bloque

- Comprender cómo Kubernetes reconcilia el estado deseado.
- Desplegar aplicaciones stateless y batch.
- Gestionar configuración externa y recursos persistentes.
- Exponer servicios con topologías de red claras.
- Diagnosticar pods, eventos, logs y errores de scheduling.
- Entender cómo empaquetar con Helm y cómo persisten realmente los datos.
- Explicar por qué un pod no queda `Ready`, reinicia o no puede planificarse.

## Bloque 4: temas de nivel superior

1. [RBAC, NetworkPolicies y aislamiento](kubernetes/12-rbac-network-policies-y-aislamiento.md)
2. [StatefulSet, HPA y patrones de escalado](kubernetes/13-statefulsets-hpa-y-patrones-de-escalado.md)
3. [Entornos, CI/CD y GitOps](kubernetes/14-entornos-ci-cd-y-gitops.md)
4. [Postgres, PVC e inicialización](kubernetes/15-postgres-pvc-y-inicializacion.md)
5. [Cookbook de troubleshooting](kubernetes/16-cookbook-de-troubleshooting.md)
6. [Seguridad aplicada y hardening](kubernetes/17-seguridad-aplicada-y-hardening.md)
7. [Observabilidad práctica](kubernetes/18-observabilidad-practica.md)

### Objetivos del bloque

- Conectar el bloque intermedio con preocupaciones reales de plataforma.
- Entender permisos, identidad y segmentación básica de red.
- Distinguir patrones stateless de cargas con identidad estable.
- Comprender el salto desde YAML y Helm hacia promoción por entornos y automatización.
- Practicar persistencia con una base de datos más realista.
- Desarrollar reflejos de diagnóstico, endurecimiento y lectura operativa del clúster.

## Bloque 5: automatización y entrega

1. [Introducción a CI/CD](ci-cd/01-introduccion-ci-cd.md)
2. [Workflows del repositorio](ci-cd/02-workflows-del-repo.md)
3. [Publicacion, promocion y releases](ci-cd/03-publicacion-promocion-y-releases.md)

### Objetivos del bloque

- Entender qué se puede validar automáticamente antes de desplegar.
- Leer workflows pequeños sin que parezcan magia.
- Relacionar Compose, Docker, Helm y YAML con una CI mínima y didáctica.
- Entender cómo una imagen versionada se promueve entre entornos.

## Bloque 6: apendices avanzados

1. [Helm tutorial paso a paso](kubernetes/19-helm-tutorial-paso-a-paso.md)
2. [Ingress, TLS y exposicion avanzada](kubernetes/20-ingress-tls-y-exposicion-avanzada.md)
3. [GitOps: Argo CD y Flux](kubernetes/21-gitops-intro-argocd-y-flux.md)
4. [Prometheus, Grafana y metricas](kubernetes/22-observabilidad-con-prometheus-y-grafana.md)
5. [Policies con Gatekeeper y Kyverno](kubernetes/23-policies-con-gatekeeper-y-kyverno.md)
6. [Introduccion a service mesh](kubernetes/24-service-mesh-introduccion.md)
7. [Kustomize: bases y overlays](kubernetes/25-kustomize-bases-y-overlays.md)
8. [cert-manager y TLS automatizado](kubernetes/26-cert-manager-y-tls-automatizado.md)
9. [Argo CD practico: app-of-apps y sync](kubernetes/27-argocd-practico-app-of-apps-y-sync.md)
10. [Observabilidad completa con Prometheus y Grafana](kubernetes/28-observabilidad-stack-completo.md)

### Objetivos del bloque

- Cerrar el recorrido del curso con temas frecuentes en plataformas modernas.
- Entender cuando un tema avanzado aporta valor y cuando aun no hace falta.
- Dar un puente hacia GitOps, gobierno, TLS, metricas y trafico avanzado.
- Mostrar una fase avanzada mas operativa y ejecutable sobre la base del curso.

## Bloque 7: CI y validacion avanzada

1. [CI end-to-end con kind](ci-cd/04-ci-end-to-end-con-kind.md)

### Objetivos del bloque

- Comprobar que una parte del curso no solo renderiza, sino que despliega y responde en un cluster efimero.
- Conectar la validacion documental con una verificacion mas operativa.

## Bloque 8: tutoriales guiados

- [Tutorial detallado de Docker](docker/07-tutorial-docker-paso-a-paso.md)
- [Tutorial detallado de Kubernetes](kubernetes/08-tutorial-kubernetes-paso-a-paso.md)

Estos tutoriales sirven como recorrido continuo y practico. La idea es que no solo leas conceptos sueltos, sino que completes una secuencia de comandos y verificaciones de principio a fin.

## Bloque 9: ejemplos y laboratorio

### Docker

- `examples/docker/fullstack-demo/`
- `examples/docker/hola-nginx/`
- `examples/docker/python-api/`
- `examples/docker/compose-web-api/`

### Helm

- `examples/helm/python-api/`
- `examples/helm/fullstack-demo/`

### Kubernetes

- `examples/k8s/argocd-practical-demo/`
- `examples/k8s/cert-manager-demo/`
- `examples/k8s/fullstack-demo/`
- `examples/k8s/gitops-demo/`
- `examples/k8s/helm-demo/`
- `examples/k8s/hola-nginx/`
- `examples/k8s/ingress-tls-demo/`
- `examples/k8s/kustomize-demo/`
- `examples/k8s/network-policy-demo/`
- `examples/k8s/observability-stack-demo/`
- `examples/k8s/policy-demo/`
- `examples/k8s/postgres-demo/`
- `examples/k8s/prometheus-demo/`
- `examples/k8s/python-api/`
- `examples/k8s/rbac-demo/`
- `examples/k8s/scaling-demo/`
- `examples/k8s/service-mesh-demo/`
- `examples/k8s/configmap-secret/`
- `examples/k8s/ingress-demo/`
- `examples/k8s/job-cronjob/`
- `examples/k8s/probes-demo/`
- `examples/k8s/storage-demo/`

## Bloque 10: notebooks de utilidades

- `notebooks/01_generador_dockerfile.ipynb`
- `notebooks/02_generador_manifiestos_k8s.ipynb`
- `notebooks/03_planificador_recursos_k8s.ipynb`
- `notebooks/04_generador_configmaps_y_secrets.ipynb`
- `notebooks/05_generador_pvc_y_resources.ipynb`
- `notebooks/06_generador_values_helm.ipynb`
- `notebooks/07_checklist_release_ci_cd.ipynb`

## Bloque 11: retos prácticos

- [Retos prácticos](05-retos-practicos.md)

Este bloque sirve para consolidar el aprendizaje rompiendo y reparando ejemplos del repositorio en lugar de limitarse a repetir comandos.

## Bloque 12: roadmap del repositorio

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
- Comparar una misma aplicación multi-servicio en Compose y Kubernetes.
- Explicar qué cambia al pasar del bloque intermedio a temas de plataforma de nivel superior.
- Describir un flujo razonable de versionado, publicación, GitOps y gobierno básico.
- Entender cuándo conviene añadir `Kustomize`, `cert-manager`, Argo CD y observabilidad más completa.
