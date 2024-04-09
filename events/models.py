import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

class ArtisticGenre(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name)


class Location(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    artistic_genre = models.ForeignKey(ArtisticGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    event_date = models.DateField()
    description = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_type = models.ForeignKey(ArtisticGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

