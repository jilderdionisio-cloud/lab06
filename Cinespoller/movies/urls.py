from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
# NUEVO: Registrar GenreViewSet
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = router.urls