from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

lenguajes = ["Python", "C++", "PHP"]

# Request: Peticion
# HttpResponse: Respuesta en HTTP 

# Primera vista
def bienvenida(request): # Objeto de tipo request como primer argumento
    return HttpResponse("Bienvenid@ a su proyecto Django")

def sumarNumeros(request):
    numero_uno = 2
    numero_dos = 2
    suma = numero_uno + numero_dos
    resultado = "<h1>La suma de los dos números es: %s</h1>" %suma
    return HttpResponse(resultado)

def primeraPlantilla(request): 
    return render(request, 'primeraPlantilla.html', {"lenguajes" : lenguajes})

# Vista
def plantillaAgregarElemento(request):
    return render(request, 'agregarElemento.html')

# Logica de alamacenamiento
def agregarElemento(request):
    nuevo_elemento = request.POST.get('nuevo_elemento')
    lenguajes.append(nuevo_elemento)
    return redirect('primera_plantilla')  # Redirecciona a la página principal