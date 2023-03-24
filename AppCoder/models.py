from django.db import models
from django.contrib.auth.models import User

   
class Doctor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)
    email=models.EmailField()
    imagen = models.ImageField(upload_to="doctores", null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creado_por")
    
    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''

class Paciente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    imagen = models.ImageField(upload_to="pacientes", null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''

class Medicina(models.Model):
    nombre=models.CharField(max_length=50)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="medicinas", null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(to=User, on_delete=models.CASCADE)

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    @property
    def avatar_url(self):
        return self.avatar.url if self.avatar else ''