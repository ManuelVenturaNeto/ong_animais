from django.urls import path
from ong_animais.views import index

urlpatterns = [
    path('', index, name='index'),
]