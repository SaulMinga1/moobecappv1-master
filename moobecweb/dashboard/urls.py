from unicodedata import name
from django.urls import path
from dashboard import views
from .views import reclamoconductor, listaReclamos, profile, verificaionPerfil, userProfile, verificacionPropietario, misAutos, infoPropietarios


urlpatterns =[
    path('', views.dashboard , name="dashboard"),
    #CONDUCTORES
    path('mis-alquileres/', views.alquileresConductores, name="alquileresConductores"),
    path('mis-pagos/', views.pagosConductores , name="pagosConductores"),
    path('reclamos-conductor/', reclamoconductor.as_view(), name='reclamo-conductor'),
    path('mis-reclamos/', views.listaReclamos , name='misreclamos'),
    path('perfil/licencia/', views.userProfile, name='licencia'),
    path('perfil/verificacion/', views.verificaionPerfil, name='verificacion'),
    #CUENTA-PERFIL-CONDUCTORES-PROPIETARIOS
    path('perfil/editar/', views.profile, name='profile'),
    #PROPIETARIOS
    path('propietarios/perfil/verificacion/', views.verificacionPropietario, name='verificacion-propietarios'),
    path('propietarios/misautos/', views.misAutos, name='misautos'),
    path('propietarios/perfil/infopropietarios/', views.infoPropietarios, name='infoPropietarios'),

    

]