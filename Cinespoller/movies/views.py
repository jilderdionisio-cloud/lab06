from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from .models import Genre, Movie, Review
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    # ========== FILTROS, BÚSQUEDA Y ORDENAMIENTO ==========
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'genres__name']  # ?is_active=true&genres__name=accion
    search_fields = ['title', 'synopsis']            # ?search=batman
    ordering_fields = ['title', 'release_date', 'duration_minutes', 'rating_avg']
    ordering = ['title']                              # Orden por defecto
    
    # ========== ENDPOINT: PROMEDIO DE CALIFICACIONES ==========
    @action(detail=True, methods=['get'], url_path='promedio')
    def promedio_resenas(self, request, pk=None):
        movie = self.get_object()
        promedio = movie.reviews.aggregate(Avg('rating'))['rating__avg']
        total = movie.reviews.count()
        return Response({
            'movie_id': movie.id,
            'title': movie.title,
            'promedio_calificacion': round(promedio, 1) if promedio else None,
            'total_resenas': total
        })
    
    # ========== ENDPOINT: PELÍCULAS POR GÉNERO ==========
    @action(detail=False, methods=['get'], url_path='genero/(?P<genre_name>[^/.]+)')
    def por_genero(self, request, genre_name=None):
        movies = Movie.objects.filter(genres__name__iexact=genre_name, is_active=True)
        serializer = self.get_serializer(movies, many=True)
        return Response({
            'genero': genre_name,
            'total': movies.count(),
            'results': serializer.data
        })