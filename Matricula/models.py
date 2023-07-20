from django.db import models

# Create your models here.

class Docente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=300)
    
    def __str__(self):
        data = "{0} {1} {2}"
        return data.format(self.dni,self.nombre, self.apellido)
        

class Alumno(models.Model):
    dni = models.PositiveIntegerField(
    validators=[
        MinLengthValidator(8),  # Mínimo 8 dígitos
        MaxLengthValidator(8)   # Máximo 8 dígitos
    ]
)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=300)
    
    def __str__(self):
        data = "{0} {1} {2}"
        return data.format(self.dni,self.nombre, self.apellido)   

