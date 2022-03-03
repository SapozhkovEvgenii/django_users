from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("author", "created", "updated", "is_moderated", "views")

    def clean(self):
        return self.cleaned_data