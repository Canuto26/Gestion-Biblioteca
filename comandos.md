# Comandos de instalacion

## Crear entorno virtual
python -m venv venv

## Activar entorno virtual (Windows)
venv\Scripts\activate

## Instalar requerimientos dependencias
pip install -r requirements.txt



# Instalacion de dependencias

## Django
pip install Django

## Django Rest framework
pip install djangorestframework

## Headers Cors
pip install django-cors-headers

## Adaptador PostgreSQL
pip install psycopg2-binary

## Sistema de filtrado
pip install django-filter



# Comandos para probar las aplicacion

## Autores
### Crear y aplicar migraciones
python manage.py makemigrations autores
python manage.py migrate

### Ejecutar el servidor
python manage.py runserver