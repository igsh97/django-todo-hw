from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile=models.TextField(null=True,blank=True)
    like_todos=models.ManyToManyField("todo.Todo",related_name="like_users")
    followings=models.ManyToManyField("self",symmetrical=False,related_name="followers")