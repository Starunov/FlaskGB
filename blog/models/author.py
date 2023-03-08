from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.extensions import db


class Author(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', backref='author_user', lazy='subquery')
    article = relationship('Article', backref='author_articles', lazy='subquery')

    def __repr__(self):
        return f"{self.user.username}"
