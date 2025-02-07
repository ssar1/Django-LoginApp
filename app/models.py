from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  # ✅ Ensure it inherits from AbstractUser
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # ✅ New field
    created_at = models.DateTimeField(auto_now_add=True)

    age = models.IntegerField(blank=True, null=True)  # ✅ New field Testing Schema Migration AGE

    def __str__(self):
        return self.username  # ✅ Use inherited username field
