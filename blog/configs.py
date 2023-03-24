import os

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)))


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'y%&lt!6eonj#%=mdpi+!w%f*xxmfb48j(=57dqgh+hvs00_-a8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True

    FLASK_ADMIN_SWATCH = 'lumen'

    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.22.0'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")


__all__ = [
    'BaseConfig',
    'DevConfig',
    'ProductionConfig',
]
