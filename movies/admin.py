from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','air_date']


admin.site.register(Movie, MovieAdmin)
