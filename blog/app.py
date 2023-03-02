import os

from flask import Flask

# Extensions
from blog.extensions import db
from blog.extensions import login_manager
from blog.extensions import migrate

# Blueprints
from blog.article.views import article
from blog.user.views import user
from blog.auth.views import auth

# Commands
from blog.commands import *


cfg_name = os.environ.get("CONFIG_NAME") or "BaseConfig"


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"blog.configs.{cfg_name}")

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)


def register_extensions(app: Flask):
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)


def register_commands(app: Flask):
    app.cli.add_command(init_db)
    app.cli.add_command(create_user)
    app.cli.add_command(create_article)
