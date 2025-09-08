from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('autores/', views.AutorListCreateView.as_view(), name='autor-list'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    path('autores/buscar/', views.autor_search, name='autor-search'),
    
    # Editoriales
    path('editoriales/', views.EditorialListCreateView.as_view(), name='editorial-list'),
    path('editoriales/<int:pk>/', views.EditorialDetailView.as_view(), name='editorial-detail'),
    
    # Libros
    path('libros/', views.LibroListCreateView.as_view(), name='libro-list'),
    path('libros/<int:pk>/', views.LibroDetailView.as_view(), name='libro-detail'),
    path('libros/buscar/', views.libro_search, name='libro-search'),
    
    # Miembros
    path('miembros/', views.MiembroListCreateView.as_view(), name='miembro-list'),
    path('miembros/<int:pk>/', views.MiembroDetailView.as_view(), name='miembro-detail'),
    
    # Préstamos
    path('prestamos/', views.PrestamoListCreateView.as_view(), name='prestamo-list'),
    path('prestamos/<int:pk>/', views.PrestamoDetailView.as_view(), name='prestamo-detail'),
    path('prestamos/<int:pk>/devolucion/', views.prestamo_devolucion, name='prestamo-devolucion'),
    path('prestamos/buscar/', views.prestamo_search, name='prestamo-search'),
    path('prestamos/miembro/<int:miembro_id>/', views.prestamos_miembro, name='prestamos-miembro'),
    path('prestamos/miembro/<int:miembro_id>/activos/', views.prestamos_activos_miembro, name='prestamos-activos-miembro'),
]

