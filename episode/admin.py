from django.contrib import admin

from .models import Episode


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Episode, EpisodeAdmin)
