# Generated by Django 3.2.9 on 2021-12-11 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_places_json_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='json_path',
        ),
    ]
