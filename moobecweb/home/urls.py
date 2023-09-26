from django.urls import path, include
from home import views
from .views import UserRegisterView, anunciarauto


urlpatterns =[
    path('', views.home , name="home"),
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('accounts/',include("django.contrib.auth.urls")),
    path('preguntas/', views.faq , name="preguntas"),
    #path('alquilar-mi-auto/', views.anunicarauto, name='anunciarauto'),
    path('alquilar/',  anunciarauto.as_view()  , name='anunciarauto'),
]