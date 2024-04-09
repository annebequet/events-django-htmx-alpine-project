# Generated by Django 4.2.7 on 2024-04-09 16:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtisticGenre',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('party_date', models.DateField()),
                ('party_time', models.TimeField()),
                ('invitation', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('artistic_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.artisticgenre')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.artisticgenre')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.location')),
            ],
        ),
    ]
