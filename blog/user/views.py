from django.shortcuts import render, HttpResponse


def user(request):
    return HttpResponse("<h1>HELLO</h1>")
