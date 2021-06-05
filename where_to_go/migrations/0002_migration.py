from where_to_go.admin import ImageInline
from django.db import migrations


def reorder(apps, schema_editor):
    Image = apps.get_model("where_to_go", "Image")
    my_order = 0
    for Image in Image.objects.all():
        my_order += 1
        Image.my_order = my_order
        Image.save()

class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(reorder),
    ]