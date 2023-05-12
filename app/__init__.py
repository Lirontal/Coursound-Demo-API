from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from config import Config  # Import Config from the config module

db = SQLAlchemy()
redis_client = FlaskRedis()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    redis_client.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
