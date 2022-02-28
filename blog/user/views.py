from audioop import reverse
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from user.forms import LoginForm, RegisterForm
import json
from django.views.generic import ListView, FormView


class UsersView(ListView):
    paginate_by = 2
    model = User
    template_name = "users.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/user/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



def login(request):
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.auth(request)
            return redirect("all_users") 
        context.update(login_form=login_form)
    return render(request, "login.html", context)

# def register(request):
#     context = {"register_form": RegisterForm}
#     if request.method == "POST":
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid:
#             register_form.save()
#             return redirect("all_users")
#         context.update(register_form=register_form)
#     return render(request, "register.html", context)

def user(request):
    context = {"key": "value", "result": "True"}
    return render(request, "login.html", context)
    # return HttpResponse(json.dumps(context), content_type="application/json")

