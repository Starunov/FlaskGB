from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, User
from blog.models.author import Author

article = Blueprint(
    'article',
    __name__,
    url_prefix='/articles',
    static_folder='../static',
    template_folder='../templates',
)


@article.route('/')
def article_list():
    author_id = request.args.get('author_id')
    if author_id and int(author_id) == current_user.id:
        articles = Article.query.filter_by(author_id=author_id)
    else:
        articles = Article.query.all()
    return render_template('article/list.html', articles=articles)


@article.route('/<int:article_id>')
@login_required
def article_detail(article_id: int):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if not article:
        raise NotFound(f'Article id {article_id} not found')
    return render_template('article/detail.html', article=article)


@article.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = CreateArticleForm()
    errors = []

    if request.method == 'POST' and form.validate_on_submit():
        author = Author.query.filter_by(id=current_user.id).one_or_none()
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
                author_id=current_user.id,
            )
            db.session.add(_article)
            db.session.commit()

        return render_template('article/detail.html', article=_article)

    return render_template('article/create.html', form=form)
