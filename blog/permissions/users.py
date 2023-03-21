from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForGet,
    PermissionForPatch
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models.user import User


class UserPermissions(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        'id',
        'username',
        'email',
        'is_staff',
    ]

    PATCH_AVAILABLE_FIELDS = [
        'username',
    ]

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        if not current_user.is_authenticated or not current_user.is_staff:
            raise AccessDenied('no access')

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data=None, obj=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=User)
        return {
            k: v
            for k, v in data.items()
            if k in permission_for_patch.columns
        }
