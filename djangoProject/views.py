from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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
                        "detailsUrl": place.json_path
                    }
                }
            ]
        }

        place_with_description.append(description)

    context = {"description": place_with_description}
    return render(request, 'index.html', context=context)


def places(request, place_id):
    place = get_object_or_404(Places, pk=place_id)
    return HttpResponse(place.title)