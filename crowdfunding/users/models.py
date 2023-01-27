from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=50, blank=True, unique=True)
    # name = models.CharField(max_length=100)
    # email = models.EmailField(("email address"), unique=True, blank=True)
    # profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
        #str(x) = x.__str__()
        #defining how to return this as a string
    
# USERNAME_FIELD = 'username'
