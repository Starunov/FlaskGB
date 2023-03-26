from flask.cli import cli
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models.article import Article
from blog.models import Users


@cli.command('init-db')
def init_db():
    db.create_all()
    print('done!')


@cli.command('create-superuser')
def create_user():
    admin = Users(
        username='admin',
        password=generate_password_hash('adminadmin'),
        email='admin@admin.com',
        is_staff=True
    )

    db.session.add(admin)
    db.session.commit()
    print('done! Created users:', admin)


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


@cli.command('create-tags')
def create_tags():
    from blog.models.tag import Tag
    for name in ['flask', 'django', 'python', 'sqlalchemy', 'news']:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('created tags')


__all__ = [
    'init_db',
    'create_user',
    'create_article',
    'create_tags',
]
