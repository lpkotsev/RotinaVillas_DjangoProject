from django.urls import path
from .views import create_review


urlpatterns = [

    path(
        "create/<int:pk>/",
        create_review,
        name="review-create"
    ),

]