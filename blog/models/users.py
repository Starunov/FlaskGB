from flask_login import UserMixin
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from blog.extensions import db


class Users(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    birthday = Column(DateTime, nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.username
