from django.shortcuts import render
from django.http import HttpResponse

def gasolina(request):
   # return HttpResponse("FORMULARIO DE GASOLINA, PATRICIO")
    return render(request, 'gasolina/gasolina.html')    

