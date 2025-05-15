from django.urls import path

from events.views import EventView

app_name = 'events'

urlpatterns = [
    path("", EventView.as_view(), name="event"),
]