from sqlalchemy import or_

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Users, Tag
from blog.models.author import Author

article = Blueprint(
    'article_bp',
    __name__,
    url_prefix='/articles',
    static_folder='../static',
    template_folder='../templates',
)


@article.route('/')
def article_list():
    tag = request.args.get('tag')
    user_id = request.args.get('user_id')
    author_id = Author.query.filter_by(user_id=user_id).one_or_none()
    if tag:
        articles = Tag.query.filter_by(name=tag).one().articles
    elif author_id and int(author_id) == current_user.id:
        articles = Article.query.filter_by(author_id=author_id)
    else:
        articles = Article.query.all()
    return render_template('article/list.html', articles=articles)


@article.route('/api')
@login_required
def article_list_api():
    import requests
    import pprint
    articles_count = requests.get('http://127.0.0.1:5000/api/articles/event_get_count/').json().get('count')
    articles = requests.get('http://127.0.0.1:5000/api/articles').json().get('data')
    pprint.pprint(articles)
    contex = {
        'articles_count': articles_count,
        'articles': articles,
    }
    return render_template('api/list_articles.html', **contex)


@article.route('/<int:article_id>')
@login_required
def article_detail(article_id: int):
    _article = Article.query.filter_by(id=article_id).options(
        joinedload(Article.tags)
    ).one_or_none()
    if not _article:
        raise NotFound(f'Article id {article_id} not found')
    return render_template('article/detail.html', article=_article)


@article.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateArticleForm()
    errors = []

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if request.method == 'POST' and form.validate_on_submit():
        author = Author.query.filter_by(user_id=current_user.id).one_or_none()
        if author is None:
            author = Author(
                user_id=current_user.id
            )
            db.session.add(author)
            db.session.commit()

        _article = Article.query.filter_by(title=form.title.data).one_or_none()
        if _article is None:
            _article = Article(
                title=form.title.data,
                text=form.text.data,
                author_id=author.id,
            )

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return render_template('article/detail.html', article=_article)

    return render_template('article/create.html', form=form)
