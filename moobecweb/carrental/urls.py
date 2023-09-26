from django.urls import path
from carrental import views

urlpatterns =[
    path('', views.rentals , name="rentals"),
]