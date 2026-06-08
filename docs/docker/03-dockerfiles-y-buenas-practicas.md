# Dockerfiles y buenas prácticas

El `Dockerfile` define cómo se construye una imagen. Cuanto mejor esté diseñado, más rápidas, seguras y mantenibles serán tus builds.

## Instrucciones más usadas

### `FROM`

Declara la imagen base:

```dockerfile
FROM python:3.12-slim
```

### `WORKDIR`

Define el directorio de trabajo:

```dockerfile
WORKDIR /app
```

### `COPY`

Copia archivos al contexto de la imagen:

```dockerfile
COPY requirements.txt .
COPY app.py .
```

### `RUN`

Ejecuta comandos durante el build:

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### `CMD`

Define el comando por defecto al arrancar el contenedor:

```dockerfile
CMD ["python", "app.py"]
```

## Ejemplo base de API Python

Archivo relevante: `examples/docker/python-api/Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]
```

## Orden de capas y caché

Docker reutiliza capas cuando puede. Por eso conviene ordenar el `Dockerfile` así:

1. Imagen base
2. Dependencias poco cambiantes
3. Código fuente que cambia con más frecuencia

Ejemplo:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

Si copias todo el proyecto demasiado pronto, cualquier cambio invalida capas costosas.

## `.dockerignore`

Sirve para no mandar archivos innecesarios al contexto de build.

Ejemplo:

```text
__pycache__/
.git/
.venv/
*.pyc
```

## Buenas prácticas importantes

- Usa imágenes base pequeñas cuando sea razonable.
- Declara versiones explícitas cuando necesites reproducibilidad.
- Evita meter secretos en la imagen.
- Usa `CMD` en formato JSON siempre que puedas.
- Mantén una sola responsabilidad por imagen.

## Multi-stage builds

Permiten compilar en una etapa y copiar solo el resultado final a una imagen más pequeña.

Ejemplo conceptual:

```dockerfile
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

## Señales y proceso principal

El contenedor vive mientras viva el proceso principal. Si ese proceso termina, el contenedor también.

Por eso:

- No conviene arrancar servicios con hacks en background.
- Es importante usar un `CMD` o `ENTRYPOINT` que represente el proceso real.

## Diferencia entre `CMD` y `ENTRYPOINT`

- `CMD`: valores por defecto fácilmente reemplazables.
- `ENTRYPOINT`: define el ejecutable principal del contenedor.

Ejemplo:

```dockerfile
ENTRYPOINT ["python", "app.py"]
CMD ["--port", "8000"]
```

## Ejercicios sugeridos

1. Toma `examples/docker/python-api/` y cambia el puerto a `9000`.
2. Añade una variable de entorno `APP_NAME`.
3. Prueba a romper la caché modificando `requirements.txt`.
4. Añade un `.dockerignore` y compara el contexto enviado.
