from django.shortcuts import render, HttpResponse
import json


def user(request):
    context = {"key": "value", "result": "True"}
    return render(request, "login.html", context)
    # return HttpResponse(json.dumps(context), content_type="application/json")

