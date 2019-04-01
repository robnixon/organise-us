from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


class Org(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    picture = models.CharField(max_length=500)  # Link to hosted image
    address = models.CharField(max_length=500)


class Admin(models.Model):
    username = models.CharField(max_length=20, primary_key=True)  # primary key
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)  # need to encrypt this!
    picture = models.CharField(max_length=500)  # URL to hosted image
    org = models.ForeignKey(Org, unique=False, null=True, on_delete=models.SET_NULL)


class OrgUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)  # url to user profile image.
    member_status = models.IntegerField(blank=True, null=True)  # E.g. 1 for current, 2 for inactive ...
    organisation = models.ForeignKey(Org, unique=False, blank=True, null=True, on_delete=models.CASCADE)
    payment = models.CharField(max_length=100, blank=True, null=True)  # In prod app would be payment token or something.

    @receiver(post_save, sender=User)
    def create_org_user(sender, instance, created, **kwargs):
        if created:
            OrgUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_org_user(sender, instance, **kwargs):
        instance.orguser.save()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    user = models.ForeignKey(User, unique=False, null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField('date published', default=timezone.now, editable=False)
    organisation = models.ForeignKey(Org, unique=False, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('social:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post_text


class ChatMessage(models.Model):
    user = models.ForeignKey(User, unique=False, null=True, on_delete=models.SET_NULL)
    message_text = models.CharField(max_length=500)
    timestamp = models.DateField()


class Chat(models.Model):
    chat_messages = models.ForeignKey(ChatMessage, unique=False, null=True, on_delete=models.CASCADE)
