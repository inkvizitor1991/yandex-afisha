from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.yandex_afisha),
    path('places/<int:place_id>/', views.places),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
