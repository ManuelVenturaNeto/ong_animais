from django.urls import path
from .views import home, sobre, contato, register_pet, delete_pet, edit_pet


urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato', contato, name='contato'),
    path('register_pet', register_pet, name='register_pet'),
    path('delete_pet/<int:photo_id>', delete_pet, name='delete_pet'),
    path('edit_pet/<int:photo_id>', edit_pet, name='edit_pet')
]

