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
    organisations = models.CharField(
        max_length=1000)  # Need to find better way to store list of orgs a member is part of.
    payment = models.CharField(max_length=100)  # In prod app would be payment token or something.


class Events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_date = models.DateField()
    event_admin = models.ForeignKey(OrgAdmin, unique=False, on_delete=models.CASCADE)
    description = models.TextField


class Email(models.Model):
    email_id = models.IntegerField(primary_key=True)
    orgUserId = models.ForeignKey(OrgUser, unique=False, null=True, on_delete=models.SET_NULL)
    orgUserRecipient = models.CharField(OrgUser)
    email_subject = models.CharField(max_length=1000)
    email_body = models.TextField
    timestamp = models.DateField()
