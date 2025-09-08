# serializers.py
from rest_framework import serializers
from .models import Autor, Editorial, Libro, Miembro, Prestamo

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
    
    def validate_nombre(self, value):
        """Valida que el nombre no esté vacío"""
        if not value.strip():
            raise serializers.ValidationError("El nombre no puede estar vacío")
        return value

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'
    
    def validate_nombre(self, value):
        """Valida que el nombre no esté vacío"""
        if not value.strip():
            raise serializers.ValidationError("El nombre no puede estar vacío")
        return value
    
    def validate_email(self, value):
        """Valida el formato del email si se proporciona"""
        if value and '@' not in value:
            raise serializers.ValidationError("El email debe tener un formato válido")
        return value

class LibroSerializer(serializers.ModelSerializer):
    # Campos de solo lectura para mostrar información relacionada
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)
    editorial_nombre = serializers.CharField(source='editorial.nombre', read_only=True)
    
    class Meta:
        model = Libro
        fields = '__all__'
        read_only_fields = ('cantidad_disponible',)
    
    def validate_isbn(self, value):
        """Valida que el ISBN tenga al menos 10 caracteres"""
        if len(value) < 10:
            raise serializers.ValidationError("El ISBN debe tener al menos 10 caracteres")
        return value
    
    def validate_año_publicacion(self, value):
        """Valida que el año de publicación sea razonable"""
        if value and (value < 1000 or value > 2100):
            raise serializers.ValidationError("El año de publicación debe ser válido")
        return value

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = '__all__'
        read_only_fields = ('fecha_registro',)
    
    def validate_email(self, value):
        """Valida el formato del email"""
        if '@' not in value:
            raise serializers.ValidationError("El email debe tener un formato válido")
        return value

class PrestamoSerializer(serializers.ModelSerializer):
    # Campos de solo lectura para mostrar información relacionada
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)
    miembro_nombre = serializers.CharField(source='miembro.nombre', read_only=True)
    
    class Meta:
        model = Prestamo
        fields = '__all__'
        read_only_fields = ('fecha_prestamo', 'estado')
    
    def validate(self, data):
        """Validaciones personalizadas para préstamos"""
        # Validar que la fecha de devolución esperada sea futura
        if 'fecha_devolucion_esperada' in data:
            from django.utils.timezone import now
            if data['fecha_devolucion_esperada'] < now().date():
                raise serializers.ValidationError({
                    'fecha_devolucion_esperada': 'La fecha de devolución debe ser futura'
                })
        
        # Validar disponibilidad del libro al crear préstamo
        if self.instance is None and 'libro' in data:  # Solo al crear
            libro = data['libro']
            if libro.cantidad_disponible <= 0:
                raise serializers.ValidationError({
                    'libro': 'Este libro no está disponible para préstamo'
                })
        
        return data

    def create(self, validated_data):
        """Sobrescribir create para actualizar la cantidad disponible"""
        libro = validated_data['libro']
        
        # Verificar disponibilidad nuevamente (doble verificación)
        if libro.cantidad_disponible <= 0:
            raise serializers.ValidationError({
                'libro': 'Este libro no está disponible para préstamo'
            })
        
        # Crear el préstamo
        prestamo = Prestamo.objects.create(**validated_data)
        
        # Actualizar la cantidad disponible del libro
        libro.cantidad_disponible -= 1
        libro.save()
        
        return prestamo

class PrestamoDevolucionSerializer(serializers.Serializer):
    """Serializer específico para registrar devoluciones"""
    fecha_devolucion_real = serializers.DateTimeField()
    
    def update(self, instance, validated_data):
        """Manejar la devolución de un libro"""
        instance.fecha_devolucion_real = validated_data['fecha_devolucion_real']
        instance.estado = 'completado'
        instance.save()
        
        # Incrementar la cantidad disponible del libro
        libro = instance.libro
        libro.cantidad_disponible += 1
        libro.save()
        
        return instance
    
# serializers.py (continuación)
class LibroSearchSerializer(serializers.Serializer):
    """Serializer para parámetros de búsqueda de libros"""
    titulo = serializers.CharField(required=False)
    autor = serializers.CharField(required=False)
    editorial = serializers.CharField(required=False)
    genero = serializers.CharField(required=False)
    año_min = serializers.IntegerField(required=False, min_value=1000, max_value=2100)
    año_max = serializers.IntegerField(required=False, min_value=1000, max_value=2100)

class AutorSearchSerializer(serializers.Serializer):
    """Serializer para parámetros de búsqueda de autores"""
    nombre = serializers.CharField(required=False)
    nacionalidad = serializers.CharField(required=False)

class PrestamoSearchSerializer(serializers.Serializer):
    """Serializer para parámetros de búsqueda de préstamos"""
    miembro = serializers.IntegerField(required=False)
    estado = serializers.ChoiceField(
        choices=[('activo', 'Activo'), ('completado', 'Completado'), ('atrasado', 'Atrasado')],
        required=False
    )
    fecha_inicio = serializers.DateField(required=False)
    fecha_fin = serializers.DateField(required=False)