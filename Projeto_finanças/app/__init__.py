from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.onboarding_routes import onboarding
    from app.routes.dashboard_routes import dashboard

    app.register_blueprint(onboarding)
    app.register_blueprint(dashboard)

    with app.app_context():
        db.create_all()

        return app