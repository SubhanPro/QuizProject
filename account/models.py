from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "account")
    avatar = models.ImageField(upload_to="avatars/")

    def __str__(self):
        return self.user.username