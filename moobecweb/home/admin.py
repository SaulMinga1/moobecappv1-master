from django.contrib import admin
from .models import SolicitudPropietario

# Register your models here.


class SolicitudPropietarioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=(  
                    'transact_id',
                    'brand', 
                    'model',
                    'year',
                    'mileage',
                    'city',
                    'owner_id',
                    'estado',
                    )
    search_fields=('transact_id','owner_id',)

admin.site.register(SolicitudPropietario, SolicitudPropietarioAdmin)