from django.shortcuts import render
from plantilla import models as mod
# Create your views here.

def index(request):
    return render(request, 'index.html')

def plantilla(request):
    servicio = mod.ServicioPlantilla()
    listaHosp = servicio.getListaHospitales()
    if ('cajaHosp' in request.POST):
        hosp_cod = int(request.POST['cajaHosp'])
#        nombre = servicio.getNombreHospital(hosp_cod)
        lista = servicio.getPlantilla(hosp_cod)
        informacion = {
            "plantilla": lista,
            "hospitales": listaHosp,
 #           "nombre": nombre
        }
        return render(request, 'plantilla.html', informacion)
    else:
        informacion = {
            "hospitales": listaHosp
        }
        return render(request, 'plantilla.html', informacion)