from django.shortcuts import render
from django.views.generic import ListView
from post.models import Post


class PostsView(ListView):
    paginate_by = 5
    model = Post
    template_name = "all_records.html"


def new_post(request):
    ...
