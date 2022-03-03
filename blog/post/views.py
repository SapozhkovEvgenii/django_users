from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import ListView
from post.forms import PostForm
from post.models import Post
from django.http import Http404


class PostsView(ListView):
    paginate_by = 5
    model = Post
    template_name = "all_records.html"


def new_post(request):
    context = {"form": PostForm()}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_posts")
        context.update(form=form)
    return render(request, "new_post.html", context)

def single_post(request, pk):
    try:
        context = {
            "post": Post.objects.get(id=pk)
        }
    except Post.DoesNotExist:
        raise Http404("Post not found")
    context["post"].views += 1
    context["post"].save()
    return render(request, "single_post.html", context)



