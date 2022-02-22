from cmath import log
import time
from django import forms
from django.contrib.auth import login, authenticate
from user.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Username"}
        )
    )
    password = forms.CharField(min_length=4,
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "Password"}
        )
    )

    # def clean(self):
    #     errors = False
    #     if self.cleaned_data["username"] == "admin":
    #         errors = True
    #         self.add_error("username", "INVALID USER!!!")
    #     if errors:
    #         raise forms.ValidationError("ERROR")
    #     return self.cleaned_data

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.user = user
            return self.cleaned_data
        time.sleep(3)
        self.add_error("username", "invalid username")
        self.add_error("password", "invalid password")
        raise forms.ValidationError("User not found")

    def auth(self, request):
        login(request, self.user)

    