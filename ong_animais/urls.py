from django.urls import path
from ong_animais.views import home, sobre, contato, registra_pet, deleta_pet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato', contato, name='contato'),
    path('registra_pet', registra_pet, name='registra_pet'),
    path('deleta_pet/<int:foto_id>', deleta_pet, name='deleta_pet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
