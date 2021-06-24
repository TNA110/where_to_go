from django.shortcuts import get_object_or_404, render
from .models import Place, Image
from django.http import JsonResponse


def create_geojson(place):
    longtitude = place.longtitude
    latitude = place.latitude
    title = place.title
    placeId = place.id
    detailsUrl = f'places/{placeId}'
    place_geojson = {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [longtitude, latitude]},
        "properties": {
          "title": title,
          "placeId": placeId,
          "detailsUrl": detailsUrl
        }
    }
    return place_geojson


def create_geodata():
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(create_geojson(place))
    geodata = {"geodata": {"type": "FeatureCollection", "features": features}}
    return geodata


def startpage(request):
    geodata = create_geodata()
    return render(request, 'startpage.html', context=geodata)


def create_images_list(place):
    images_list = []
    images = Image.objects.filter(place=place)
    for image in images:
        image_url = str(image.image.url)
        images_list.append(image_url)
    return(images_list)


def endpoint(request, place_id):
    places = Place.objects.all()
    place = get_object_or_404(places, id=place_id)
    images = create_images_list(place)
    context = {"title": place.title, "imgs": images, "description_short": place.description_short, "description_long": place.description_long, "coordinates": {"lat": place.latitude, "lng": place.longtitude}}
    response = JsonResponse(context, json_dumps_params=dict(ensure_ascii=False, indent=2))
    return response
