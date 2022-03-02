from django.urls import path
from post.views import PostsView


urlpatterns = [
    path('all/', PostsView.as_view, name="all_posts"),
]

