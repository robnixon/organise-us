from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Org(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    picture = models.CharField(max_length=500)  # Link to hosted image
    address = models.CharField(max_length=500, primary_key=True)

    class Meta:
        unique_together = (('picture', 'address'),)


class Admin(models.Model):
    username = models.CharField(max_length=20, primary_key=True)  # primary key
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)  # need to encrypt this!
    picture = models.CharField(max_length=500)  # URL to hosted image
    org = models.ForeignKey(Org, unique=False, null=True, on_delete=models.SET_NULL)


class OrgUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    member_status = models.IntegerField()  # E.g. 1 for current, 2 for inactive ...
    organisations = models.ForeignKey(Org, unique=False, null=True, on_delete=models.CASCADE)
    payment = models.CharField(max_length=100)  # In prod app would be payment token or something.


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    user = models.ForeignKey(User, unique=False, null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('date published', default=timezone.now, editable=False)

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post_text


class ChatMessage(models.Model):
    org_user_id = models.ForeignKey(OrgUser, unique=False, null=True, on_delete=models.SET_NULL)
    message_text = models.CharField(max_length=500)
    timestamp = models.DateField()


class Chat(models.Model):
    chat_messages = models.ForeignKey(ChatMessage, unique=False, null=True, on_delete=models.CASCADE)
