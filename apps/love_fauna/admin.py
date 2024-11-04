from django.contrib import admin
from .models import Pet

class ListaPet(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_display_links = ("id", "name",)
    search_fields = ("name",)
    list_filter = ("category",)
    list_per_page = 10



admin.site.register(Pet,ListaPet)