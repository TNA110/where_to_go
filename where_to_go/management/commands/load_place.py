from django.core.management.base import BaseCommand
from where_to_go.models import Place, Image
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Загружает данные из JSON-файла, на который вы укажете ссылку'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        url = url[0]
        response = requests.get(url)
        response.raise_for_status()
        place_data = response.json()
        coordinates = place_data["coordinates"]
        image_urls = place_data["imgs"]

        place = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            longtitude=coordinates["lng"],
            latitude=coordinates['lat'],
        )

        for image_id, image_url in enumerate(image_urls):
            image_id += 1
            response = requests.get(image_url)
            response.raise_for_status()
            image_binary = response.content
            image_file = ContentFile(image_binary)

            Image.objects.get_or_create(
                title=f"{str(image_id)} {place.title}",
                place=place,
                order=image_id,
            )

            image_note = Image.objects.get(title=f"{str(image_id)} {place.title}")
            image_note.image.save(f"{str(image_id)} {place.title}", content=image_file, save=True)
