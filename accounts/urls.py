from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView
from .views import ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("profile/<int:pk>/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
]