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

## Nivel 3: Kubernetes intermedio

### Reto 5: romper un selector de `Service`

Usa:

- `examples/k8s/hola-nginx/`

Objetivo:

- provocar que el service deje de tener endpoints
- detectarlo con `kubectl get endpoints`
- corregir labels o selector

### Reto 6: readiness rota

Usa:

- `examples/k8s/probes-demo/deployment-bad-readiness.yaml`

Objetivo:

- explicar por qué el pod está `Running` pero no `Ready`

### Reto 7: `PVC` y persistencia

Usa:

- `examples/k8s/storage-demo/`

Objetivo:

- verificar que el contador sobrevive a la recreación del pod

## Nivel 4: temas de nivel superior

### Reto 8: mínimos permisos

Usa:

- `examples/k8s/rbac-demo/`

Objetivo:

- comprobar qué puede y qué no puede hacer la service account

### Reto 9: leer una `NetworkPolicy`

Usa:

- `examples/k8s/network-policy-demo/`

Objetivo:

- explicar qué tráfico queda permitido y cuál no

### Reto 10: analizar un `StatefulSet`

Usa:

- `examples/k8s/scaling-demo/`

Objetivo:

- describir por qué `demo-store-0` y `demo-store-1` no son pods intercambiables como los de un `Deployment`

## Nivel 5: proyecto integral

### Reto 11: comparar Compose y Kubernetes

Usa:

- `examples/docker/fullstack-demo/`
- `examples/k8s/fullstack-demo/`

Objetivo:

- explicar qué cambia entre red, configuración, exposición y observabilidad

### Reto 12: renderizar el chart fullstack

Usa:

- `examples/helm/fullstack-demo/`

Objetivo:

- renderizar `dev`, `demo` y `prod`
- comparar réplicas, host y configuración

## Cómo usar estos retos

La recomendación es resolverlos así:

1. Ejecuta el ejemplo base.
2. Introduce el cambio o el fallo.
3. Observa síntomas.
4. Usa comandos de diagnóstico.
5. Documenta qué pasó y por qué.
