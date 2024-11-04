from django.urls import path, include
from .views import clinicas

urlpatterns = [
    path('clinicas/', clinicas, name='clinicas'),
]