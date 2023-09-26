from faulthandler import disable
from random import choices
from secrets import choice
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from carrental.models import ReclamoConductor
from django import forms
from django.forms import ModelForm
from .models import Profile
import pytz

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))
    password1 = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'form-control','placeholder':'Confirm yor password'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))

    class Meta:
        model =User
        fields =('username', 'first_name','last_name', 'email','password1', 'password2')

class ReclamoConductorForm(ModelForm):
    class Meta:
        model=ReclamoConductor
        #fields= "__all__" todos los campos del form
        
        
        fields = (      
                    'incident_type',
                    'cost',
                    )

        widgets  = {
                    
                    'incident_type': forms.Textarea(attrs={'class': 'form-control','placeholder':'Descripcion del evento'}),
                    'cost': forms.NumberInput (attrs={'class': 'form-control','placeholder':'Costo'}),
                    } 


class ProfileForm(UserChangeForm):
    

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
        )
        widgets  = {
                    'username': forms.TextInput(attrs={'class': 'form-control disable-imput', 'readonly':'readonly','placeholder':'Nombre de Usuario'}),
                    'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
                    'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly':'readonly','placeholder':'Email'}),

                    }

class UserProfileForm(forms.ModelForm):
    

    class Meta:
        model=Profile
        fields=(
            
            'DOB',
            'birth_place',
            'licencia_conductor',
            'fecha_emision_licencia',
            'pais_emision_licencia',
            'numero_telefono',
            'direccion',
            'ciudad',
            'pais',
            'bio',
        )
        widgets  = {
                
                    'DOB': forms.DateInput(attrs={'class': 'form-control','placeholder':'AAAA-MM-DD',  'pattern':'/\d{4 } - (0[1-9]|1[0-2]) - (0[1-9]|[12][0-9]|3[01])/'  }),
                    'birth_place':forms.DateInput(attrs={'class': 'form-control','placeholder':'Lugar de nacimiento'}),
                    'licencia_conductor':forms.TextInput(attrs={'class': 'form-control','placeholder':'Numero de licencia', 'pattern':'/\d{4 } - (0[1-9]|1[0-2]) - (0[1-9]|[12][0-9]|3[01])/'}),
                    'fecha_emision_licencia':forms.DateInput(attrs={'class': 'form-control','placeholder':'AAAA-MM-DD'}),
                    'pais_emision_licencia':forms.Select(attrs={'class': 'form-control','placeholder':'Pais de emision'}, choices=pytz.country_names.items()),
                    'numero_telefono':forms.TextInput(attrs={'class': 'form-control','placeholder':'Numero de telefono'}),
                    'direccion':forms.TextInput(attrs={'class': 'form-control','placeholder':'Direccion'}),
                    'ciudad':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ciudad'}),
                    'pais':forms.Select(attrs={'class': 'form-control','placeholder':'Pais','blank':'blank'}, choices=pytz.country_names.items()),
                    'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'Cuentanos un poco sobre ti: como por ejemplo, en que hotel te vas a quedar, las ciudades q visitaras, etc','blank':'blank'}),
        
                    }
        