from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    CITIZENSHIP = [
        ("CZE", "cze"),
        ("POL", "pol"),
        ("GER", "ger"),
        ("SVK", "svk"),
        ("AUT", "aut")
    ]

    phone = models.CharField(max_length=24, verbose_name="Phone", null=True, blank=True)
    avatar = models.ImageField(upload_to="users/", verbose_name="Avatar", null=True, blank=True)
    citizenship = models.CharField(max_length=10, verbose_name="Where are you from?", choices=CITIZENSHIP)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name='user_groups', verbose_name='Groups')
    username = None
    email = models.EmailField(unique=True, verbose_name="Mail")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
