from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.database import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@app.cli.command('create-user')
def create_user():
    from blog.models import User
    admin = User(
        username='admin',
        password=generate_password_hash('admin'),
        email='admin@admin.com',
        is_staff=True
    )
    james = User(
        username='james',
        password=generate_password_hash('jamesjames'),
        email='james@james.com'
    )

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()
    print('done! Created users:', admin, james)


@app.cli.command('create-article')
def create_article():
    from blog.models.article import Article

    article1 = Article(
        title='Статья 1',
        text='текст статьи номер 1',
        author_id=1,
    )
    article2 = Article(
        title='Статья 2',
        text='текст статьи номер 2',
        author_id=1,
    )
    article3 = Article(
        title='Статья 3',
        text='текст статьи номер 3',
        author_id=2,
    )
    db.session.add(article1)
    db.session.add(article2)
    db.session.add(article3)
    db.session.commit()
    print('done! Created articles:', article1, article2, article3)


if __name__ == '__main__':
    app.run()
