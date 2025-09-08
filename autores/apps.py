from django.apps import AppConfig

class AutoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autores'
    verbose_name = 'Gestión de Autores'
    
    def ready(self):
        # Puedes importar señales aquí si las necesitas luego
        pass