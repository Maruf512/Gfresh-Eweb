
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("View_Api.urls")),
    path('admin/', admin.site.urls),
]
