from django.urls import path
from ong_animais.views import home, sobre, contato, cadastra_pet, deleta_pet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato', contato, name='contato'),
    path('cadastra_pet', cadastra_pet, name='cadastra_pet'),
    path('deleta_pet', deleta_pet, name='deleta_pet'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
