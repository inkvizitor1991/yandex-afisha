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
            place_raw = response.json()

            imgs_urls = place_raw['imgs']
            place, _ = Places.objects.get_or_create(
                defaults={
                    'title': place_raw['title'],
                    'description_short': place_raw['description_short'],
                    'description_long': place_raw['description_long']
                },
                lat=place_raw['coordinates']['lat'],
                lon=place_raw['coordinates']['lng'],
            )
            for number, img_url in enumerate(imgs_urls, 1):
                image_url_path = urlsplit(img_url).path
                image_name = os.path.split(image_url_path)[-1]
                response = requests.get(img_url)
                response.raise_for_status()

                images, _ = Images.objects.update_or_create(
                    defaults={'order': number},
                    place=place,
                    image=image_name,
                )
                images.image.save(image_name, ContentFile(response.content),
                                  save=True)