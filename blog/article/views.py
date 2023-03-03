from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from blog.models import Article

article = Blueprint(
    'article',
    __name__,
    url_prefix='/articles',
    static_folder='../static',
    template_folder='../templates',
)


@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template('article/list.html', articles=articles)


@article.route('/<int:article_id>')
@login_required
def article_detail(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if not article:
        raise NotFound(f'Article id {article_id} not found')
    return render_template('article/detail.html', article=article)
