# ConfigMaps, Secrets y almacenamiento

Uno de los cambios de mentalidad más importantes al pasar a Kubernetes es separar imagen, configuración y datos persistentes.

## ConfigMaps

Sirven para configuración no sensible.

Ejemplo:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_NAME: Curso Kubernetes
  APP_MODE: demo
```

Uso como variables de entorno:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

## Secrets

Se usan para datos sensibles, aunque conviene recordar que no son cifrado mágico por defecto.

Ejemplo:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  API_TOKEN: super-demo-token
```

Uso en el pod:

```yaml
envFrom:
  - secretRef:
      name: app-secret
```

## Configuración por archivo

Tanto ConfigMaps como Secrets también pueden montarse como archivos en un volumen.

## Volúmenes en Kubernetes

Un pod puede montar distintos tipos de volúmenes. Para persistencia real suele usarse:

- `PersistentVolume` (PV)
- `PersistentVolumeClaim` (PVC)

## `emptyDir`

Es útil para datos temporales compartidos entre contenedores del mismo pod, pero se pierde al destruir el pod.

## PersistentVolumeClaim

Ejemplo simplificado:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Montarlo en un contenedor:

```yaml
volumeMounts:
  - name: app-data
    mountPath: /data
volumes:
  - name: app-data
    persistentVolumeClaim:
      claimName: app-pvc
```

## Cuándo usar cada cosa

- ConfigMap: configuración normal
- Secret: tokens, passwords, claves
- PVC: datos persistentes
- emptyDir: scratch space temporal

## Ejemplo del repositorio

Revisa `examples/k8s/configmap-secret/` para ver:

- `configmap.yaml`
- `secret.yaml`
- `deployment.yaml`
- `service.yaml`

## Errores frecuentes

- El nombre del ConfigMap o Secret no coincide.
- Se pone información sensible en ConfigMap.
- El PVC queda en `Pending` porque no hay storage class adecuada.
- Se espera persistencia usando `emptyDir`.
