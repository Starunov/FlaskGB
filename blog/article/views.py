from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint(
    'article',
    __name__,
    url_prefix='/articles',
    static_folder='../static',
    template_folder='../templates',
)

ARTICLES = {
    1: 'article 1',
    2: 'article 2',
    3: 'article 3',
    4: 'article 4',
}


@article.route('/')
def article_list():
    return render_template('article/list.html', articles=ARTICLES)


@article.route('/<int:article_id>')
def article_detail(article_id: int):
    try:
        article = ARTICLES[article_id]
    except KeyError:
        raise NotFound(f'Article id {article_id} not found')
    return render_template('article/detail.html', article=article)
