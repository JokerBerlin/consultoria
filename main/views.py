from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
import json
from django.shortcuts import redirect

from .models import Region, Asesor



# Create your views here.
def mostrarContacto(request):
    context = {}
    return render(request,'main/contacto/contacto.html',context)

def mostrarAsesores(request, id_region):
    print(id_region)
    asesores = Asesor.objects.filter(region = id_region)
    regiones = Region.objects.filter(activo=True)
    context = {'asesores':asesores,'regiones':regiones,}
    return render(request,'main/asesores/asesores.html',context)

def mostrarAsesor(request):
    context = {}
    return render(request,'main/asesor/asesor.html',context)

def mostrarIndex(request):
    context = {}
    return render(request,'main/index/index.html',context)

def mostrarNosotros(request):
    context = {}
    return render(request,'main/nosotros/nosotros.html',context)

def mostrarServicios(request):
    context = {}
    return render(request,'main/servicios/servicios.html',context)

def registrarAsesor(request):
    regiones = Region.objects.filter(activo=True)
    context = {'regiones':regiones,}
    return render(request,'asesor/registrar.html',context)

def registarAsesorAPI(request):
    if request.method == 'POST':
        data = request.POST, request.FILES
        # print(data[0]['nombre'])
        region = Region.objects.get(id=data[0]['region'])
        asesor = Asesor(
            nombre = data[0]['nombre'],
            tipo_documento =data[0]['tipo_documento'],
            documento = data[0]['documento'],
            telefono = data[0]['telefono'],
            correo = data[0]['correo'],
            funcion = data[0]['funcion'],
            precio = data[0]['precio'],
            region = region,
            foto = data[1]['foto'],
            
            )
        asesor.save()
        
        return redirect('/asesor/registrar/')
