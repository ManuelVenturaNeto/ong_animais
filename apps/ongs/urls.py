from django.urls import path, include
from .views import ongs

urlpatterns = [
    path('ongs/', ongs, name='ongs'),
]