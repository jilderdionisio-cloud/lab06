from rest_framework import serializers

from .models import Genre, Movie, Review, PerfilUsuario


# Serializer para Genre
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", "description", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


# Serializer para Review
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


# Serializer para PerfilUsuario
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'


# Serializer para Movie
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source="genres"
    )
    reviews = ReviewSerializer(many=True, read_only=True)

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