from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="User phone number")  # null = True, тогда поле необязательно

    """Вложенный класс (способ настроить нашу модель)"""

    class Meta:
        db_table = "users"  # Создание таблицы с именем users
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

