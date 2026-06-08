# Bitácora del proyecto

Registro de trabajo, decisiones y próximos pasos del repositorio.

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

### Decisiones tomadas

- El curso se redacta en español.
- El enfoque inicial será práctico y progresivo.
- El primer ejemplo usa `nginx` para reducir complejidad y centrarse en contenedores y despliegue.

### Próximos pasos sugeridos

- Ejecutar la Fase 1 del plan de expansión.
- Consolidar o ampliar los laboratorios recién añadidos.
- Añadir ejemplos con `PersistentVolumeClaim` más cercanos a aplicaciones reales.
- Incorporar ejercicios de seguridad, probes y recursos.
- Empaquetar el proyecto multiservicio con Helm.
