from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from blog.extensions import db
from blog.models.article_tag import article_tag_association_table


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, default="", server_default="")

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')
