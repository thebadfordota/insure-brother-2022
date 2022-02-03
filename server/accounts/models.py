from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(AbstractUser):
    """
    Данный класс расширяет поля класса 'AbstractUser'.
    """
    about_company = models.CharField(max_length=1000, verbose_name="О компании")
    image = models.ImageField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
