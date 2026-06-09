# Bitácora del proyecto

Registro de trabajo, decisiones y próximos pasos del repositorio.

## 2026-06-09

### Trabajo realizado

- Se ejecutó una validación operativa real en un clúster local `minikube` con perfil `curso-k8s-ci`.
- Se comprobó en vivo el despliegue `Kustomize` de `examples/k8s/kustomize-demo/overlays/dev`.
- Se comprobó en vivo el chart Helm `examples/helm/python-api/`.
- La `python-api` quedó verificada en `/health` y `/metrics`.
- Se instaló y validó `cert-manager`, incluyendo la creación del `Certificate` `python-api-tls`.
- Se instaló y validó la pila de observabilidad con Prometheus, Alertmanager y Grafana.
- Se aplicó y verificó el bloque práctico de Argo CD con `AppProject`, `Root Application` y aplicaciones hijas.
- Se ajustaron los manifiestos de Argo CD para apuntar al remoto actual del repositorio.
- Se documentó la validación real en `docs/validacion-operativa.md`.
- Se añadió un `Makefile` para repetir el laboratorio avanzado con objetivos locales y de CI.
- Se añadió `docs/06-laboratorio-local-avanzado.md` como guía ejecutable de la fase avanzada.
- El workflow `kind-e2e.yml` quedó alineado con el `Makefile` para evitar duplicación entre CI y uso local.

### Decisiones tomadas

- La validación viva local se documenta aparte del temario para distinguir teoría, ejemplos y evidencia operativa.
- El ejemplo de Argo CD mantiene la nota de que GitOps sincroniza desde Git remoto y no desde cambios no publicados del workspace local.
- El comportamiento `Progressing` de un `Ingress` sin dirección publicada se trata como matiz de laboratorio local, no como fallo del ejemplo.
- La automatización local debe vivir en el propio repositorio y no quedarse dispersa en comandos de bitácora.

### Próximos pasos sugeridos

- Publicar los cambios del repositorio remoto si se quiere que una instalación fresca de Argo CD consuma exactamente estos manifiestos corregidos.
- Estandarizar un laboratorio local con `minikube tunnel` o equivalente si se quiere que las demos con `Ingress` aparezcan sanas también a nivel de health de Argo CD.

## 2026-06-08

### Trabajo realizado

- Se amplió el `README.md` con una descripción más completa del curso.
- Se creó una ruta inicial de aprendizaje con cuatro documentos en `docs/`.
- Se añadió un ejemplo práctico con Docker en `examples/docker/hola-nginx/`.
- Se añadieron manifiestos base de Kubernetes en `examples/k8s/hola-nginx/`.
- Se creó esta bitácora y el archivo `changelog.md` para dar seguimiento a la evolución del proyecto.
- Se expandió el temario con módulos específicos de Docker y Kubernetes en subdirectorios de `docs/`.
- Se añadieron ejemplos nuevos de API Python, Docker Compose, ConfigMap/Secret, Ingress y Jobs.
- Se añadieron notebooks de utilidades para generar Dockerfiles, manifiestos y estimaciones de recursos.
- Se añadieron diagramas Mermaid en módulos clave para reforzar arquitectura, flujos y networking.
- Se añadieron dos tutoriales largos, uno de Docker y otro de Kubernetes, enlazados al temario principal.
- Se añadió un ejemplo de despliegue `python-api` en Kubernetes para conectar los laboratorios de Docker y clúster.
- Se desarrolló un plan de expansión detallado del repositorio con fases, prioridades, entregables y criterios de aceptación.
- Se amplió ese plan con mucho más detalle: alcance, perfiles de usuario, riesgos, métricas, hitos, roadmap de ejemplos, notebooks, validación y sprints.
- Se desarrolló aún más el contenido del plan con malla temática futura, banco de laboratorios, ejercicios por nivel, rutas por semanas, herramientas recomendadas y matrices de capacidad/verificación.
- Se materializó buena parte de la Fase 1 con tres módulos nuevos: Helm, storage y probes/recursos/scheduling.
- Se añadieron laboratorios `helm-demo`, `storage-demo` y `probes-demo`.
- Se añadieron dos notebooks nuevos para generar `ConfigMap`, `Secret`, `PVC` y bloques de recursos.
- Se amplió la parte práctica con un proyecto multiservicio completo en Compose y en Kubernetes.
- Se añadió una guía comparativa de proyecto fullstack en `docs/04-proyecto-multiservicio.md`.
- Se abrió un bloque superior del curso con RBAC, `NetworkPolicy`, `StatefulSet`, HPA, entornos, CI/CD y GitOps.
- Se añadieron laboratorios `rbac-demo`, `network-policy-demo` y `scaling-demo`.
- Se añadió un chart Helm completo para `fullstack-demo` con valores `dev`, `demo` y `prod`.
- Se añadió un laboratorio de PostgreSQL con `PVC`, `Secret`, `ConfigMap`, `Service` y `readinessProbe`.
- Se añadieron nuevos módulos de cookbook de troubleshooting, seguridad aplicada y observabilidad práctica.
- Se añadieron documentos de CI/CD y workflows reales en `.github/workflows/`.
- Se añadió un bloque de retos prácticos para consolidar el aprendizaje por niveles.
- Se añadieron módulos nuevos de versionado/publicacion de imágenes y hardening de contenedores en Docker.
- Se añadió un chart Helm más completo para `python-api`, con `Ingress`, `ConfigMap`, recursos y values por entorno.
- Se añadió un workflow de publicación versionada de imágenes y un documento específico de promoción y releases.
- Se añadieron apéndices avanzados de TLS, GitOps, Prometheus/Grafana, policy-as-code y service mesh.
- Se añadieron laboratorios de referencia para `Ingress` con TLS, GitOps, Prometheus, policies y service mesh.
- Se añadieron dos notebooks nuevos para `values` Helm y checklist de release.
- Se añadió una fase avanzada adicional con `Kustomize`, `cert-manager`, Argo CD más práctico y observabilidad más completa.
- Se añadió un workflow `kind-e2e.yml` para validar despliegues reales en un clúster efímero.
- La `python-api` del curso ahora expone métricas en `/metrics` para conectar observabilidad y pruebas avanzadas.

### Decisiones tomadas

- El curso se redacta en español.
- El enfoque inicial será práctico y progresivo.
- El primer ejemplo usa `nginx` para reducir complejidad y centrarse en contenedores y despliegue.

### Próximos pasos sugeridos

- Profundizar solo si se quiere especialización por proveedor cloud o por stack concreto.
- Llevar la fase avanzada a integración real con controladores instalados si se define un entorno de laboratorio estándar.
- Añadir escenarios más ricos de base de datos, backup y recovery si el curso evoluciona hacia operación aplicada.
