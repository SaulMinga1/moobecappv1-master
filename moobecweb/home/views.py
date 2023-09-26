from email import message
from email.headerregistry import Group
from pickle import FALSE
from pyexpat.errors import messages
from urllib import request
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy

from dashboard.views import profile
from .forms import RegisterUserForm, SolicitudPropietarioForm2
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import SolicitudPropietarioForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import SolicitudPropietario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.contrib import messages
from dashboard.models import Profile
from dashboard.forms import UserProfileForm
# Create your views here.

def home(request):
    return render(request, "home/index.html")

def faq(request):
    return render(request, "home/preguntas.html")



"""@login_required()
def anunicarauto(request):
    submitted=False
    if request.method == 'POST':
        form=SolicitudPropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:    
        form=SolicitudPropietarioForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, "home/alquilarauto.html",{'form':form, 'submitted': submitted})"""

class UserRegisterView(generic.CreateView):
    form_class= RegisterUserForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('dashboard')
    #success_message = " was created successfully" 

    @receiver(post_save,sender=User)#asignar grupo al registrarse
    def create_user_profile(sender,instance, created, **kwargs):
        if created:
            instance.groups.add(Group.objects.get(name='Conductor'))
    
 

            
            


#class anunciarauto(LoginRequiredMixin,CreateView):
class anunciarauto(CreateView):
    model=SolicitudPropietario
    form_class=SolicitudPropietarioForm2
    template_name='home/alquilerauto2.html'
    success_url= reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner_id = self.request.user
        return super().form_valid(form)
    
   

        