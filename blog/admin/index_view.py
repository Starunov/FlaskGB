from flask import redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth_bp.login'))
        return super(MyAdminIndexView, self).index()
