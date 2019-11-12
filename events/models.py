from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    TYPE_CHOICES = [
        ("Public", "public"),
        ("Private", "private")
    ]

    start = models.DateTimeField()
    end = models.DateTimeField()
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(User, related_name="owner", on_delete=models.DO_NOTHING)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    attendees = models.ManyToManyField(User, related_name="attendees")
    no_of_attendees = models.IntegerField(default=0)
    max_attendees = models.IntegerField(default=0)
    invited = models.ManyToManyField(User, related_name="invited")