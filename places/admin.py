from django.contrib import admin
from .models import Places, Images

from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Images
    fields = [
        'title', 'description_short',
        'description_long', 'lat',
        'lon', 'show_image'
    ]
    readonly_fields = ['show_image']

    def show_image(self, instance):
        return format_html(
            f'<img src="{instance.image.url}" style="max-height: 200px;">')

    show_image.short_description = "Image"


@admin.register(Places)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Images)
