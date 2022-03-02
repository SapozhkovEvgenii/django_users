from django.db import models
from user.models import User
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from datetime import datetime
from random import randint


class Post(models.Model):

    def file_path(self, filename):
        file_type = filename.split(".")[-1]
        path_file = datetime.strftime(datetime.now, "post/%Y/%m/%d/%H")
        return path_file + str(randint(100000000, 999999999)) + "." + file_type

    title = models.CharField(max_length=256, unique=True, verbose_name="Post title")
    tags = models.ManyToManyField("Tag", related_name="posts")
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, verbose_name="Post author")
    text = models.TextField(verbose_name="Post data")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Post created")
    updated = models.DateField(auto_now=True, verbose_name="Post updated")
    is_moderated = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to=file_path)

    def __str__(self) -> str:
        return (self.title[:20] + "...") if len(self.title) > 20 else self.title

    def get_url(self):
        return self.title.replace(" ", "_")

    class Meta:
        db_table = "posts"
        verbose_name = "Post"


class Tag(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"

@receiver(pre_save, sender=Tag)
def sharp(sender, instance, **kwargs):
    if instance.value[0] != "#":
        instance.value = "#" + instance.value


