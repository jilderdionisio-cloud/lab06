from django.db import models


class Genre(models.Model):
    # NUEVO: Entidad Genre para categorizar películas
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "genre"
        verbose_name_plural = "genres"

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)
    # NUEVO: Relación muchos a muchos con Genre
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.title