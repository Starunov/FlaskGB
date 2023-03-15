import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from blog.extensions import db
from blog.models.article_tag import article_tag_association_table


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship('Author', backref='article_author', lazy='subquery')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __repr__(self):
        return f"{self.title}"
