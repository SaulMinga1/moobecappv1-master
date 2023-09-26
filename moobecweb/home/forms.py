from random import choices
from secrets import choice
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SolicitudPropietario
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email','id':'validationusername'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))
    password1 = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'form-control','placeholder':'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput (attrs={'class': 'form-control','placeholder':'Confirm yor password'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))


    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario no disponible')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email usado por otra cuenta')
        return email


    class Meta:
        model =User
        fields =('username', 'first_name','last_name', 'email','password1', 'password2')
    

yearchoices=[
            ('2016', '2016 '),
            ('2017', '2017 '),
            ('2018', '2018 '),
            ('2019', '2019 '),
            ('2020', '2020 '),
            ('2021', '2021 '),
            ('2022', '2022 '),
            ('2023', '2023 '),
]

km_range=[
            ('0-15000', '0-15000 km'),
            ('15-50000', '15-50000 km'),
            ('50-100000', '50-100000 km'),
            ('+100000', '+100000 km'),
]


class SolicitudPropietarioForm(ModelForm):
    class Meta:
        model=SolicitudPropietario
        #fields= "__all__" todos los campos del form
        fields = (
                    'brand',
                    'model',
                    'year',
                    'mileage',
                    'city',
                    'owner_id',
                    )

        widgets  = {
                    'brand': forms.TextInput(attrs={'class': 'form-control','placeholder':'Marca'}),
                    'model': forms.TextInput(attrs={'class': 'form-control','placeholder':'Modelo'}),
                    'year': forms.Select(attrs={'class': 'form-control','placeholder':'Anio'}, choices=yearchoices),
                    'mileage': forms.Select(attrs={'class': 'form-control','placeholder':'Kilometros'}, choices=km_range),
                    'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ciudad'}),
                    'owner_id': forms.TextInput(attrs={'class': 'form-control', 'value': '' ,'id': 'elder', 'type':'hidden'})
                    #'car_owner_id': forms.TextInput(attrs={'class': 'form-control','placeholder':'Owner'})
                    }   
   

class SolicitudPropietarioForm2(ModelForm):
    class Meta:
        model=SolicitudPropietario
        #fields= "__all__" todos los campos del form
        fields = (
                    'brand',
                    'model',
                    'year',
                    'mileage',
                    'city',
                    )

        widgets  = {
                    'brand': forms.TextInput(attrs={'class': 'form-control','placeholder':'Mrca'}),
                    'model': forms.TextInput(attrs={'class': 'form-control','placeholder':'Modelo'}),
                    'year': forms.Select(attrs={'class': 'form-control','placeholder':'Anio'}, choices=yearchoices),
                    'mileage': forms.Select(attrs={'class': 'form-control','placeholder':'Kilometros'}, choices=km_range),
                    'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ciudad'}),
                    }   


     