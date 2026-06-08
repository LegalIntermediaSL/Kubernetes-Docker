from flask import Flask, jsonify, request
import os
import redis


app = Flask(__name__)


def get_redis_client():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        password=os.getenv("REDIS_PASSWORD", ""),
        decode_responses=True,
        socket_connect_timeout=1,
        socket_timeout=1,
    )


def get_counter_key():
    return os.getenv("REDIS_KEY", "fullstack:visits")


def ping_redis():
    client = get_redis_client()
    client.ping()
    return client


@app.get("/api")
def index():
    return jsonify(
        {
            "message": "API fullstack del curso Docker y Kubernetes",
            "app_name": os.getenv("APP_NAME", "fullstack-demo"),
            "environment": os.getenv("APP_ENV", "development"),
            "redis_host": os.getenv("REDIS_HOST", "redis"),
            "redis_key": get_counter_key(),
        }
    )


@app.get("/api/health")
def health():
    try:
        ping_redis()
        redis_status = "ok"
    except Exception as exc:
        redis_status = f"error: {exc.__class__.__name__}"

    return jsonify(
        {
            "status": "ok",
            "redis": redis_status,
        }
    )


@app.get("/api/stats")
def stats():
    try:
        client = ping_redis()
        visits = int(client.get(get_counter_key()) or "0")
        return jsonify({"visits": visits})
    except Exception as exc:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "No se pudo leer Redis",
                    "error": exc.__class__.__name__,
                }
            ),
            503,
        )


@app.post("/api/visits")
def visits():
    try:
        client = ping_redis()
        visits = client.incr(get_counter_key())
        return jsonify({"visits": visits})
    except Exception as exc:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "No se pudo incrementar el contador",
                    "error": exc.__class__.__name__,
                }
            ),
            503,
        )


@app.post("/api/reset")
def reset():
    secret = os.getenv("RESET_TOKEN", "reset-demo")
    token = request.headers.get("X-Reset-Token", "")
    if token != secret:
        return jsonify({"status": "forbidden"}), 403

    try:
        client = ping_redis()
        client.set(get_counter_key(), "0")
        return jsonify({"status": "ok", "visits": 0})
    except Exception as exc:
        return jsonify({"status": "error", "error": exc.__class__.__name__}), 503


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
