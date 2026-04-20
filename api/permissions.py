from rest_framework.permissions import BasePermission


class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.owner or
            request.user.is_superuser or
            request.user.groups.filter(name="Moderators").exists()
        )