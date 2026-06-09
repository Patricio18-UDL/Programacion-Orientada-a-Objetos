from django.shortcuts import render
from django.http import HttpResponse

def usuario(request):
   # return HttpResponse("FORMULARIO DE USUARIO, PATRICIO")
    return render(request, 'usuario/usuario.html')    
