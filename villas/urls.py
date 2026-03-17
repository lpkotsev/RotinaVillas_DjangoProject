from django.urls import path
from .views import *


urlpatterns = [

    path("",VillaListView.as_view(),name="villa-list"),

    path("create/",VillaCreateView.as_view(),name="villa-create"),

    path("<int:pk>/",VillaDetailView.as_view(),name="villa-details"),

    path("<int:pk>/edit/",VillaEditView.as_view(),name="villa-edit"),

    path("<int:pk>/delete/",VillaDeleteView.as_view(),name="villa-delete"),

    path("my/", MyVillasView.as_view(), name="my-villas"),

]