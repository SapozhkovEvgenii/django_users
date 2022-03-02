from django.shortcuts import render
from django.views.generic import ListView
from post.forms import PostForm
from post.models import Post


class PostsView(ListView):
    paginate_by = 5
    model = Post
    template_name = "all_records.html"


def new_post(request):
    context = {"form": PostForm()}
