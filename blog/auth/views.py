from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import login_manager
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models import User
from blog.extensions import db

auth = Blueprint(
    'auth_bp',
    __name__,
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth_bp.login'))


@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user_bp.user_list'))

    form = UserLoginForm(request.form)
    errors = []

    if request.method == 'GET':
        return render_template('user/login.html', form=form)

    if not form.validate_on_submit():
        return render_template('user/login.html', form=form, errors=errors)

    _user = User.query.filter_by(email=form.email.data).one_or_none()
    if not _user or not check_password_hash(_user.password, form.password.data):
        flash('Check your login details', 'alert alert-danger')
        return redirect(url_for('auth_bp.login'))

    login_user(_user)
    return redirect(url_for('user_bp.user_list'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_bp.user_list'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user_bp.user_list", user_id=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append('username not uniq')
            return render_template('user/register.html', form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not uniq')
            return render_template('user/register.html', form=form)

        _user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)
        return redirect(url_for('user_bp.user_list'))

    return render_template('user/register.html', form=form, errors=errors)
