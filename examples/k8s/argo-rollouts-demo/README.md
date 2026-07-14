# Argo Rollouts Demo

Laboratorio para practicar progressive delivery con:

- `blue-green`
- `canary`
- servicios activo y preview
- pasos `setWeight` y `pause`

## Archivos

- `namespace.yaml`
- `bluegreen-active-service.yaml`
- `bluegreen-preview-service.yaml`
- `rollout-bluegreen.yaml`
- `canary-service.yaml`
- `rollout-canary.yaml`

## Prerrequisitos

Necesitas tener instalado el controlador de Argo Rollouts.

La guia rapida oficial usa:

```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
```

## Ruta 1: blue-green

```bash
kubectl apply -f examples/k8s/argo-rollouts-demo/namespace.yaml
kubectl apply -f examples/k8s/argo-rollouts-demo/bluegreen-active-service.yaml
kubectl apply -f examples/k8s/argo-rollouts-demo/bluegreen-preview-service.yaml
kubectl apply -f examples/k8s/argo-rollouts-demo/rollout-bluegreen.yaml
```

Para lanzar una nueva revision:

```bash
kubectl patch rollout rollouts-bluegreen-demo \
  -n rollouts-demo \
  --type=json \
  -p='[{"op":"replace","path":"/spec/template/spec/containers/0/image","value":"argoproj/rollouts-demo:yellow"}]'
```

## Ruta 2: canary

```bash
kubectl apply -f examples/k8s/argo-rollouts-demo/canary-service.yaml
kubectl apply -f examples/k8s/argo-rollouts-demo/rollout-canary.yaml
```

Para lanzar una nueva revision:

```bash
kubectl patch rollout rollouts-canary-demo \
  -n rollouts-demo \
  --type=json \
  -p='[{"op":"replace","path":"/spec/template/spec/containers/0/image","value":"argoproj/rollouts-demo:yellow"}]'
```

## Comprobaciones utiles

```bash
kubectl get rollout,rs,pods,svc -n rollouts-demo
kubectl describe rollout -n rollouts-demo rollouts-bluegreen-demo
kubectl describe rollout -n rollouts-demo rollouts-canary-demo
```

Si tienes el plugin:

```bash
kubectl argo rollouts get rollout rollouts-bluegreen-demo -n rollouts-demo --watch
kubectl argo rollouts get rollout rollouts-canary-demo -n rollouts-demo --watch
```
