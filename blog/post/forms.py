from django import forms
from post.models import Post


class PostForm(forms.Form):
    class Meta:
        model = Post
        exclude = ("created", "updated", "is_moderited", "views")

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data