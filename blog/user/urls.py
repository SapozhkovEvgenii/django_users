from django.urls import path
from user.views import user

urlpatterns = [
    path("", user, name="user_page"),

]

