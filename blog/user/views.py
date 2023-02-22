from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint(
    'user',
    __name__,
    url_prefix='/users',
    static_folder='../static',
    template_folder='../templates'
)

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Boby',
}


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)


@user.route('/<int:user_id>')
def user_detail(user_id: int):
    try:
        user = USERS[user_id]
    except KeyError:
        raise NotFound(f'User id {user_id} not found')
    return render_template('user/detail.html', user=user)
