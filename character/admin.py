from django.contrib import admin

from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Character, CharacterAdmin)
