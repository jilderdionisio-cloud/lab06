from rest_framework import serializers

from .models import Genre, Movie, Review, PerfilUsuario


# NUEVO: Serializer para Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", "description", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# NUEVO: Serializer para Review
class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source="movie",
        write_only=True,
    )

    class Meta:
        model = Review
        fields = (
            "id",
            "movie",
            "movie_id",
            "rating",
            "comment",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


# CAMBIO: MovieSerializer actualizado para incluir géneros y reseñas
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
    # NUEVO: Reseñas asociadas a la película
    reviews = ReviewSerializer(many=True, read_only=True)


# NUEVO: Serializer para PerfilUsuario
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

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
            "reviews",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")