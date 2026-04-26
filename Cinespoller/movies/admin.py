from django.contrib import admin

from .models import Genre, Movie, Review, PerfilUsuario


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ("rating", "comment", "created_at")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Genre)
# NUEVO: Admin para Genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("movie__title", "comment")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration_minutes", "release_date", "is_active")
    list_filter = ("is_active", "release_date", "genres")  # CAMBIO: agregado filtro por géneros
    search_fields = ("title",)
    # NUEVO: configurar inline para genres y reviews
    filter_horizontal = ("genres",)
    inlines = (ReviewInline,)


# NUEVO: Registro de PerfilUsuario en admin
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email", "edad", "ciudad")
    search_fields = ("nombre", "email")