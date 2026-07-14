# Ingress Demo

Ejemplo mínimo para entender cómo un `Ingress` enruta tráfico HTTP hacia un `Service`.

## Recursos incluidos

- `namespace.yaml`
- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`

## Despliegue

```bash
kubectl apply -f examples/k8s/ingress-demo/
```

## Verificación básica

```bash
kubectl get deployment ingress-demo -n ingress-demo
kubectl get service ingress-demo -n ingress-demo
kubectl get ingress ingress-demo -n ingress-demo
```

## Prueba local sin controlador Ingress

Si tu cluster todavía no tiene controlador `Ingress`, puedes validar la aplicación por `Service`:

```bash
kubectl port-forward -n ingress-demo service/ingress-demo 8082:80
curl -s http://localhost:8082
```

## Prueba con controlador Ingress

Si tu laboratorio ya tiene controlador y resolución local configurada para `demo.local`, la ruta esperada es:

- `http://demo.local`

## Qué practicar

- Diferencia entre `Service` e `Ingress`.
- Regla `host + path`.
- Validación progresiva: primero el `Service`, luego el `Ingress`.

## Limpieza

```bash
kubectl delete -f examples/k8s/ingress-demo/
```
