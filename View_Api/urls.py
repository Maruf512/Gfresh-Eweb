from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("shop", views.shop, name="Shop"),
    path("view", views.view, name="View"),
    path("wishlist", views.wishlist, name="Wishlist"),
    path("login", views.login, name="Login"),
    path("register", views.register, name="Register"),
    path("account", views.account, name="Account"),
    path("profile-info", views.profile_info, name="Profile-Info"),
    path("manage-address", views.manage_address, name="Manage-Address"),
    path("change-password", views.change_password, name="Change-Password"),
]