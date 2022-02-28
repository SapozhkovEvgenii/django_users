from unicodedata import name
from django.shortcuts import redirect
from django.urls import path
from user.views import UsersView, login, RegisterView
urlpatterns = [
    path("", lambda request: redirect("all_users")),
    path("login", login, name="user_login"),
    path("users/", UsersView.as_view(), name="all_users"),
    path("register", RegisterView.as_view(), name="register_user"),
]

