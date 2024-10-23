from django.contrib import admin
from .models import Pet,usuario

class ListaPet(admin.ModelAdmin):
    list_display = ("id", "nome",)
    list_display_links = ("id", "nome",)
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 10



admin.site.register(Pet,ListaPet)