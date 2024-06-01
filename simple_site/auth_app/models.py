from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    image = models.ImageField(upload_to= "users_image/%Y/%m/%d",blank=True,null=True,verbose_name="Аватар")

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
# Create your models here.
