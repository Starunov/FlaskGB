from flask import Blueprint, render_template

from blog.models.author import Author

author = Blueprint(
    'author_bp',
    __name__,
    url_prefix='/authors',
    static_folder='../static',
    template_folder='../templates'
)


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template('author/list.html', authors=authors)


@author.route('/<int:author_id>')
def author_detail(author_id):
    return f'Author Detail {author_id}'
