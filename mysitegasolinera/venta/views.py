from django.shortcuts import render
from django.http import HttpResponse

def venta(request):
   # return HttpResponse("FORMULARIO DE VENTA, PATRICIO")
    return render(request, 'venta/venta.html')    
