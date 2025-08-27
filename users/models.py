from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    tg_chat_id = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="telegram chat id",
        help_text="Укажите telegram chat-id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
