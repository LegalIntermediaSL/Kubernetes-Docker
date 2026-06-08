# Introducción a Docker y Kubernetes

Docker y Kubernetes suelen aparecer juntos, pero no hacen exactamente lo mismo.

Docker resuelve el empaquetado y la ejecución consistente de aplicaciones. Kubernetes resuelve la operación de esas aplicaciones cuando ya tenemos varios contenedores, varios entornos y necesidad de automatizar despliegues.

## El problema que queremos resolver

Una frase clásica en desarrollo es: "en mi máquina funciona". Eso suele pasar porque:

- Faltan dependencias
- Cambian versiones de librerías
- El sistema operativo no coincide
- La configuración no está bien documentada

Los contenedores ayudan a reducir esa diferencia entre entornos porque empaquetan aplicación, dependencias y una parte controlada del entorno de ejecución.

## Máquina virtual vs contenedor

Una máquina virtual incluye un sistema operativo completo encima de un hipervisor. Un contenedor comparte el kernel del host y aísla procesos, red y sistema de archivos.

En la práctica:

- Una VM suele ser más pesada.
- Un contenedor suele arrancar más rápido.
- Un contenedor es ideal para empaquetar una aplicación concreta.

## Qué es Docker

Docker popularizó un flujo muy cómodo para trabajar con contenedores:

- Escribes un `Dockerfile`
- Construyes una imagen
- Ejecutas uno o varios contenedores
- Publicas la imagen en un registro si la quieres compartir

Conceptos básicos:

- `Imagen`: plantilla inmutable con el contenido de la aplicación.
- `Contenedor`: instancia en ejecución de una imagen.
- `Dockerfile`: receta para construir la imagen.
- `Registry`: lugar donde se almacenan imágenes, como Docker Hub.

## Qué es Kubernetes

Kubernetes es un orquestador de contenedores. Su trabajo es mantener el estado deseado del sistema.

Ejemplos de lo que hace bien:

- Mantener varias réplicas de una aplicación
- Reiniciar contenedores que fallan
- Exponer servicios dentro o fuera del clúster
- Distribuir carga
- Facilitar despliegues declarativos

Conceptos básicos:

- `Pod`: unidad mínima desplegable.
- `Deployment`: define cuántas réplicas queremos y cómo actualizarlas.
- `Service`: ofrece una dirección estable para acceder a los pods.
- `Cluster`: conjunto de nodos administrados por Kubernetes.

## Relación entre ambos

Una forma simple de verlo:

- Docker te ayuda a construir y ejecutar contenedores.
- Kubernetes te ayuda a coordinar muchos contenedores.

Se pueden aprender por separado, pero tiene mucho sentido estudiarlos en ese orden.

## Cuándo usar cada uno

Usa Docker cuando quieras:

- Crear un entorno reproducible
- Empaquetar una API, un frontend o un worker
- Simplificar el onboarding de un proyecto

Usa Kubernetes cuando quieras:

- Ejecutar servicios con alta disponibilidad
- Automatizar despliegues
- Escalar aplicaciones
- Operar varios servicios como sistema

## Objetivo del tutorial

En este repositorio vamos a recorrer un camino progresivo:

1. Comprender los conceptos.
2. Crear una imagen con Docker.
3. Ejecutar esa imagen localmente.
4. Desplegarla en Kubernetes.

## Mini ejercicio

Antes de seguir, comprueba si tienes instaladas las herramientas:

```bash
docker --version
kubectl version --client
kind version
```

Si no usas `kind`, puedes sustituirlo por:

```bash
minikube version
```
