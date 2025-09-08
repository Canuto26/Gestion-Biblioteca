from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet, basename='autor')

urlpatterns = [
    path('', include(router.urls)),
]

# URLs adicionales personalizadas (si necesitas endpoints específicos)
additional_patterns = [
    # Puedes agregar endpoints personalizados aquí si no usas ViewSet
]

urlpatterns += additional_patterns