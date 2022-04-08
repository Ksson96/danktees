from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=200)
