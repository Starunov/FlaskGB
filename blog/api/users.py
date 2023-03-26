from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import Users
from blog.permissions.users import UserPermissions
from blog.schemas import UserSchema


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': Users,
        'permission_get': [UserPermissions],
    }
