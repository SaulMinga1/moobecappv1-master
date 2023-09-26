from audioop import reverse
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from carrental.models import Reservas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView
from carrental.models import ReclamoConductor, Pago
from .models import Profile
from .forms import ReclamoConductorForm, ProfileForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from django.forms.models import model_to_dict

# Create your views here.
@login_required()
def dashboard(request):
    #bookingdetail=BookingDetail.objects.all()
    #bookingdetail_count=BookingDetail.objects.all().count() DEVULEVE TODOS LOS REGISTROS
    bookingdetail_count= Reservas.objects.filter(customer_detail=request.user)
    if request.user.groups.filter( name='Owner').exists():
        return render(request, "dashboard/propietarios.html", { 'bookingdetail_count':bookingdetail_count })
    else:
        return render(request, "dashboard/index.html", { 'bookingdetail_count':bookingdetail_count })


#def BookingDetailsView(request):
#    bookingdetail=BookingDetail.object.all()
#    bookingdetail_count=BookingDetail.objects.all().count()
#    return render(request, "dashboard/index.html",{ 'bookingdetail': bookingdetail,'bookingdetail_count':bookingdetail_count })


@login_required()
def alquileresConductores(request):
    bookingdetail_count= Reservas.objects.filter(customer_detail=request.user)
    if request.user.groups.filter( name='Conductor').exists():
        return render(request, "dashboard/conductores/alquileres.html", { 'bookingdetail_count':bookingdetail_count })
    else:
        #return render(request, "dashboard/index.html", { 'bookingdetail_count':bookingdetail_count })
        return redirect('dashboard')

def pagosConductores(request):
    reserva=Reservas.objects.filter(customer_detail=request.user)
    
    if request.user.groups.filter( name='Conductor').exists():
        
        return render(request, "dashboard/conductores/pagos.html", { 'reserva':reserva})
    else:
        #return render(request, "dashboard/index.html", { 'bookingdetail_count':bookingdetail_count })
        return redirect('dashboard')


class reclamoconductor(LoginRequiredMixin, CreateView):
            model= ReclamoConductor
            form_class=ReclamoConductorForm
            template_name='dashboard/conductores/reclamosConductor.html'
            success_url= reverse_lazy('home')
        
            def form_valid(self, form):
                form.instance.user_id = self.request.user
                return super().form_valid(form)


def listaReclamos(request):
    form = ReclamoConductorForm(request.POST)
    if form.is_valid():
        form=form.save(commit = False)
        form.user_id= request.user
        form.claim_status="Reclamo Recibido"
        form.save()
        messages.success(request, 'Reclamo recibido con exito')
        return redirect('misreclamos')
    reclamoconductorlist=ReclamoConductor.objects.filter(user_id=request.user)
    if request.user.groups.filter( name='Conductor').exists():
        return render(request, 'dashboard/conductores/lista-reclamos.html' ,{ 'reclamoconductorlist': reclamoconductorlist,'form':form})
    else:
        #return render(request, "dashboard/index.html", { 'bookingdetail_count':bookingdetail_count })
        return redirect('dashboard')


def profile(request):
    if request.method =="POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Informacion actualizada con exito')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        context={
            'form': form,
        }
        return render (request, 'dashboard/conductores/cuenta.html', context=context )


def userProfile(request): 
    form = UserProfileForm(request.POST if request.POST else None, instance= Profile.objects.get(user=request.user))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Informacion actualizada con exito1')
            return redirect('licencia')

    return render(request, 'dashboard/conductores/licencia.html', context={'form': form})



def verificaionPerfil(request):
    return render (request, 'dashboard/conductores/verificacion.html' )

def verificacionPropietario(request):
    return render(request, 'dashboard/propietarios/verificacionPropietarios.html')

def misAutos(request):
    return render(request, 'dashboard/propietarios/mis-autos.html')

def infoPropietarios(request):
    form = UserProfileForm(request.POST if request.POST else None, instance= Profile.objects.get(user=request.user))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Informacion actualizada con exito')
            return redirect('infoPropietarios')

    return render(request, 'dashboard/propietarios/cuenta.html', context={'form': form})

