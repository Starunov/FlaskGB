from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import login_manager
from blog.models import User
from blog.extensions import db

auth = Blueprint(
    'auth',
    __name__,
)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.user_list'))

    if request.method == 'GET':
        return render_template('auth/login.html')
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).one_or_none()
    if not user or not check_password_hash(user.password, password):
        flash('Check your login details', 'alert alert-danger')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.user_detail', user_id=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.user_list'))


@auth.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.user_list'))

    if request.method == 'GET':
        return render_template('auth/register.html')

    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    for key, val in locals().items():
        if key == 'password2':
            continue
        if not val:
            if key == 'password1':
                key = 'password'
            flash(f"{key.capitalize()} field not be empty")
            return render_template('auth/register.html', username=username, email=email)

    user = User.query.filter_by(username=username).one_or_none()
    if user:
        flash("Username exists")
        return render_template('auth/register.html', email=email)

    user = User.query.filter_by(email=email).one_or_none()
    if user:
        flash("Email exists")
        return render_template('auth/register.html', username=username)

    if password1 != password2:
        flash("Passwords don't match")
        return render_template('auth/register.html', username=username, email=email)

    user = User(
        username=username,
        password=generate_password_hash(password1),
        email=email
    )
    db.session.add(user)
    db.session.commit()

    flash('Congratulations, you are now a registered user!', 'alert alert-success')
    return redirect(url_for('.login'))
