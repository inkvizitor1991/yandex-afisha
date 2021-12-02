from django.contrib import admin
from django.urls import path
from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.yandex_afisha),
]