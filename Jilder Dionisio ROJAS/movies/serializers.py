from rest_framework import serializers

from .models import Genre, Movie


# NUEVO: Serializer para Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", "description", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# CAMBIO: MovieSerializer actualizado para incluir géneros
class MovieSerializer(serializers.ModelSerializer):
    # NUEVO: Incluir géneros como objetos anidados (lectura)
    genres = GenreSerializer(many=True, read_only=True)
    # NUEVO: IDs de géneros para escritura
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source="genres"
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "synopsis",
            "duration_minutes",
            "release_date",
            "is_active",
            "genres",
            "genre_ids",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")