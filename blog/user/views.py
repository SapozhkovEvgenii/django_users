from http.client import HTTPResponse
from logging import exception
from django.shortcuts import render, redirect
from user.models import User
from user.forms import LoginForm, RegisterForm
import json
from django.views.generic import ListView, FormView
from django.contrib.auth import logout
# from django.contrib.auth.decorators import permission_required, login_required
# from django.http import HttpResponseNotFound, Http404


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
#     if request.user.is_anonymous:
#         if request.method == "POST":
#             register_form = RegisterForm(request.POST)
#             if register_form.is_valid:
#                 register_form.save()
#                 return redirect("all_users")
#             context.update(register_form=register_form)
#     # return HttpResponseNotFound('<h1>This page is not available for authorized users</h1>')
#     return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect("all_users")


