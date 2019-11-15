from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class Event(models.Model):
    TYPE_CHOICES = [
        ("Public", "Public"),
        ("Private", "Private")
    ]

    start = models.DateTimeField()
    end = models.DateTimeField()
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.DO_NOTHING, unique=False)
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, default="Public")
    attendees = models.ManyToManyField(User, related_name="attendees", blank=True)
    no_of_attendees = models.IntegerField(default=0)
    max_attendees = models.IntegerField(default=0)
    invited = models.ManyToManyField(User, related_name="invited", blank=True)

    def clean(self):
        if self.end <= self.start:
            raise ValidationError("End datetime cannot be less or equal to start datetime")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)