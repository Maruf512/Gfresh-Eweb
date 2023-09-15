from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("shop", views.shop, name="Shop"),
    path("view", views.view, name="View"),
]