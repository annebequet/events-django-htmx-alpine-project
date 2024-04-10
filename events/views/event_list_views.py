import datetime

from django.views.generic import ListView

from events.models import Event


class EventListPage(ListView):
    template_name = "event/event_list/page_events_list.html"
    context_object_name = "events"

    def get_queryset(self):
        events = Event.objects.filter(
            event_date__gte=datetime.date.today()
        ).order_by(
            "event_date"
        )

        return events