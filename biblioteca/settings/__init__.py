from .base import *
# Importar el entorno específico según la variable de entorno
# Por defecto: development
import os

env = os.environ.get('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
else:
    from .development import *