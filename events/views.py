from django.views.generic import ListView

from events.models import EventModel


class EventView(ListView):
    model = EventModel
    template_name = 'main.html'
    context_object_name = 'event'
