from django.db import models
from django.utils import timezone

# Create your models here.

from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True, default='')
    name = models.CharField(max_length=200, default='')
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """
        Hashes the raw password and stores it in the password field.
        """
        self.password = make_password(raw_password)

    
    
# JESS STRUCTURE.
# from django.db import models


class Letter(models.Model):
    title = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
