from flask import Flask

from blog.article.views import article
from blog.user.views import user
from blog.auth.views import auth


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'y%&lt!6eonj#%=mdpi+!w%f*xxmfb48j(=57dqgh+hvs00_-a8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_apps(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)


def init_apps(app: Flask):
    from blog.auth.views import login_manager
    from blog.models.database import db

    login_manager.init_app(app)
    db.init_app(app)
