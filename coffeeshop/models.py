from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    duration = models.IntegerField()
    description = models.TextField()

    def __unicode__(self):
        return "Doing " + self.name + " at " + self.location

