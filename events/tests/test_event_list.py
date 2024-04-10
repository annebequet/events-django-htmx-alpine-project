import datetime


import pytest
from django.urls import reverse


# anyone can access the list of events 
# past events should not be displayed
# events should be ordered by date

@pytest.mark.django_db
def test_event_list_page_returns_list_of_future_events(
    unauthenticated_client,
    create_user,
    create_location,
    create_artistic_genre,
    create_event,
):
    today = datetime.date.today()
    artistic_genre = create_artistic_genre()
    location = create_location(artistic_genre)
    user = create_user

    event_today = create_event(
        artistic_genre,
        location,
        name="event_today",
        event_date=today
    )
    event_future = create_event(
        artistic_genre,
        location,
        name="event_future",
        event_date=today + datetime.timedelta(days=30)
    )
    create_event(
        artistic_genre,
        location,
        name="event_past",
        event_date=today - datetime.timedelta(days=10),
    )

    url = reverse("page_event_list")
    response = unauthenticated_client(user).get(url)

    events_list = list(response.context_data["events"])

    assert response.status_code == 200
    assert len(events_list) == 2
    assert events_list == [event_today, event_future]