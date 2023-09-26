from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models
import uuid
from carrental.models import Vehicle
from django.contrib.auth.models import User
import pytz
from django.db.models.signals import post_save

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField(null= True, blank=True, default='2000-12-12')
    birth_place= models.CharField(null=True, max_length=50, blank=True)
    licencia_conductor=models.CharField(null=True, max_length=50, blank=True)
    fecha_emision_licencia=models.DateField(null=True, blank=True)
    pais_emision_licencia=models.CharField(null=True, max_length=50, choices=pytz.country_names.items(), blank=True, default='EC')
    numero_telefono=models.CharField(null=True, max_length=12, blank=True)
    direccion=models.CharField(null=True, max_length=50,blank=True)
    ciudad=models.CharField(null=True, max_length=50, blank=True)
    pais=models.CharField(null=True, max_length=25, choices=pytz.country_names.items(), blank=True)
    bio=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user.username)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)
    
    def save(self, *args, **kwargs):
        self.DOB = self.DOB
        super().save(*args, **kwargs)








