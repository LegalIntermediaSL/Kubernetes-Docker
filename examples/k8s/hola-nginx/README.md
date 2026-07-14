# Hola Nginx en Kubernetes

Versión en Kubernetes del ejemplo `hola-nginx` de Docker.

## Requisitos

- `kubectl`
- `kind` o `minikube`
- imagen `hola-nginx:local` construida

## Preparación

```bash
docker build -t hola-nginx:local examples/docker/hola-nginx
kind load docker-image hola-nginx:local --name curso-k8s
```

Si usas `minikube`, carga la imagen con el comando equivalente.

## Namespace

Este laboratorio crea y usa el namespace `hola-nginx-demo`.

## Despliegue

```bash
kubectl apply -f examples/k8s/hola-nginx/
```

## Verificación

```bash
kubectl get deployment hola-nginx -n hola-nginx-demo
kubectl get pods -n hola-nginx-demo -l app=hola-nginx
kubectl get service hola-nginx -n hola-nginx-demo
kubectl port-forward -n hola-nginx-demo service/hola-nginx 8080:80
```

En otra terminal:

```bash
curl -s http://localhost:8080
```

## Qué practicar

- Relación entre `Deployment`, `Pod` y `Service`.
- Carga de imágenes locales en un cluster local.
- Verificación básica con `kubectl get` y `port-forward`.

## Limpieza

```bash
kubectl delete -f examples/k8s/hola-nginx/
```
