import os
from urllib.parse import urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Images, Places


class Command(BaseCommand):
    help = 'Укажите путь до файла JSON.'

    def add_arguments(self, parser):
        parser.add_argument('load_place', nargs='+')

    def handle(self, *args, **options):
        for place in options['load_place']:
            response = requests.get(place)
            response.raise_for_status()
            place = response.json()

            title = place['title']
            imgs = place['imgs']
            description_short = place['description_short']
            description_long = place['description_long']
            lon = place['coordinates']['lng']
            lat = place['coordinates']['lat']

            places, _ = Places.objects.get_or_create(
                title=title,
                description_short=description_short,
                description_long=description_long,
                lat=lat,
                lon=lon,
            )
            for number, img in enumerate(imgs, 1):
                parse_image_url = urlsplit(img)
                image_name = os.path.split(parse_image_url.path)[-1]
                response = requests.get(img)
                response.raise_for_status()

                images, _ = Images.objects.update_or_create(
                    order=number,
                    places=places,
                    image=image_name,
                )
                images.image.save(image_name, ContentFile(response.content),
                                  save=True)
