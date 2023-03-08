import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from blog.extensions import db


class Article(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', backref='article_author', lazy='subquery')

    def __repr__(self):
        # return f"{self.title}"
        return f"{self.title} author-{self.author_id}"
