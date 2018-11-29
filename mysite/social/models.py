from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    user = models.ForeignKey(User, unique=False, null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text
