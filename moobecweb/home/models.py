from pyexpat import model
from types import CoroutineType
from django.db import models
import uuid
from django.contrib.auth.models import User 

# Create your models here.
yearChoises=[tuple([x,x]) for x in range(2016,2024)]


SolicitudPropietarioChoises=[
    ('pendiente', 'Pendiente'),
    ('aprobado', 'Aprobado'),
    ('rechazado', 'Rechazado'),
    ('revision', 'Necesita mas informacion'),
]


class SolicitudPropietario(models.Model):
    transact_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    brand=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    year=models.IntegerField(choices=yearChoises, default='2016')
    mileage=models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    owner_id=models.ForeignKey(User, on_delete=models.CASCADE)
    estado=models.CharField(max_length=20,choices=SolicitudPropietarioChoises, default='pendiente')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Solicitud Propietario"
        verbose_name_plural="Solicitudes Propietarios"
    
    def __str__(self):
        return self.brand

