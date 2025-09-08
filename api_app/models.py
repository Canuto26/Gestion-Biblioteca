from django.db import models



from django.db import models
from django.core.validators import MinValueValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.RESTRICT)
    editorial = models.ForeignKey(Editorial, on_delete=models.RESTRICT)
    isbn = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    año_publicacion = models.IntegerField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0)]
    )
    
    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('completado', 'Completado'),
        ('atrasado', 'Atrasado'),
    ]
    
    libro = models.ForeignKey(Libro, on_delete=models.RESTRICT)
    miembro = models.ForeignKey(Miembro, on_delete=models.RESTRICT)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='activo'
    )
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.miembro.nombre}"