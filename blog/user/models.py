from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver


class User(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="User phone number")  # null = True - field is not required

    class Meta:
        db_table = "users"  # Create a table called users
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username + " " "|" + " " + self.phone


@receiver(pre_save, sender=User)
def hash_password(sender, instance, **kwargs):
    if (instance.id is None) or (
            sender.objects.get(id=instance.id).password != instance.password
    ):
        instance.set_password(instance.password)

