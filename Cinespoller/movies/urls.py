from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, MovieViewSet, ReviewViewSet, PerfilUsuarioViewSet

router = DefaultRouter()
# NUEVO: Registrar GenreViewSet
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"reviews", ReviewViewSet, basename="review")
# NUEVO: Registrar PerfilUsuarioViewSet con endpoint usuarios
router.register(r"usuarios", PerfilUsuarioViewSet, basename="perfilusuario")

urlpatterns = router.urls