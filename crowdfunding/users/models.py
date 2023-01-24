from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username
        #str(x) = x.__str__()
        #defining how to return this as a string
