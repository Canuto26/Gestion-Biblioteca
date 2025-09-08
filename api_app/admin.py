from django.contrib import admin

# Register your models here.

# gestion_biblioteca/admin.py
from django.contrib import admin
from .models import Autor, Editorial, Libro, Miembro, Prestamo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nacionalidad']
    search_fields = ['nombre']

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email']
    search_fields = ['nombre']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editorial', 'cantidad_disponible']
    list_filter = ['genero', 'año_publicacion']
    search_fields = ['titulo', 'autor__nombre']

@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['libro', 'miembro', 'estado', 'fecha_prestamo']
    list_filter = ['estado']
    search_fields = ['libro__titulo', 'miembro__nombre']