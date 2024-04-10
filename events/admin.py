from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, ArtisticGenre, Location, Event


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass


@admin.register(ArtisticGenre)
class ArtisticGenreAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid",)