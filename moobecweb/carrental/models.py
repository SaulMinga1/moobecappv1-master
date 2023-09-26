from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class CarModel(models.Model):
    model_name = models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Modelo Auto"
        verbose_name_plural="Modelos Autos"
    
    def __str__(self):
        return self.model_name

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    location_street=models.CharField(max_length=100)
    location_city=models.CharField(max_length=25)
    location_state_name=models.CharField(max_length=25)
    location_zip_code=models.CharField(max_length=5)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Locacion"
        verbose_name_plural="Locaciones"
    
    def __str__(self):
        return self.location_name

class Spots(models.Model):
    location_name = models.CharField(max_length=50)
    location_street=models.CharField(max_length=100)
    location_city=models.CharField(max_length=25)
    location_state_name=models.CharField(max_length=25)
    location_zip_code=models.CharField(max_length=6)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Spot"
        verbose_name_plural="Spots"
    
    def __str__(self):
        return self.location_name

class CarCategories(models.Model):
    categorie_name= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
    
    def __str__(self):
        return self.categorie_name


yearChoises=[tuple([x,x]) for x in range(2016,2023)]

class Vehicle(models.Model):
    #car_id = models.CharField(max_length=16)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    desciption=models.CharField(max_length=250)
    car_year=models.IntegerField(choices=yearChoises)
    car_color=models.CharField(max_length=20)
    car_capacity=models.CharField(max_length=3)
    car_plate_number=models.CharField(max_length=10)
    car_proposal_rate=models.FloatField()
    car_owner_id=models.ForeignKey(User, on_delete=models.CASCADE)
    spot_name=models.ForeignKey(Spots, on_delete=models.CASCADE, default=' 1')
    car_categorie=models.ForeignKey(CarCategories, blank=True, on_delete=models.CASCADE, null=True)
    availability=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Vehiculo"
        verbose_name_plural="Vehiculos"
    
    def __str__(self):
        return self.car_plate_number

reserva_status=[
    ('Confirmado', 'CONFIRMADO'),
    ('Reservado', 'RESERVA TEMPORAL'),
    ('Rechazado', 'RECHAZADO'),
    ('Cancelado', 'CANCELADO'),
    ] 

class Pago(models.Model):
    payment_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    payment_amount = models.FloatField()
    add_charges=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Datafast"
        verbose_name_plural="Datafast"
    
    def __str__(self):
        return str(self.payment_id)




class Reservas(models.Model):
    transact_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    reserved_vehicle= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer_detail= models.ForeignKey(User, on_delete=models.CASCADE)
    pago_id=models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True)
    rental_pickup=models.ForeignKey(Spots, on_delete=models.CASCADE, related_name='rental_pickup')
    rental_dropoff=models.ForeignKey(Spots, on_delete=models.CASCADE, related_name='rental_dropoff')
    rental_start=models.DateTimeField()
    rental_stop=models.DateTimeField()
    reserva_status= models.CharField(choices=reserva_status, max_length=25)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name="Reserva"
        verbose_name_plural="Reservas"
    
    def __str__(self):
        return str(self.transact_id)

reclamo_status=[
    ('Reclamo Recibido', 'Reclamo Recibido'),
    ('Analizando Informacion', 'Analizando Informacion'),
    ('Pago Pendiente', 'Pago Pendiente'),
    ('Transferido a Cuenta', 'Transferido a Cuenta'),
    ('Rechazado','Rechazado')
    ] 

class ReclamoConductor(models.Model):
    transact_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type=models.CharField(max_length=25, )
    claim_status= models.CharField( max_length=25, choices=reclamo_status)
    cost=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name="Reclamo"
        verbose_name_plural="Reclamo Conductor"
    
    def __str__(self):
        return str(self.transact_id)
