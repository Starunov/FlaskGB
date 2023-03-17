from flask import redirect, url_for, render_template
from blog.app import create_app

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('user_bp.user_list'))


@app.route('/admin')
def admin():
    return render_template('admin/index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )
