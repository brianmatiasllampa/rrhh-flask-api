import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from extensions import db, migrate, ma
from api import bp as api_bp
import api.empleados  # asegura que las rutas se registren
import models  # asegura que los modelos estén visibles para Alembic/Flask-Migrate

load_dotenv()  # lee las variables del archivo .env


def create_app():
    app = Flask(__name__)

    # La URL de conexión ahora sale del .env, no está escrita acá
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_AS_ASCII"] = False

    # Extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # CORS (abrimos para /api/*; ajusta origins según tu front)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Blueprints
    app.register_blueprint(api_bp)

    @app.get("/")
    def inicio():
        return "API de Recursos Humanos (Flask)"

    return app


if __name__ == "__main__":
    create_app().run(debug=True, port=8080)