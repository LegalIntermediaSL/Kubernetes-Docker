# External Secrets y Secret Stores

Los `Secret` nativos de Kubernetes resuelven parte del problema, pero no todos.

Si guardas credenciales directamente en YAML:

- acabas discutiendo donde meterlas
- duplicas secretos por entorno
- pierdes trazabilidad de rotacion
- complicas GitOps

Este bloque introduce una capa mas realista: un operador que sincroniza secretos desde una fuente externa o compartida hacia un `Secret` local consumible por tu aplicacion.

## Que problema resuelve este bloque

Un `ExternalSecret` no reemplaza el concepto de secreto. Lo que cambia es la fuente de verdad.

En vez de pensar:

- "este YAML contiene la password"

pasas a pensar:

- "este recurso describe de donde viene la password y como se materializa en el namespace de trabajo"

## Mapa conceptual

```mermaid
flowchart LR
    SRC["Secret origen o proveedor"] --> STORE["SecretStore"]
    STORE --> ESO["ExternalSecret"]
    ESO --> TGT["Secret destino"]
    TGT --> APP["Deployment consumidor"]
```

## Piezas principales

### `SecretStore`

Describe como conectarse a una fuente de secretos.

Puede apuntar a:

- un proveedor cloud
- otro cluster
- otro namespace del mismo cluster

### `ExternalSecret`

Declara:

- que claves quieres traer
- cada cuanto refrescarlas
- como se llamara el `Secret` final

### `Secret` resultante

La aplicacion no suele consumir el `ExternalSecret` directamente. Consume el `Secret` normal creado por el operador.

Eso hace que muchas aplicaciones no tengan que saber nada del operador.

## Cuando merece la pena usarlo

Especialmente cuando tienes:

- varios entornos
- GitOps
- rotacion de credenciales
- equipos que no quieren secretos reales dentro del repositorio

## Ejemplo del repositorio

Revisa:

- `examples/k8s/external-secrets-demo/source-namespace.yaml`
- `examples/k8s/external-secrets-demo/target-namespace.yaml`
- `examples/k8s/external-secrets-demo/source-secret.yaml`
- `examples/k8s/external-secrets-demo/serviceaccount.yaml`
- `examples/k8s/external-secrets-demo/role.yaml`
- `examples/k8s/external-secrets-demo/rolebinding.yaml`
- `examples/k8s/external-secrets-demo/secretstore.yaml`
- `examples/k8s/external-secrets-demo/externalsecret.yaml`
- `examples/k8s/external-secrets-demo/deployment.yaml`

El laboratorio usa una variante didactica:

- un `Secret` vive en `secret-source`
- el operador lo lee con RBAC minimo
- un `ExternalSecret` lo sincroniza en `external-secrets-demo`
- una app consume el secreto resultante

Esto evita depender de un proveedor cloud para comprender el flujo.

## Instalacion del operador

Antes de aplicar los CRDs del ejemplo necesitas instalar External Secrets Operator.

Una instalacion orientativa con Helm:

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm repo update
helm install external-secrets \
  external-secrets/external-secrets \
  -n external-secrets \
  --create-namespace
```

## Recorrido recomendado

### 1. Crear namespaces y secreto origen

```bash
kubectl apply -f examples/k8s/external-secrets-demo/source-namespace.yaml
kubectl apply -f examples/k8s/external-secrets-demo/target-namespace.yaml
kubectl apply -f examples/k8s/external-secrets-demo/source-secret.yaml
```

### 2. Crear identidad y permisos minimos

```bash
kubectl apply -f examples/k8s/external-secrets-demo/serviceaccount.yaml
kubectl apply -f examples/k8s/external-secrets-demo/role.yaml
kubectl apply -f examples/k8s/external-secrets-demo/rolebinding.yaml
```

Aqui esta una de las lecciones importantes:

- el operador no deberia leer cualquier secreto de cualquier namespace
- el `SecretStore` debe tener el minimo acceso necesario

### 3. Crear `SecretStore` y `ExternalSecret`

```bash
kubectl apply -f examples/k8s/external-secrets-demo/secretstore.yaml
kubectl apply -f examples/k8s/external-secrets-demo/externalsecret.yaml
```

### 4. Verificar el secreto materializado

```bash
kubectl get externalsecret -n external-secrets-demo
kubectl get secret -n external-secrets-demo database-credentials-local
kubectl describe secretstore -n external-secrets-demo k8s-source-store
```

### 5. Desplegar una app consumidora

```bash
kubectl apply -f examples/k8s/external-secrets-demo/deployment.yaml
kubectl logs -n external-secrets-demo deploy/secret-consumer
```

El contenedor no necesita conocer el operador. Solo ve variables de entorno normales.

## Que mirar en este laboratorio

- si `SecretStore` queda listo o en error
- si el `ExternalSecret` genera realmente un `Secret`
- si el `Deployment` arranca despues de que el secreto exista
- si una rotacion en el secreto origen termina sincronizandose

## Prueba de rotacion

Puedes modificar el secreto origen:

```bash
kubectl patch secret database-credentials \
  -n secret-source \
  --type merge \
  -p '{"stringData":{"password":"rotada-demo"}}'
```

Despues revisa si el `Secret` de destino cambia tras el intervalo de refresco.

## Errores frecuentes

### `kubectl apply` falla porque el recurso no existe

Eso significa normalmente que External Secrets Operator aun no esta instalado y los CRDs no existen.

### `SecretStore` no queda `Ready`

Revisa:

- RBAC
- namespace remoto
- referencia a `kube-root-ca.crt`
- que la autenticacion usada coincida con la configuracion

### El `Deployment` no arranca

Suele pasar porque:

- el `ExternalSecret` aun no ha sincronizado
- el nombre del `Secret` destino no coincide
- falta alguna clave como `username` o `password`

## Buenas practicas

- mantener el alcance del `SecretStore` lo mas pequeño posible
- separar secreto origen y secreto consumido por namespace
- documentar quien rota el valor y con que frecuencia
- no asumir que el secreto esta cifrado fuera de etcd si no lo has configurado

## Que no resuelve por si solo

External Secrets ayuda con sincronizacion y gobierno, pero no sustituye:

- cifrado en reposo de etcd
- politicas de acceso en la aplicacion
- auditoria de quien usa la credencial

## Conexiones importantes

- [ConfigMaps, Secrets y almacenamiento](05-configmaps-secrets-y-storage.md)
- [Entornos, CI/CD y GitOps](14-entornos-ci-cd-y-gitops.md)
- [Seguridad aplicada y hardening](17-seguridad-aplicada-y-hardening.md)
- [Argo CD practico: app-of-apps y sync](27-argocd-practico-app-of-apps-y-sync.md)
