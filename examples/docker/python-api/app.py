from flask import Flask, jsonify
import os


app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "message": "Hola desde la API de ejemplo",
            "app_name": os.getenv("APP_NAME", "curso-docker-k8s"),
            "environment": os.getenv("APP_ENV", "development"),
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
