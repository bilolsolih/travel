from rest_framework.permissions import BasePermission


class IsNotVerified(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.is_verified
