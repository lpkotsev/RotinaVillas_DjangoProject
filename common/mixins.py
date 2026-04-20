from django.contrib.auth.mixins import UserPassesTestMixin

class IsOwnerOrModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user

        is_owner = (
            hasattr(obj, "owner") and obj.owner == user
        ) or (
            hasattr(obj, "user") and obj.user == user
        )

        is_moderator = user.groups.filter(name="Moderators").exists()

        return user.is_superuser or is_moderator or is_owner