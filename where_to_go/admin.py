from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin

admin.site.register(Image)

preview_height = 200


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview"]
    fields = ("image", "image_preview")

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.image.url}"  height="{preview_height}" />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

    class Meta:
        model = Place
