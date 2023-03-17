from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_admin import Admin

from blog.admin.index_view import MyAdminIndexView

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

migrate = Migrate()

csrf = CSRFProtect()

admin = Admin(
    name='Blog Admin Panel',
    index_view=MyAdminIndexView(),
    template_mode='bootstrap4'
)
