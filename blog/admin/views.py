from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from blog.models import Article, Author, Users, Tag
from blog.extensions import db, admin


class CustomAdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_bp.login'))


class TagAdminView(CustomAdminView):
    create_modal = True
    edit_modal = True
    column_searchable_list = ['name']


class UserAdminView(CustomAdminView):
    column_exclude_list = ('password', 'birthday')


class ArticleAdminView(CustomAdminView):
    column_list = (
        'title',
        'text',
        'created_at',
        'updated_at',
        'author',
        'tags'
    )
    edit_modal = True


class AuthorAdminView(CustomAdminView):
    edit_template = True
    column_list = ('users', 'article')


admin.add_view(TagAdminView(Tag, db.session, category='Models'))
admin.add_view(ArticleAdminView(Article, db.session, category='Models'))
admin.add_view(AuthorAdminView(Author, db.session, category='Models'))
admin.add_view(UserAdminView(Users, db.session, category='Models'))
