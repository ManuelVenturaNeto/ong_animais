from django.urls import path
from ong_animais.views import home, sobre, contato, register_pet, delete_pet, edit_pet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato', contato, name='contato'),
    path('register_pet', register_pet, name='register_pet'),
    path('delete_pet/<int:foto_id>', delete_pet, name='delete_pet'),
    path('edit_pet/<int:foto_id>', edit_pet, name='edit_pet')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
