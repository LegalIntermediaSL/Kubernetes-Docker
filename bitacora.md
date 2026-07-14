# Bitácora del proyecto

Registro de trabajo, decisiones y próximos pasos del repositorio.

## 2026-06-22

### Trabajo realizado

- Se añadio soporte completo de MkDocs para convertir `docs/` en un sitio navegable.
- Se ampliaron los contenidos avanzados de Kubernetes con dos modulos nuevos:
  - `docs/kubernetes/32-disponibilidad-scheduling-y-cuotas.md`
  - `docs/kubernetes/33-supply-chain-trivy-sbom-y-firma.md`
- Se abrio una segunda ampliacion avanzada con dos modulos adicionales:
  - `docs/kubernetes/34-gateway-api-y-httproute.md`
  - `docs/kubernetes/35-progressive-delivery-con-argo-rollouts.md`
- Se amplio despues la especializacion de GitOps seguro con:
  - `docs/kubernetes/36-sops-sealed-secrets-y-gitops-seguro.md`
- Se creo un laboratorio nuevo en `examples/k8s/scheduling-policy-demo/` para practicar:
  - `PodDisruptionBudget`
  - `PriorityClass`
  - `ResourceQuota`
  - `LimitRange`
  - reparto de replicas con `anti-affinity` y `topologySpreadConstraints`
- Se añadieron dos laboratorios mas:
  - `examples/k8s/sops-demo/`
  - `examples/k8s/sealed-secrets-demo/`
  - `examples/k8s/gateway-api-demo/`
  - `examples/k8s/argo-rollouts-demo/`
- Se creo `mkdocs.yml` con:
  - `site_name`
  - `nav` manual basada en el temario
  - plugin `mermaid2` para conservar los diagramas del curso
  - hoja de estilo adicional para la portada
- Se creo `docs/index.md` como landing page del sitio.
- Se añadieron dependencias de documentacion en `requirements-docs.txt`.
- Se ampliaron `Makefile` y `README.md` con comandos para servir, construir y validar la documentacion.
- Se actualizo `ci.yml` para ejecutar `mkdocs build --strict` en CI.
- Se amplio el validador offline `scripts/validate_k8s_examples.py` para cubrir `PodDisruptionBudget`, `PriorityClass`, `LimitRange` y `ResourceQuota`.

### Decisiones tomadas

- Se mantiene `docs/` como fuente principal del sitio para no duplicar el contenido del curso.
- La navegacion del sitio queda definida manualmente para respetar el orden pedagogico del temario y no depender del orden alfabetico por archivo.
- Los diagramas `Mermaid` se conservan en el sitio mediante `mkdocs-mermaid2-plugin`, ya que el repositorio usa Mermaid de forma intensa y perder ese render degradaria mucho la experiencia.
- El despliegue a GitHub Pages no se activa todavia; primero se deja estable el build y la validacion del sitio dentro de la CI actual.
- La expansion del curso se orienta ya a especializacion practica de plataforma, no a reabrir el bloque base.
- El siguiente valor pedagogico esta en disponibilidad, cuotas y trazabilidad del artefacto, no en multiplicar ejemplos basicos equivalentes.
- La siguiente capa logica despues de supply chain y cuotas es trafico moderno y despliegue progresivo, porque conecta red, observabilidad y riesgo de cambio.
- GitOps quedaba todavia cojo sin un bloque especifico de secretos cifrados en Git, asi que se abrio una comparativa practica entre `SOPS`, `Sealed Secrets` y `External Secrets`.

### Próximos pasos sugeridos

- Si se quiere publicar la documentacion automaticamente, el siguiente paso natural es un workflow de deploy a GitHub Pages.
- Tambien se puede abrir una segunda fase para traer al sitio una vista mas integrada de `examples/` y `notebooks/`, ya sea con paginas puente o con una estrategia de documentacion adicional.
- Si se sigue ampliando Kubernetes, lo mas natural ahora es bajar a implementaciones concretas de `Gateway API`, analisis automatizado en Argo Rollouts o providers reales, no repetir temas ya cubiertos.
- A partir de aqui, la ampliacion mas natural seria conectar `Argo Rollouts` con analisis Prometheus real o aterrizar `Gateway API` sobre un controlador concreto del laboratorio local.
- Otra siguiente fase razonable seria bajar `SOPS` a un laboratorio GitOps completo con Flux o mostrar `Sealed Secrets` con rotacion de certificados.

## 2026-06-21

### Trabajo realizado

- Se endurecio la ruta base de Kubernetes para que deje de depender del namespace por defecto.
- Se añadieron namespaces explicitos en:
  - `examples/k8s/hola-nginx/`
  - `examples/k8s/python-api/`
  - `examples/k8s/configmap-secret/`
  - `examples/k8s/ingress-demo/`
  - `examples/k8s/job-cronjob/`
- Se actualizo la documentacion principal afectada:
  - `docs/02-kubernetes-fundamentos.md`
  - `docs/03-primer-proyecto.md`
  - `docs/kubernetes/08-tutorial-kubernetes-paso-a-paso.md`
  - `docs/06-laboratorio-local-avanzado.md`
  - README de los laboratorios base en `examples/k8s/`
- Se amplio el `Makefile` con validaciones repetibles para:
  - `ConfigMap` y `Secret`
  - `Job` y `CronJob`
- Se amplio el workflow `kind-e2e.yml` para cubrir esos laboratorios base adicionales.
- Se sustituyo la idea inicial de validacion `kubectl apply --dry-run=client` por una validacion offline propia en `scripts/validate_k8s_examples.py`, mas estable para CI sin cluster.

### Decisiones tomadas

- La ruta base de Kubernetes debe reflejar habitos mas cercanos a entornos reales, aunque eso anada un poco mas de sintaxis con `-n`.
- La validacion de manifests no debe depender de tener un API server disponible si el objetivo es CI estructural del repositorio.
- Los laboratorios avanzados con CRDs siguen validandose por parseo, render o e2e segun el caso; los manifests nativos del curso reciben ahora una validacion semantica offline mas estricta.

### Próximos pasos sugeridos

- Si se quiere seguir endureciendo Kubernetes, el siguiente salto natural es anadir checks de politica o conformidad sobre recursos, no tanto mas contenido.
- Otra mejora posible seria separar mejor los laboratorios que dependen de controladores externos mediante perfiles o matrices de validacion por capacidad del cluster.

## 2026-06-13

### Trabajo realizado

- Se alineo `README.md` con el estado real del repositorio para presentar el curso base como ya completado.
- Se ajusto `docs/temario-completo.md` para tratar el roadmap como trazabilidad historica y no como lista de pendientes del recorrido principal.
- Se aclaro `docs/plan-expansion.md` como documento historico del diseno y crecimiento del proyecto.
- Se anadieron indices navegables en `examples/README.md`, `examples/docker/README.md`, `examples/k8s/README.md` y `examples/helm/README.md`.
- Se completaron los `README.md` que faltaban en los ejemplos base mas utilizados:
  - `examples/docker/hola-nginx/`
  - `examples/docker/python-api/`
  - `examples/k8s/hola-nginx/`
  - `examples/k8s/configmap-secret/`
  - `examples/k8s/ingress-demo/`
  - `examples/k8s/job-cronjob/`

### Decisiones tomadas

- El proyecto queda cerrado como curso base completo; cualquier trabajo posterior entra ya en especializacion y no en contenido imprescindible.
- Cada laboratorio principal debe poder entenderse y ejecutarse desde su propio directorio, sin depender de leer primero todo el temario.
- El roadmap se mantiene por trazabilidad y memoria de diseno, no como señal de que el repositorio siga incompleto.

### Próximos pasos sugeridos

- No hacen falta mas entregables para cerrar el curso base.
- Si el repositorio vuelve a crecer, lo natural seria abrir lineas de especializacion separadas: supply chain security, cloud providers concretos o stacks de plataforma mas opinionados.

## 2026-06-12

### Trabajo realizado

- Se completó la ampliación del bloque Docker con tres módulos nuevos:
  - `docs/docker/10-buildkit-multi-stage-y-optimizacion.md`
  - `docs/docker/11-debugging-runtime-redes-y-senales.md`
  - `docs/docker/12-volumenes-backup-y-limpieza-operativa.md`
- Se añadieron tres laboratorios Docker complementarios:
  - `examples/docker/python-api-optimized/`
  - `examples/docker/runtime-debug-demo/`
  - `examples/docker/volume-backup-demo/`
- Se amplió `docs/05-retos-practicos.md` para cubrir optimización de imágenes, runtime debugging, backup de volúmenes, `External Secrets` y KEDA.
- Se cerró mejor la navegación global del curso en `README.md`, `docs/temario-completo.md` y `docs/01-docker-fundamentos.md`.
- Se añadieron tres modulos nuevos de Kubernetes avanzado y operacion aplicada:
  - `docs/kubernetes/29-backup-restore-y-disaster-recovery.md`
  - `docs/kubernetes/30-external-secrets-y-secret-stores.md`
  - `docs/kubernetes/31-keda-y-event-driven-autoscaling.md`
- Se añadieron tres laboratorios nuevos:
  - `examples/k8s/backup-demo/`
  - `examples/k8s/external-secrets-demo/`
  - `examples/k8s/keda-demo/`
- El laboratorio de backup quedo centrado en `PVC`, `CronJob` y `Job` de restore para explicar el flujo completo sin depender de herramientas externas.
- El laboratorio de External Secrets quedo planteado con sincronizacion entre namespaces para enseñar el modelo `SecretStore -> ExternalSecret -> Secret`.
- El laboratorio de KEDA quedo dividido en dos rutas:
  - escalado por horario con `cron`
  - escalado por metrica externa con Prometheus
- Se actualizo la navegacion principal del repositorio en `README.md`, `docs/temario-completo.md` y `docs/02-kubernetes-fundamentos.md`.

### Decisiones tomadas

- El cierre del temario no se limita a añadir mas Kubernetes; tambien refuerza Docker en optimizacion, diagnostico y operacion local para equilibrar el curso.
- Los laboratorios Docker nuevos se dejaron pequenos y didacticos para que sirvan tanto en local como en explicaciones de clase.
- La ampliacion del curso sigue priorizando contenido practico y ejemplos ejecutables antes que texto puramente teorico.
- Los ejemplos de operadores avanzados se dejaron en variantes didacticas y locales para no depender de cloud providers concretos.
- El ejemplo de KEDA con Prometheus se mantiene con `minReplicaCount: 1` porque una metrica scrapeada desde los pods no es una buena base para escalar a `0`.

### Próximos pasos sugeridos

- Si el curso sigue creciendo, el siguiente salto ya sería especialización: supply chain security, `SBOM`, `Trivy`, `Sealed Secrets` o proveedores cloud concretos.
- Añadir una capa mas operativa de backups de base de datos con `pg_dump` o herramientas equivalentes si se quiere profundizar en persistencia real.
- Sumar un bloque de `Sealed Secrets` o `SOPS` si el curso quiere cubrir tambien secretos cifrados en Git.
- Conectar KEDA con una cola real como Redis o RabbitMQ para ampliar el bloque de event-driven autoscaling.

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
