from django.shortcuts import render
#from .models import Vehicle, BookingDetail
from .models import Vehicle, Reservas
import datetime
from .forms import SearchCarForm

# Create your views here.
def rentals(request):
    #vehicles=Vehicle.objects.all()
    form = SearchCarForm(request.POST)
    if form.is_valid():
        if request.method =='POST':
            #check_in=datetime.datetime(2022,8,21)
            #check_out=datetime.datetime(2022,8,23)
            check_in=request.POST.get('check_in')
            check_out=request.POST.get('check_out')
            booked=set(values['reserved_vehicle_id'] for values in Reservas.objects.filter(rental_start__lte=check_out, rental_stop__gte=check_in ).values('reserved_vehicle_id'))
            vehicles=Vehicle.objects.exclude(id__in=booked)
            #vehicles=Vehicle.objects.exclude(id__in=booked).filter(availability=True)
            # vehicles=Vehicle.objects.filter(availability=True)

            #vehicles_count=Vehicle.objects.all().count()
            #return render(request, "homerentals/index.html",{"vehicles": vehicles, 'vehicles_count':vehicles_count })
            return render(request, "homerentals/index.html",{"vehicles": vehicles, "form": form})
            #return render(request, "index.html")
    else:
        vehicles=Vehicle.objects.all()
        return render(request, "homerentals/index.html",{"vehicles": vehicles, "form": form})


#def Vehicles(request):
    
