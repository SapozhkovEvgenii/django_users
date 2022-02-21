from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from user.forms import LoginForm
import json


def users(request):
    context = {"users": User.objects.all()}
    return render(request, "users.html", context)

def login(request):
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print("VALID USER")
            return redirect("all_users") 
        print("INVALID USER")
        context.update(login_form=login_form)
    return render(request, "login.html", context)

def user(request):
    context = {"key": "value", "result": "True"}
    return render(request, "login.html", context)
    # return HttpResponse(json.dumps(context), content_type="application/json")

