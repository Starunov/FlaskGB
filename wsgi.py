from flask import redirect, url_for
from blog.app import create_app

app = create_app()


@app.route('/')
def index():
    return redirect(url_for('user.user_list'))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
    )
