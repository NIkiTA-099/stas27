from django.contrib import admin
from django.urls import path
from stas.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostHome, name="home"),
    path('json/', MyView, name="json")
]
