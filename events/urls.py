from django.urls import path

from . import views


list_events_urlpatterns = [
   path("", views.EventListPage.as_view(), name="page_event_list"),
]

urlpatterns = list_events_urlpatterns