import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "dev")


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": APP_VERSION
    }), 200


@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "version": APP_VERSION
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)