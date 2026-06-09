# Argo CD Practical Demo

Ejemplo de `app-of-apps` para Argo CD mezclando una aplicacion basada en Helm y otra basada en `Kustomize`.

## Archivos

- `project.yaml`
- `root-application.yaml`
- `applications/python-api-helm-demo.yaml`
- `applications/python-api-kustomize-demo.yaml`

## Nota

Los manifiestos ya apuntan al remoto actual del repositorio, pero sigues pudiendo adaptar `repoURL`, ramas o namespaces si quieres reutilizar la demo en otro proyecto.

## Nota para cluster local

Si ejecutas esta demo en `minikube` o en otro cluster local:

- la aplicacion Helm puede quedar en `Progressing` en Argo CD mientras el `Ingress` no tenga direccion publicada
- la aplicacion Kustomize del overlay `demo` usa una etiqueta de imagen pensada para registry, asi que debes publicarla o cargar esa misma etiqueta en tu cluster local
- si cambias estos manifiestos solo en tu workspace local, Argo CD no vera esos cambios hasta que existan en Git remoto
