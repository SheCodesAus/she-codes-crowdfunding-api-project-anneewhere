from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField() #this is giving us the option for the project to be open or not
    date_created = models.DateTimeField(auto_now_add=True) #by default, this will add the time that it was created.  usually, we always write this line with it. 
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects' 
    )
    liked_by = models.ManyToManyField(
        User,
        related_name='liked_projects'
    )

    @property #a function that applies to a function?
    def total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="pledges")
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE, #cascade deletes everything underneath +/or related to this. 
        related_name='supporter_pledges'
    )

