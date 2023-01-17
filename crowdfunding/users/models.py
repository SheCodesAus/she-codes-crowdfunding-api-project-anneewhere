from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
        #str(x) = x.__str__()
        #defining how to return this as a string
