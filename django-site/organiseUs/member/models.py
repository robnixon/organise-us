from django.db import models

# Create your models here.


class Event(models.Model):
    intro = models.CharField(max_length=300)
    date = models.DateField()
    description = models.CharField(max_length=3000)


class Post(models.Model):
    organisation_posting = models.CharField(max_length=400)
    postText = models.CharField(max_length=5000)
