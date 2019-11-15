from django.urls import path
from .views import EventViewSet, Register, Unregister

event_add = EventViewSet.as_view({'post': 'create'})
event_delete = EventViewSet.as_view({'get': 'destroy'})
event_list = EventViewSet.as_view({'get': 'list'})

urlpatterns = [
    path("add/", event_add, name="add-event"),
    path("delete/<int:event_id>/<int:user_id>", event_delete, name="delete-event"),
    path("list/<int:pk>", event_list, name="list-event"),
    path("unregister/<str:username>/<int:event_id>", Unregister.as_view(), name="unregister-event"),
    path("register/<str:username>/<int:event_id>", Register.as_view(), name="register-event"),
]