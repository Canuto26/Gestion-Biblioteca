from django.http import JsonResponse
from django.shortcuts import render

def home_view(request):
    """Vista para la página principal que muestra información de la API"""
    api_info = {
        "message": "Bienvenido a la API de Gestión de Biblioteca",
        "version": "1.0.0",
        "description": "API REST para gestionar una biblioteca con autores, libros, editoriales, miembros y préstamos",
        "endpoints": {
            "autores": {
                "list": "/api/autores/",
                "detail": "/api/autores/{id}/",
                "search": "/api/autores/buscar/"
            },
            "editoriales": {
                "list": "/api/editoriales/",
                "detail": "/api/editoriales/{id}/"
            },
            "libros": {
                "list": "/api/libros/",
                "detail": "/api/libros/{id}/",
                "search": "/api/libros/buscar/"
            },
            "miembros": {
                "list": "/api/miembros/",
                "detail": "/api/miembros/{id}/"
            },
            "prestamos": {
                "list": "/api/prestamos/",
                "detail": "/api/prestamos/{id}/",
                "search": "/api/prestamos/buscar/",
                "devolucion": "/api/prestamos/{id}/devolucion/",
                "por_miembro": "/api/prestamos/miembro/{id}/",
                "activos_por_miembro": "/api/prestamos/miembro/{id}/activos/"
            }
        },
        "admin": "/admin/",
        "documentation": "Para más información sobre cómo usar la API, consulta la documentación del proyecto"
    }
    
    return JsonResponse(api_info, json_dumps_params={'indent': 2, 'ensure_ascii': False})
