from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_url = 'user_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = 'user_list'

    id = fields.Integer(as_string=True)
    username = fields.String(allow_none=False)
    email = fields.Email(allow_none=False)
    is_staff = fields.Boolean(allow_none=False)

    author = Relationship(
        nested='AuthorSchema',
        attribute='author',
        related_url='author_detail',
        related_url_kwargs={'id': '<id>'},
        schema='AuthorSchema',
        type_='author',
        many=False,
    )
    articles = Relationship(
        nested='ArticleSchema',
        attribute='articles',
        related_url='article_detail',
        related_url_kwargs={'id': '<id>'},
        schema='ArticleSchema',
        type_='article',
        many=True,
    )