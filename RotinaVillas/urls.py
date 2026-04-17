from django.contrib import admin
from django.urls import path,include


urlpatterns = [

    path("admin/",admin.site.urls),

    path("",include("common.urls")),
    path("villas/",include("villas.urls")),
    path("bookings/",include("bookings.urls")),
    path("reviews/",include("reviews.urls")),
    path("api/", include("api.urls")),
    path("accounts/", include("accounts.urls")),

]

handler404 = "common.views.custom_404"