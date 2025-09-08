from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    # Campo calculado para edad (opcional)
    edad = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Autor
        fields = [
            'id', 
            'nombre', 
            'fecha_nacimiento', 
            'nacionalidad', 
            'biografia', 
            'fecha_creacion', 
            'fecha_actualizacion',
            'edad'
        ]
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion')

    def get_edad(self, obj):
        from datetime import date
        if obj.fecha_nacimiento:
            today = date.today()
            return today.year - obj.fecha_nacimiento.year - (
                (today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day)
            )
        return None

    def validate_nombre(self, value):
        """Validar que el nombre tenga al menos 2 palabras"""
        if len(value.strip().split()) < 2:
            raise serializers.ValidationError("El nombre debe contener al menos nombre y apellido")
        return value

class AutorListSerializer(serializers.ModelSerializer):
    # Serializer simplificado para listado
    total_libros = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad', 'total_libros']

    def get_total_libros(self, obj):
        # Esto funcionará cuando tengamos la relación con libros
        return 0  # Por ahora 0, luego se actualizará