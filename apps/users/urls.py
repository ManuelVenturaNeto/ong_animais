from django.urls import path
from .views import users, login, register_user, register_shelter

urlpatterns = [
    path('login/', login, name='login'),
    path('register_user/', register_user, name='register_user'),
    path('register_shelter/', register_shelter, name='register_shelter'),
]