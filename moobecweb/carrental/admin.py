from django.contrib import admin
from .models import Vehicle,  Location, CarModel, Spots, CarCategories, Pago, Reservas, ReclamoConductor


# Register your models here.

class VehicleInstanceAdmin(admin.TabularInline):
    model=Vehicle

class PagoInstanceAdmin(admin.TabularInline):
    model=Pago

class VehicleAdmin (admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=(  
                    'car_model', 
                    'desciption',
                    'car_year',
                    'car_color',
                    'car_capacity',
                    'car_plate_number',
                    'car_proposal_rate',
                    'car_categorie',
                    'availability',
                    'car_owner_id',
                    'spot_name')
    search_fields=('car_plate_number','car_owner_id__username')
    raw_id_fields=['car_model','car_owner_id','spot_name','car_categorie']
    search_help_text=('Buscar por: # de placa, nombre de cliente')


class CarModelAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('model_name',)
    search_fields=('model_name',)

class LocationAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('location_name','location_street','location_city','location_state_name','location_zip_code')
    search_fields=('location_name',)

class SpotsAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('location_name','location_street','location_city','location_state_name','location_zip_code')
    search_fields=('location_name',)

class CarCategoriesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('categorie_name',)
    search_fields=('categorie_name',)



class BookingDetailAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('transact_id','reserved_vehicle','customer_detail','pago_id','rental_start','rental_stop','booking_detail_status')
    search_fields=('transact_id','customer_detail__username', 'pago_id')
    search_help_text=[]


    
class ReservasAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('transact_id','reserved_vehicle','customer_detail','pago_id','rental_pickup','rental_dropoff','rental_start','rental_stop','reserva_status')
    search_fields=('transact_id','customer_detail__first_name', 'pago_id__payment_id')
    raw_id_fields=['customer_detail','reserved_vehicle','pago_id','rental_pickup','rental_dropoff']
    search_help_text=('Buscar por: # de transaccion, Nombre de cliente, # de pago')
    #fieldsets = (
     #   ('Availability', {
      #      'fields': ('customer_detail',)
      #  }),)

class reservaInstanceAdmin(admin.StackedInline):
    model= Reservas
    extra=0
    raw_id_fields=['customer_detail','reserved_vehicle', 'rental_pickup', 'rental_dropoff']

class PagoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('payment_id','payment_amount','add_charges')
    search_fields=('payment_id',)
    search_help_text=('Buscar por: # de pago')
    inlines=[reservaInstanceAdmin]

class ReclamoConductoresAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=('transact_id','user_id','incident_type','claim_status','cost')
    search_fields=('transact_id',)
    search_help_text=('Buscar por: # de transaccion')
    




admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(CarModel, CarModelAdmin)
#admin.site.register(Location, LocationAdmin)
admin.site.register(Spots, SpotsAdmin)
admin.site.register(CarCategories, CarCategoriesAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Reservas, ReservasAdmin)
admin.site.register(ReclamoConductor, ReclamoConductoresAdmin)
