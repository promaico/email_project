from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_("Username"), max_length=50, unique=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    USERNAME_FIELD = "username"
    
    def __str__(self):
        return self.username


class EmailAccount(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "E-Mail Accounts"

    def __str__(self):
        return self.email
