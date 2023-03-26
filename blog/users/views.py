from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Users

user = Blueprint(
    'user_bp',
    __name__,
    url_prefix='/users',
    static_folder='../static',
    template_folder='../templates'
)


@user.route('/')
def user_list():
    users = Users.query.all()
    return render_template('user/list.html', users=users)


@user.route('/<int:user_id>')
@login_required
def user_detail(user_id: int):
    user = Users.query.filter_by(id=user_id).one_or_none()
    if not user:
        raise NotFound(f"Users #{user_id} not found")
    return render_template('user/detail.html', user=user)
