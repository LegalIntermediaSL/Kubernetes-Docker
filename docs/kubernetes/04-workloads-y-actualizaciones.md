# Workloads y actualizaciones

Kubernetes ofrece distintos tipos de workloads según el patrón de ejecución que necesites.

## Pod

Es la unidad mínima. Suele agrupar uno o varios contenedores muy cercanos.

Ejemplo simple:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: web
      image: nginx:alpine
```

En la práctica, para aplicaciones normales se usa más `Deployment`.

## Deployment

Es el estándar para servicios stateless.

Permite:

- mantener réplicas
- actualizar versión
- hacer rollback

Comandos útiles:

```bash
kubectl get deployments
kubectl rollout status deployment/hola-nginx
kubectl rollout history deployment/hola-nginx
kubectl rollout undo deployment/hola-nginx
```

## StatefulSet

Útil para workloads con identidad estable y almacenamiento persistente por réplica.

Casos típicos:

- bases de datos
- brokers
- sistemas distribuidos con nodos nombrados

## DaemonSet

Asegura una réplica por nodo. Muy usado para:

- agentes de logging
- métricas
- networking

## Job

Ejecuta una tarea hasta completarla.

Ejemplo:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: saludo-job
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: saludo
          image: busybox
          command: ["sh", "-c", "echo Hola desde un Job"]
```

## CronJob

Programa tareas recurrentes.

Ejemplo conceptual:

```yaml
schedule: "*/5 * * * *"
```

## Estrategias de actualización

En `Deployment`, la más común es `RollingUpdate`. Permite cambiar de versión sin cortar todo el servicio a la vez.

Campos útiles:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

## Probes

Importan mucho en producción.

### `readinessProbe`

Indica cuándo el pod está listo para recibir tráfico.

### `livenessProbe`

Indica cuándo el contenedor debe reiniciarse.

### `startupProbe`

Protege aplicaciones que tardan en arrancar.

## Recursos

Define `requests` y `limits` cuando el entorno lo requiera:

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "256Mi"
```

## Ejercicio sugerido

1. Cambia la imagen del deployment `hola-nginx`.
2. Observa el rollout.
3. Añade `readinessProbe`.
4. Provoca un error y revisa el estado con `describe`.
