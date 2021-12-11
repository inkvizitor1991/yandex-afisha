from django.contrib import admin
from .models import Places, Images


class ImageInline(admin.TabularInline):
    model = Images


@admin.register(Places)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Images)
