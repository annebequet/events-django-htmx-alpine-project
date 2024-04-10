
import datetime

import pytest
from django.test import Client

from events.models import Event, Location, ArtisticGenre


@pytest.fixture(scope="function")
def create_user(django_user_model):
    return django_user_model.objects.create_user(
        username="testuser",
        password="123456"
    )

@pytest.fixture(scope="session")
def unauthenticated_client():
    def _unauthenticated_client(test_user):
        client = Client()

        return client

    return _unauthenticated_client

@pytest.fixture(scope="session")
def authenticated_client():
    def _authenticated_client(test_user):
        client = Client()
        client.force_login(test_user)

        return client

    return _authenticated_client


@pytest.fixture(scope="session")
def create_artistic_genre():
    def _create_artistic_genre(**kwargs):
        return ArtisticGenre.objects.create(
            name=kwargs.get("name", "Théâtre"),
        )

    return _create_artistic_genre


@pytest.fixture(scope="session")
def create_location():
    def _create_location(artistic_genre, **kwargs):
        return Location.objects.create(
            name=kwargs.get("name", "Les clochards célestes"),
            address=kwargs.get("address", "6 rue des patates"),
            artistic_genre=artistic_genre
        )

    return _create_location


@pytest.fixture(scope="session")
def create_event():
    def _create_event(artistic_genre, location, **kwargs):
        return Event.objects.create(
            name=kwargs.get("name", "Shakespeare"),
            event_date=kwargs.get("event_date", datetime.date.today()),
            event_time=kwargs.get("event_time", datetime.datetime.now()),
            description=kwargs.get(
                "description",
                "Une histoire de patates."
            ),
            price=kwargs.get("price", 12.5),
            link=kwargs.get("link", "https://testlink.com"),
            location=location,
            event_type=artistic_genre,
        )

    return _create_event