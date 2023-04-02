from django.contrib import admin

from .models import Planet


class PlanetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Planet, PlanetAdmin)
