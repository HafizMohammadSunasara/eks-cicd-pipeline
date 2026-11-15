"""Simple Flask demo for the GitOps-on-EKS learning project."""

import os
import socket

from flask import Flask, jsonify, render_template


def create_app():
    application = Flask(__name__)

    @application.get("/")
    def index():
        return render_template(
            "index.html",
            version=os.environ.get("APP_VERSION", "local-dev"),
            pod=socket.gethostname(),
        )

    @application.get("/healthz")
    def health():
        return jsonify(status="ok"), 200

    @application.get("/readyz")
    def ready():
        return jsonify(status="ready"), 200

    @application.get("/version")
    def version():
        return jsonify(version=os.environ.get("APP_VERSION", "local-dev")), 200

    return application


app = create_app()
