from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    user = models.ForeignKey(User, unique=False, null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('date published', default=timezone.now, editable=False)

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post_text
