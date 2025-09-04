from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Autor
from .serializers import AutorSerializer, AutorListSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nacionalidad']
    search_fields = ['nombre', 'biografia']
    ordering_fields = ['nombre', 'fecha_nacimiento', 'fecha_creacion']
    ordering = ['nombre']

    def get_serializer_class(self):
        if self.action == 'list':
            return AutorListSerializer
        return AutorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtro personalizado por rango de años (ej: ?decada=1980)
        decada = self.request.query_params.get('decada', None)
        if decada:
            try:
                decada = int(decada)
                start_year = decada
                end_year = decada + 9
                queryset = queryset.filter(
                    fecha_nacimiento__year__gte=start_year,
                    fecha_nacimiento__year__lte=end_year
                )
            except ValueError:
                pass
                
        return queryset

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """Endpoint personalizado para estadísticas de autores"""
        total_autores = self.get_queryset().count()
        
        # Estadísticas por nacionalidad
        por_nacionalidad = self.get_queryset().values('nacionalidad').annotate(
            total=models.Count('id')
        ).order_by('-total')
        
        return Response({
            'total_autores': total_autores,
            'autores_por_nacionalidad': list(por_nacionalidad),
            'nacionalidades_unicas': self.get_queryset().values('nacionalidad').distinct().count()
        })

    @action(detail=True, methods=['get'])
    def detalle_completo(self, request, pk=None):
        """Endpoint para obtener detalles completos de un autor"""
        autor = self.get_object()
        serializer = AutorSerializer(autor)
        return Response(serializer.data)