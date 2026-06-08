# Observabilidad, seguridad y depuración

Una gran parte del trabajo real en Kubernetes no es crear YAML, sino entender por qué algo no está funcionando.

## Observabilidad mínima

Herramientas básicas que debes dominar:

```bash
kubectl get pods
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl describe pod <pod_name>
kubectl logs <pod_name>
kubectl logs -f <pod_name>
```

Si hay varios contenedores:

```bash
kubectl logs <pod_name> -c <container_name>
```

## Patrón de diagnóstico útil

1. Ver si el recurso existe.
2. Ver su estado.
3. Revisar eventos.
4. Revisar logs.
5. Inspeccionar configuración montada y variables.

## Estados de error frecuentes

### `ImagePullBackOff`

Posibles causas:

- imagen inexistente
- tag mal escrito
- registry inaccesible
- credenciales faltantes

### `CrashLoopBackOff`

El contenedor arranca y cae repetidamente.

Revisa:

- logs
- comando de arranque
- dependencias
- variables

### `Pending`

El pod no encuentra dónde ejecutarse.

Revisa:

- recursos insuficientes
- PVC pendiente
- nodos no compatibles
- taints y tolerations

## Probes y fiabilidad

Los probes bien configurados evitan enrutar tráfico a pods rotos y permiten recuperar procesos atascados.

Ejemplo:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 10
```

## Seguridad básica

- Usa namespaces para separar entornos.
- Minimiza permisos de service accounts.
- Evita ejecutar contenedores como root.
- Limita capacidades cuando aplique.
- Controla imágenes y registries permitidos.

## Recursos y estabilidad

Sin `requests` y `limits`, un clúster compartido puede comportarse peor y hacer más difícil el scheduling.

## Comandos de apoyo

```bash
kubectl top pods
kubectl top nodes
kubectl get all -n <namespace>
kubectl rollout status deployment/<name>
```

## Checklist de depuración

- El namespace es el correcto.
- La imagen existe y es accesible.
- El service selecciona los pods esperados.
- El contenedor escucha en el puerto correcto.
- Los probes apuntan a la ruta correcta.
- La configuración externa está disponible.

## Cierre del bloque

Si puedes diagnosticar un `CrashLoopBackOff`, corregir un selector roto en un service y explicar la diferencia entre `readiness` y `liveness`, ya tienes una base muy sólida para trabajar con Kubernetes real.

## Profundización recomendada

Para practicar estos conceptos con laboratorios más concretos, continúa con:

- [Probes, recursos y scheduling](11-probes-recursos-y-scheduling.md)
