from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Consultorio(models.Model):

    especialidad=models.CharField(max_length=40)
    sala = models.IntegerField()
    def __str__(self):
        return f"Especialidad {self.especialidad} - Sala {self.sala}"



class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    obra_social= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - obra_social {self.obra_social}"


class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    especialidad= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Especialidad {self.especialidad}"


from django.contrib.auth.models import User

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

