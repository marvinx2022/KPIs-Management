from django.urls import path
from gestion import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('analitica', views.analitica, name='Analytics'),
    path('paradas', views.paradas, name='Paradas'),
    path('datos', views.datos, name='Datos')
]

