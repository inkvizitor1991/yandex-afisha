from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Places


def yandex_afisha(request):
    places = Places.objects.all()

    place_with_description = []
    for place in places:
        description = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lon, place.lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse('places', args=[place.id])
                    }
                }
            ]
        }

        place_with_description.append(description)

    context = {"description": place_with_description}
    return render(request, 'index.html', context=context)


def places(request, place_id):
    place = get_object_or_404(Places, pk=place_id)

    context = {
        "title": place.title,
        "imgs": [place.image.url for place in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(
        context,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )