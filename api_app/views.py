from django.shortcuts import render

# Para autores 

from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import (
    AutorSerializer, EditorialSerializer, LibroSerializer,
    MiembroSerializer, PrestamoSerializer, PrestamoDevolucionSerializer,
    LibroSearchSerializer, AutorSearchSerializer, PrestamoSearchSerializer
)

class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'nacionalidad']

class AutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def destroy(self, request, *args, **kwargs):
        autor = self.get_object()
        # Verificar si el autor tiene libros asociados
        if autor.libro_set.exists():
            return Response(
                {'error': 'No se puede eliminar el autor porque tiene libros asociados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

@api_view(['GET'])
def autor_search(request):
    """Búsqueda avanzada de autores"""
    serializer = AutorSearchSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    queryset = Autor.objects.all()
    
    if data.get('nombre'):
        queryset = queryset.filter(nombre__icontains=data['nombre'])
    if data.get('nacionalidad'):
        queryset = queryset.filter(nacionalidad__icontains=data['nacionalidad'])
    
    serializer = AutorSerializer(queryset, many=True)
    return Response(serializer.data)



# Para editoriales

class EditorialListCreateView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all().order_by('nombre')
    serializer_class = EditorialSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']

class EditorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def destroy(self, request, *args, **kwargs):
        editorial = self.get_object()
        # Verificar si la editorial tiene libros asociados
        if editorial.libro_set.exists():
            return Response(
                {'error': 'No se puede eliminar la editorial porque tiene libros asociados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
    
    
# Para libros
class LibroListCreateView(generics.ListCreateAPIView):
    queryset = Libro.objects.all().select_related('autor', 'editorial').order_by('titulo')
    serializer_class = LibroSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genero', 'año_publicacion']
    search_fields = ['titulo', 'autor__nombre', 'editorial__nombre']

class LibroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all().select_related('autor', 'editorial')
    serializer_class = LibroSerializer

    def destroy(self, request, *args, **kwargs):
        libro = self.get_object()
        # Verificar si el libro tiene préstamos activos
        if libro.prestamo_set.filter(estado='activo').exists():
            return Response(
                {'error': 'No se puede eliminar el libro porque tiene préstamos activos.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

@api_view(['GET'])
def libro_search(request):
    """Búsqueda avanzada de libros"""
    serializer = LibroSearchSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    queryset = Libro.objects.all().select_related('autor', 'editorial')
    
    if data.get('titulo'):
        queryset = queryset.filter(titulo__icontains=data['titulo'])
    if data.get('autor'):
        queryset = queryset.filter(autor__nombre__icontains=data['autor'])
    if data.get('editorial'):
        queryset = queryset.filter(editorial__nombre__icontains=data['editorial'])
    if data.get('genero'):
        queryset = queryset.filter(genero__icontains=data['genero'])
    if data.get('año_min'):
        queryset = queryset.filter(año_publicacion__gte=data['año_min'])
    if data.get('año_max'):
        queryset = queryset.filter(año_publicacion__lte=data['año_max'])
    
    serializer = LibroSerializer(queryset, many=True)
    return Response(serializer.data)


# Para miembros
class MiembroListCreateView(generics.ListCreateAPIView):
    queryset = Miembro.objects.all().order_by('nombre')
    serializer_class = MiembroSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'email']

class MiembroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def destroy(self, request, *args, **kwargs):
        miembro = self.get_object()
        # Verificar si el miembro tiene préstamos activos
        if miembro.prestamo_set.filter(estado='activo').exists():
            return Response(
                {'error': 'No se puede eliminar el miembro porque tiene préstamos activos.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
    

# Para préstamos
class PrestamoListCreateView(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all().select_related('libro', 'miembro').order_by('-fecha_prestamo')
    serializer_class = PrestamoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado']

class PrestamoDetailView(generics.RetrieveUpdateAPIView):
    queryset = Prestamo.objects.all().select_related('libro', 'miembro')
    serializer_class = PrestamoSerializer

    def update(self, request, *args, **kwargs):
        # Para actualizaciones parciales (PATCH)
        return super().update(request, *args, **kwargs)

@api_view(['POST'])
def prestamo_devolucion(request, pk):
    """Registrar devolución de un préstamo"""
    try:
        prestamo = Prestamo.objects.get(pk=pk)
    except Prestamo.DoesNotExist:
        return Response(
            {'error': 'Préstamo no encontrado'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    if prestamo.estado == 'completado':
        return Response(
            {'error': 'Este préstamo ya fue devuelto'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = PrestamoDevolucionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update(prestamo, serializer.validated_data)
        return Response(
            {'message': 'Devolución registrada correctamente'},
            status=status.HTTP_200_OK
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def prestamo_search(request):
    """Búsqueda avanzada de préstamos"""
    serializer = PrestamoSearchSerializer(data=request.query_params)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    queryset = Prestamo.objects.all().select_related('libro', 'miembro')
    
    if data.get('miembro'):
        queryset = queryset.filter(miembro_id=data['miembro'])
    if data.get('estado'):
        queryset = queryset.filter(estado=data['estado'])
    if data.get('fecha_inicio'):
        queryset = queryset.filter(fecha_prestamo__date__gte=data['fecha_inicio'])
    if data.get('fecha_fin'):
        queryset = queryset.filter(fecha_prestamo__date__lte=data['fecha_fin'])
    
    serializer = PrestamoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prestamos_miembro(request, miembro_id):
    """Obtener todos los préstamos de un miembro específico"""
    try:
        Miembro.objects.get(pk=miembro_id)
    except Miembro.DoesNotExist:
        return Response(
            {'error': 'Miembro no encontrado'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    prestamos = Prestamo.objects.filter(
        miembro_id=miembro_id
    ).select_related('libro', 'miembro').order_by('-fecha_prestamo')
    
    serializer = PrestamoSerializer(prestamos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prestamos_activos_miembro(request, miembro_id):
    """Obtener préstamos activos de un miembro específico"""
    try:
        Miembro.objects.get(pk=miembro_id)
    except Miembro.DoesNotExist:
        return Response(
            {'error': 'Miembro no encontrado'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    prestamos = Prestamo.objects.filter(
        miembro_id=miembro_id, 
        estado='activo'
    ).select_related('libro', 'miembro')
    
    serializer = PrestamoSerializer(prestamos, many=True)
    return Response(serializer.data)