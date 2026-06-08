# Arquitectura del clúster

Kubernetes es un sistema distribuido. Entender su arquitectura ayuda a leer errores con menos frustración.

## Componentes del plano de control

```mermaid
flowchart TB
    U["kubectl o cliente"] --> API["kube-apiserver"]
    API --> ETCD["etcd"]
    API --> SCHED["kube-scheduler"]
    API --> CTRL["kube-controller-manager"]
    SCHED --> N1["Nodo worker 1"]
    SCHED --> N2["Nodo worker 2"]
    N1 --> K1["kubelet"]
    N1 --> R1["container runtime"]
    N1 --> P1["Pods"]
    N2 --> K2["kubelet"]
    N2 --> R2["container runtime"]
    N2 --> P2["Pods"]
```

### `kube-apiserver`

Es la puerta de entrada. `kubectl` y otros componentes hablan con esta API.

### `etcd`

Base de datos clave-valor donde Kubernetes guarda el estado del clúster.

### `kube-scheduler`

Decide en qué nodo debería ejecutarse cada pod.

### `kube-controller-manager`

Ejecuta controladores que comparan estado real y deseado.

## Componentes de los nodos

### `kubelet`

Agente del nodo que recibe instrucciones y gestiona pods.

### `container runtime`

Es quien realmente ejecuta los contenedores.

### `kube-proxy`

Participa en la conectividad de red de los services.

## Nodo, pod y clúster

- `cluster`: el conjunto completo
- `node`: una máquina de trabajo
- `pod`: la unidad mínima desplegable

## El bucle de reconciliación

Kubernetes funciona comparando:

- estado deseado, definido en YAML
- estado real, observado en el clúster

Cuando difieren, los controladores actúan.

## Bucle de reconciliacion

```mermaid
flowchart LR
    D["Estado deseado en YAML"] --> API["API Server"]
    API --> C["Controladores"]
    C --> O["Acciones sobre el cluster"]
    O --> R["Estado real"]
    R --> C
```

## Namespaces

Sirven para agrupar y aislar recursos lógicamente:

```bash
kubectl get namespaces
kubectl create namespace curso
```

Aplicar un recurso en un namespace:

```bash
kubectl apply -n curso -f deployment.yaml
```

## Etiquetas y selectores

Son esenciales para que los objetos se encuentren entre sí.

Ejemplo:

```yaml
labels:
  app: hola-nginx
  tier: web
```

Selector:

```yaml
selector:
  app: hola-nginx
```

## Flujo mental del scheduler

Cuando un pod no arranca, piensa:

1. La definición YAML es válida.
2. El scheduler encuentra nodo compatible.
3. La imagen puede descargarse.
4. El contenedor arranca.
5. Los probes pasan.

```mermaid
flowchart LR
    A["Pod Pending"] --> B{"YAML valido?"}
    B -- "No" --> C["Corregir manifiesto"]
    B -- "Si" --> D{"Hay nodo compatible?"}
    D -- "No" --> E["Revisar recursos, taints o selectors"]
    D -- "Si" --> F{"La imagen descarga?"}
    F -- "No" --> G["Revisar tag, registry y credenciales"]
    F -- "Si" --> H{"El proceso arranca?"}
    H -- "No" --> I["Revisar logs y command"]
    H -- "Si" --> J{"Pasan los probes?"}
    J -- "No" --> K["Revisar health checks"]
    J -- "Si" --> L["Pod listo"]
```

## Comandos útiles

```bash
kubectl cluster-info
kubectl get nodes
kubectl get namespaces
kubectl get events --sort-by=.metadata.creationTimestamp
```

## Qué mirar cuando algo falla

- Eventos del namespace
- `describe pod`
- imágenes y `imagePullPolicy`
- recursos solicitados
- tolerations y node selectors si existen
