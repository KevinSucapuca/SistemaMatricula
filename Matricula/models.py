from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from datetime import datetime
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


class Curso(models.Model):
    nombreCurso = models.CharField(max_length=40)
    vacantes = models.PositiveIntegerField(
    validators=[
        MaxLengthValidator(3)   # Máximo 3 dígitos
    ]
)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    
    def __str__(self):
        data = "{0} {1} {2}"
        return data.format(self.nombreCurso, self.vacantes, self.docente) 


class Ciclo(models.Model):
    nombreCiclo = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    
    def __str__(self):
        data = "{0} {1} "
        return data.format(self.nombreCiclo, self.carrera) 


class CicloCurso(models.Model):
    ciclo = models.ForeignKey(Ciclo, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    def __str__(self):
        data = "{0} {1}"
        return data.format(self.ciclo, self.curso) 

class Matricula(models.Model):
    fecha = models.DateField()  
    alumnoMatricula = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    turno = models.CharField(max_length=15)
    modalidad = models.CharField(max_length=20)
    cicloMatricula = models.ForeignKey(Ciclo, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{0} {1}".format(self.fecha.strftime('%d/%m/%Y'), self.alumnoMatricula) 

