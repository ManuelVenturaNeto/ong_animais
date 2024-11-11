from django.urls import path
from .views import login, register_user, register_shelter, logout  #, apply_login

urlpatterns = [
    path('login/', login, name='login'),
    path('register_user/', register_user, name='register_user'),
    path('register_shelter/', register_shelter, name='register_shelter'),
    path('', logout, name='logout'),
    # path('', apply_login, name='apply_login'),
]