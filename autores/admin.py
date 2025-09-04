from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_creacion')
    list_filter = ('nacionalidad', 'fecha_creacion')
    search_fields = ('nombre', 'biografia', 'nacionalidad')
    ordering = ('nombre',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'fecha_nacimiento', 'nacionalidad')
        }),
        ('Biografía', {
            'fields': ('biografia',),
            'classes': ('collapse',)
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    # Personalizar el formulario de creación
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return (
                ('Información Personal', {
                    'fields': ('nombre', 'fecha_nacimiento', 'nacionalidad', 'biografia')
                }),
            )
        return super().get_fieldsets(request, obj)