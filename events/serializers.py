from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ['id', "attendees", "no_of_attendees"]


class EventShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['id', 'attendees', 'no_of_attendees', 'invited']