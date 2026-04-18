from django.contrib.auth.mixins import UserPassesTestMixin

class IsObjectOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()

        if hasattr(obj, "owner"):
            return obj.owner == self.request.user

        if hasattr(obj, "user"):
            return obj.user == self.request.user

        return False