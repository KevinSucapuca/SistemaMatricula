from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'home.html')
#Docente
def Docente(request):
    
    return render(request, 'admin-docente.html')

def ListaDocente(request):
    
    return render(request, 'admin-lista-docente.html')

def BuscarDocente(request):
    
    return render(request, 'admin-buscar-docente.html')

#Alumno
def Alumno(request):
    
    return render(request, 'admin-alumno.html')

def ListaAlumno(request):
    
    return render(request, 'admin-lista-alumno.html')

def BuscarAlumno(request):
    
    return render(request, 'admin-buscar-alumno.html')

#Curso
def Curso(request):
    
    return render(request, 'admin-curso.html')

def ListaCurso(request):
    
    return render(request, 'admin-lista-curso.html')

def BuscarCurso(request):
    
    return render(request, 'admin-buscar-curso.html')

