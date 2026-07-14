# Retos prácticos

Este documento reúne ejercicios guiados para reforzar la parte práctica del curso. Están pensados para que no solo sigas pasos, sino que tomes decisiones y aprendas a depurar.

## Nivel 1: fundamentos

### Reto 1: cambiar una página estática

Usa:

- `examples/docker/hola-nginx/`

Objetivo:

- modificar `index.html`
- reconstruir la imagen
- comprobar el cambio en el navegador

### Reto 2: cambiar el puerto de la API

Usa:

- `examples/docker/python-api/`

Objetivo:

- modificar `PORT`
- volver a ejecutar la app
- comprobar que el endpoint `/health` sigue funcionando

## Nivel 2: multi-servicio

### Reto 3: alterar la red del Compose

Usa:

- `examples/docker/fullstack-demo/`

Objetivo:

- romper la referencia entre `web` y `api`
- observar el fallo
- corregir el proxy

### Reto 4: reiniciar el contador

Objetivo:

- usar el endpoint `/api/reset`
- comprobar que la autenticación por header funciona

### Reto 5: comparar imagen base y optimizada

Usa:

- `examples/docker/python-api/`
- `examples/docker/python-api-optimized/`

Objetivo:

- construir ambas imágenes
- comparar `docker history`
- explicar qué gana el enfoque multi-stage y qué coste de complejidad introduce

### Reto 6: depurar una parada limpia

Usa:

- `examples/docker/runtime-debug-demo/`

Objetivo:

- lanzar el contenedor con una variable de entorno visible
- seguir sus logs
- detenerlo con `docker stop`
- explicar qué señal recibió y qué implicación tiene para PID 1

## Nivel 3: Docker avanzado y operación local

### Reto 7: backup simple de un volumen Docker

Usa:

- `examples/docker/volume-backup-demo/`

Objetivo:

- generar datos en el volumen
- crear un `.tgz`
- restaurarlo en otro volumen
- explicar por qué `down -v` cambia por completo el riesgo operativo

## Nivel 4: Kubernetes intermedio

### Reto 8: romper un selector de `Service`

Usa:

- `examples/k8s/hola-nginx/`

Objetivo:

- provocar que el service deje de tener endpoints
- detectarlo con `kubectl get endpoints`
- corregir labels o selector

### Reto 9: readiness rota

Usa:

- `examples/k8s/probes-demo/deployment-bad-readiness.yaml`

Objetivo:

- explicar por qué el pod está `Running` pero no `Ready`

### Reto 10: `PVC` y persistencia

Usa:

- `examples/k8s/storage-demo/`

Objetivo:

- verificar que el contador sobrevive a la recreación del pod

## Nivel 5: temas de nivel superior

### Reto 11: mínimos permisos

Usa:

- `examples/k8s/rbac-demo/`

Objetivo:

- comprobar qué puede y qué no puede hacer la service account

### Reto 12: leer una `NetworkPolicy`

Usa:

- `examples/k8s/network-policy-demo/`

Objetivo:

- explicar qué tráfico queda permitido y cuál no

### Reto 13: analizar un `StatefulSet`

Usa:

- `examples/k8s/scaling-demo/`

Objetivo:

- describir por qué `demo-store-0` y `demo-store-1` no son pods intercambiables como los de un `Deployment`

### Reto 14: seguir un `ExternalSecret`

Usa:

- `examples/k8s/external-secrets-demo/`

Objetivo:

- describir el flujo `SecretStore -> ExternalSecret -> Secret`
- identificar qué pieza requiere RBAC minimo
- explicar por qué la app consumidora no necesita saber nada del operador

### Reto 15: elegir entre HPA y KEDA

Usa:

- `examples/k8s/scaling-demo/`
- `examples/k8s/keda-demo/`

Objetivo:

- comparar el caso de CPU/memoria con el de `cron` o Prometheus
- justificar cuándo introducirías KEDA y cuándo no

## Nivel 6: proyecto integral

### Reto 16: comparar Compose y Kubernetes

Usa:

- `examples/docker/fullstack-demo/`
- `examples/k8s/fullstack-demo/`

Objetivo:

- explicar qué cambia entre red, configuración, exposición y observabilidad

### Reto 17: renderizar el chart fullstack

Usa:

- `examples/helm/fullstack-demo/`

Objetivo:

- renderizar `dev`, `demo` y `prod`
- comparar réplicas, host y configuración

## Nivel 7: plataforma y supply chain

### Reto 18: leer cuotas y defaults de namespace

Usa:

- `examples/k8s/scheduling-policy-demo/`

Objetivo:

- explicar la diferencia entre `LimitRange` y `ResourceQuota`
- identificar que pieza mete defaults y cual rechaza exceso agregado
- justificar por que el ejemplo usa `preferred` y `ScheduleAnyway` en vez de reglas duras

### Reto 19: disenar una promocion minima con evidencia

Usa:

- `examples/docker/python-api/`
- [Supply chain, Trivy, SBOM y firma](kubernetes/33-supply-chain-trivy-sbom-y-firma.md)

Objetivo:

- proponer un flujo simple `build -> scan -> SBOM -> sign -> verify`
- distinguir que haria CI y que verificaria una politica de plataforma
- explicar por que una firma no sustituye ni al escaneo ni al control de secretos

### Reto 20: decidir entre `Ingress` y `Gateway API`

Usa:

- `examples/k8s/ingress-demo/`
- `examples/k8s/gateway-api-demo/`

Objetivo:

- explicar que separa `Gateway`, `GatewayClass` y `HTTPRoute`
- identificar cuando un `Ingress` sencillo sigue siendo suficiente
- justificar cuando el split por pesos aporta valor real

### Reto 21: describir un rollout con menor blast radius

Usa:

- `examples/k8s/argo-rollouts-demo/`
- [Progressive delivery con Argo Rollouts](kubernetes/35-progressive-delivery-con-argo-rollouts.md)

Objetivo:

- comparar `RollingUpdate`, `blue-green` y `canary`
- explicar por que el canary basico reparte por replicas y no por trafico exacto
- justificar que observabilidad minima pedirias antes de automatizar promotion o rollback

### Reto 22: elegir estrategia de secretos para GitOps

Usa:

- `examples/k8s/sops-demo/`
- `examples/k8s/sealed-secrets-demo/`
- `examples/k8s/external-secrets-demo/`

Objetivo:

- explicar la diferencia entre ciphertext en Git, secreto sellado para cluster y referencia a fuente externa
- justificar cuando escogerias `SOPS`, `Sealed Secrets` o `External Secrets`
- identificar por que Argo CD recomienda poblar secretos en el cluster destino

## Cómo usar estos retos

La recomendación es resolverlos así:

1. Ejecuta el ejemplo base.
2. Introduce el cambio o el fallo.
3. Observa síntomas.
4. Usa comandos de diagnóstico.
5. Documenta qué pasó y por qué.
