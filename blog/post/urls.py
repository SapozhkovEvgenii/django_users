from django.urls import path
from post.views import PostsView, new_post
from django.shortcuts import redirect

urlpatterns = [
    path('all/', PostsView.as_view(), name="all_posts"),
    path('new/', new_post, name="new_post"),
    # path('<int:pk/>', single_post, name="single_post"),
]

