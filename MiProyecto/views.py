from django.http import HttpResponse
from django.shortcuts import render

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
    lenguajes = ["Python", "C++", "PHP"]
    return render(request, 'primeraPlantilla.html', {"lenguajes" : lenguajes})

