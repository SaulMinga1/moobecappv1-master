from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Vehicle

# create a model form based

class VehicleForm(ModelForm):
    class Meta:
        model=Vehicle
        #fields= "__all__" todos los campos del form
        fields = (
                    'car_model',
                    'car_year',
                    'car_plate_number',
                    'car_proposal_rate',
                    'car_owner_id')

        widgets  = {
                    'car_model': forms.TextInput(attrs={'class': 'form-control','placeholder':'Modelo'}),
                    'car_year': forms.NumberInput(attrs={'class':'form-control','placeholder':'Year'}),
                    'car_plate_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Placa'}),
                    'car_proposal_rate': forms.NumberInput(attrs={'class': 'form-control','placeholder':'precio que te gustaria alquilar tu auto'}),
                    'car_owner_id': forms.TextInput(attrs={'class': 'form-control','placeholder':'Owner'})
                    }   
   

class SearchCarForm(forms.Form):
    check_in=forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M"])
    check_out=forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M"])