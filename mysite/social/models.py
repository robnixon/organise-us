from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text
