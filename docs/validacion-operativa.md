# Validacion operativa del repositorio

Este documento resume la validacion real ejecutada sobre el repositorio el 2026-06-09.

## Entorno usado

- Sistema local con Docker Desktop
- Cluster local `minikube`
- Perfil usado: `curso-k8s-ci`
- Contexto de `kubectl`: `curso-k8s-ci`

## Resumen rapido

Se validaron en vivo los caminos principales de despliegue del curso:

- `Kustomize` con `examples/k8s/kustomize-demo/overlays/dev`
- Helm con `examples/helm/python-api/`
- `cert-manager` con `examples/k8s/cert-manager-demo/`
- Argo CD con `examples/k8s/argocd-practical-demo/`
- observabilidad con `examples/k8s/observability-stack-demo/`

La `python-api` respondio correctamente en `/health` y expuso metricas reales en `/metrics`.

## Validaciones completadas

### 1. Kustomize

Se construyo la imagen `python-api:local`, se cargo en `minikube`, se aplico el overlay `dev` y el `Deployment` quedo `Ready`.

Comprobaciones realizadas:

- `kubectl apply -k examples/k8s/kustomize-demo/overlays/dev`
- `kubectl rollout status deployment/python-api -n kustomize-dev`
- peticion HTTP real a `/health`
- peticion HTTP real a `/metrics`

Resultado:

- `Service` operativo
- `Deployment` operativo
- endpoint de salud correcto
- metricas Prometheus visibles

### 2. Helm

Se instalo el chart `examples/helm/python-api/` con `values-dev.yaml` y la imagen local ya cargada en el cluster.

Comprobaciones realizadas:

- `helm install python-api-demo examples/helm/python-api -n helm-demo --create-namespace -f values-dev.yaml --set image.tag=local`
- `kubectl rollout status deployment/python-api-demo-python-api -n helm-demo`
- peticion HTTP real a `/health`
- peticion HTTP real a `/metrics`

Resultado:

- chart instalable
- `Deployment` listo
- `Service` operativo
- endpoint de salud correcto
- metricas visibles

### 3. cert-manager

Se instalo `cert-manager` con Helm y se aplico la demo local del repositorio.

Comprobaciones realizadas:

- despliegues `cert-manager`, `cert-manager-webhook` y `cert-manager-cainjector` en `Running`
- aplicacion de `namespace.yaml`, `clusterissuer-selfsigned.yaml`, `deployment.yaml`, `service.yaml` y `certificate.yaml`
- espera activa sobre `certificate/python-api-tls`

Resultado:

- `Certificate` en estado `Ready=True`
- `Secret` `python-api-tls` creado con tipo `kubernetes.io/tls`

### 4. Argo CD

Se instalaron los componentes principales de Argo CD y se aplico el ejemplo `app-of-apps` del repositorio.

Comprobaciones realizadas:

- `argocd-server`, `argocd-repo-server` y `argocd-application-controller` en ejecucion
- `AppProject` `curso-demo` aplicado correctamente
- `Root Application` sincronizada y sana con los manifiestos locales corregidos
- `python-api-helm-demo` sincronizada y respondiendo en `/health`
- `python-api-kustomize-demo` sincronizada y respondiendo en `/health`

Resultado:

- el flujo GitOps del ejemplo funciona en cluster real
- el ejemplo Helm queda `Synced`
- el ejemplo Kustomize queda `Synced` y `Healthy`

Nota local importante:

- en `minikube`, la app Helm puede quedarse en `Progressing` dentro de Argo CD mientras el `Ingress` no tenga direccion publicada
- esto no impide que los pods y el `Service` funcionen
- para exponer la ruta con direccion local suele hacer falta `minikube tunnel`

Nota sobre repositorio remoto:

- Argo CD sincroniza desde Git remoto, no desde el workspace local
- si se quiere que una instalacion fresca vea exactamente estos manifiestos corregidos, hay que publicar los cambios del repositorio remoto

### 5. Observabilidad completa

Se instalo `kube-prometheus-stack` y se aplicaron los recursos de observabilidad del repositorio.

Comprobaciones realizadas:

- `observability-kube-prometh-operator` en `Running`
- `observability-grafana` en `Running`
- `prometheus-observability-kube-prometh-prometheus` en `Running`
- `alertmanager-observability-kube-prometh-alertmanager` en `Running`
- `ServiceMonitor` `python-api`
- `PrometheusRule` `python-api`
- `ConfigMap` del dashboard de Grafana
- respuesta HTTP `200 OK` de Grafana en `/login`

Resultado:

- la pila minima de observabilidad del curso queda desplegable
- Prometheus y Grafana arrancan correctamente
- la demo de `python-api` queda conectable a metricas y dashboards

## Limitaciones y matices

### `kind` frente a `minikube`

El workflow `.github/workflows/kind-e2e.yml` ya estaba preparado y validado de forma estructural. La validacion viva de este documento se hizo en `minikube` porque `kind` no estaba instalado en este entorno local.

### Ingress local y salud de Argo CD

En laboratorios locales es normal que un `Ingress` aparezca sin direccion publicada. En ese caso Argo CD puede dejar la aplicacion en `Progressing` aunque:

- el `Deployment` este listo
- el `Service` tenga endpoints
- la aplicacion responda por `port-forward`

### GitOps y cambios no publicados

Si cambias manifiestos en local y no los publicas, Argo CD seguira leyendo la version remota del repositorio. Esto es especialmente visible en demos `app-of-apps`.

## Conclusiones

El plan principal del repositorio no solo quedo desarrollado como documentacion y ejemplos, sino tambien validado en vivo en los flujos mas importantes:

- despliegue con Kustomize
- despliegue con Helm
- TLS automatizado con `cert-manager`
- GitOps con Argo CD
- observabilidad con Prometheus y Grafana

Quedan como matices normales de laboratorio local la publicacion del repo remoto para GitOps fresco y la exposicion del `Ingress` con direccion publica local.
