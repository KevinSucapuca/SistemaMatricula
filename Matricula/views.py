from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def Docente(request):
    
    return render(request, 'admin-docente.html')

def ListaDocente(request):
    
    return render(request, 'admin-lista-docente.html')

def BuscarDocente(request):
    
    return render(request, 'admin-buscar-docente.html')