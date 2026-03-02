from django.urls import path
from plantilla import views

urlpatterns = [
    path('', views.index, name='index'), #para la pagina principal no se rellenan las comillas del path y el NAME se llama INDEX
    path('plantilla/', views.plantilla, name='plantilla')
]