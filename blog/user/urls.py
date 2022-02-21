from unicodedata import name
from django.urls import path
from user.views import user, users, login
urlpatterns = [
    # path("", user, name="user_page"),
    path("login", login, name="user_login"),
    path("users/", users, name="all_users"),
]

