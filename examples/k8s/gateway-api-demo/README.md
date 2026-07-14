# Gateway API Demo

Laboratorio para estudiar:

- `Gateway`
- `HTTPRoute`
- routing simple
- split de trafico entre servicios

## Archivos

- `namespace.yaml`
- `deployment-v1.yaml`
- `deployment-v2.yaml`
- `service-v1.yaml`
- `service-v2.yaml`
- `gateway.yaml`
- `httproute-simple.yaml`
- `httproute-split.yaml`

## Prerrequisitos

Necesitas:

- CRDs de Gateway API
- un controlador compatible
- un `GatewayClass` real en tu cluster

Compruebalo con:

```bash
kubectl get gatewayclass
```

## Flujo recomendado

```bash
kubectl apply -f examples/k8s/gateway-api-demo/namespace.yaml
kubectl apply -f examples/k8s/gateway-api-demo/deployment-v1.yaml
kubectl apply -f examples/k8s/gateway-api-demo/deployment-v2.yaml
kubectl apply -f examples/k8s/gateway-api-demo/service-v1.yaml
kubectl apply -f examples/k8s/gateway-api-demo/service-v2.yaml
```

Antes de aplicar `gateway.yaml`, cambia `gatewayClassName` para que coincida con una clase real.

Despues:

```bash
kubectl apply -f examples/k8s/gateway-api-demo/gateway.yaml
kubectl apply -f examples/k8s/gateway-api-demo/httproute-simple.yaml
kubectl apply -f examples/k8s/gateway-api-demo/httproute-split.yaml
```

## Comprobaciones utiles

```bash
kubectl get gateway,httproute -n gateway-demo
kubectl describe gateway -n gateway-demo app-gateway
kubectl describe httproute -n gateway-demo python-api-simple
kubectl describe httproute -n gateway-demo python-api-split
```

## Que mirar en el split

`httproute-split.yaml` envia mas trafico a `python-api-v1` que a `python-api-v2`.

Ese patron sirve para:

- canaries manuales
- migraciones graduales
- mitigacion de incidentes
