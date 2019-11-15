from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.views import APIView, View
from .serializers import EventSerializer, EventShowSerializer
from rest_framework import status, viewsets
import json
from .models import Event
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db.models import F


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return HttpResponse(json.dumps({"status": "Saved!"}), status=status.HTTP_201_CREATED,
                                content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": "Invalid JSON", "errors": serializer.errors}),
                                status=status.HTTP_400_BAD_REQUEST, content_type="application/json")

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return HttpResponse(json.dumps({"status": "Event with id " + str(pk) + " deleted"}),
                            status=status.HTTP_200_OK,
                            content_type="application/json")

    def list(self, request, *args, **kwargs):
        """
        pk = request.user.pk
        public_events = Event.objects.filter( type='Public')
        private_events = Event.objects.filter(type= "Private', invited__in=[pk])
        """
        pk = kwargs['pk']
        public_events = Event.objects.filter(type='Public')
        private_events = Event.objects.filter(type='Private', invited__in=[pk])

        events = public_events.union(private_events)
        serializer = EventShowSerializer(events, many=True)

        return HttpResponse(json.dumps(serializer.data), status=status.HTTP_302_FOUND, content_type="application/json")


class Register(APIView):
    def get(self, *args, **kwargs):

        event_id = kwargs['event_id']
        username = kwargs['username']

        event = get_object_or_404(Event, pk=event_id)
        user = get_object_or_404(User, username=username)

        public_events = Event.objects.filter(type='Public', attendees__in=[user.pk])
        private_events = Event.objects.filter(type='Private', attendees__in=[user.pk])

        events = public_events.union(private_events)
        flag = True

        for e in events:
            if e.start <= event.start <= e.end or e.start <= event.end <= e.end:
                flag = False
                break
        if flag:
            if event.no_of_attendees < event.max_attendees:
                event.attendees.add(user)
                event.no_of_attendees += 1
                event.save()
                return HttpResponse(json.dumps({"status": "user added in the event successfully"}),
                                    status=status.HTTP_200_OK,
                                    content_type="application/json")
            else:
                return HttpResponse(json.dumps({"status": "event full!"}),
                                    status=status.HTTP_200_OK,
                                    content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": "Conflict in event occurred"}),
                                status=status.HTTP_304_NOT_MODIFIED,
                                content_type="application//json")


class Unregister(APIView):
    def get(self, username, event_id):
        user = get_object_or_404(User, username=username)
        event = get_object_or_404(Event, pk=event_id)

        event.attendees.remove(user)
        event.no_of_attendees -= 1
        event.save()
        return HttpResponse(json.dumps({"status": "user removed from the event successfully"}),
                            status=status.HTTP_200_OK,
                            content_type="application/json")


