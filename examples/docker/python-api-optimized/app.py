from flask import Flask, Response, jsonify
import os
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest


app = Flask(__name__)
REQUEST_COUNTER = Counter(
    "python_api_requests_total",
    "Numero total de peticiones atendidas por la API de ejemplo",
    ["endpoint"],
)


@app.get("/")
def index():
    REQUEST_COUNTER.labels(endpoint="/").inc()
    return jsonify(
        {
            "message": "Hola desde la API optimizada de ejemplo",
            "app_name": os.getenv("APP_NAME", "curso-docker-k8s"),
            "environment": os.getenv("APP_ENV", "optimized"),
        }
    )


@app.get("/health")
def health():
    REQUEST_COUNTER.labels(endpoint="/health").inc()
    return jsonify({"status": "ok"})


@app.get("/metrics")
def metrics():
    REQUEST_COUNTER.labels(endpoint="/metrics").inc()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
