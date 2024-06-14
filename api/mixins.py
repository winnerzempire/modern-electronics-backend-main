from rest_framework import permissions
from .permissions import IsStaffPermissions


class StaffEditorPermissionsMixin():
  permission_class=[permissions.IsAdminUser, IsStaffPermissions]