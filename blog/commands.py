from flask.cli import cli
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models.article import Article
from blog.models import User


@cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@cli.command('create-user')
def create_user():
    admin = User(
        username='admin',
        password=generate_password_hash('admin'),
        email='admin@admin.com',
        is_staff=True
    )

    db.session.add(admin)
    db.session.commit()
    print('done! Created user:', admin)


@cli.command('create-article')
def create_article():
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

    db.session.add(article1)
    db.session.add(article2)
    db.session.commit()
    print('done! Created articles:', article1, article2)


__all__ = [
    'init_db',
    'create_user',
    'create_article',
]
