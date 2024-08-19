"""
ce fichier permet d initialiser toutes les dependances ou libreries que nous allons utiliser

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db= SQLAlchemy()

def crate_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Définir la clé secrète ici
    app.secret_key = 'Doriane12'  # Remplacez par une clé unique

    db.init_app(app)

    with app.app_context():
        #importer et enregister les bleuprints
        from . import routes
        app.register_blueprint(routes.bp)

        #creer les tables si elles n existent pas
        db.create_all()

    return app