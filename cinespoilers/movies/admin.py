from django.contrib import admin

from .models import Genre, Movie


@admin.register(Genre)
# NUEVO: Admin para Genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration_minutes", "release_date", "is_active")
    list_filter = ("is_active", "release_date", "genres")  # CAMBIO: agregado filtro por géneros
    search_fields = ("title",)
    # NUEVO: configurar inline para genres
    filter_horizontal = ("genres",)