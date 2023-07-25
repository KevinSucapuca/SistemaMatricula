from django.shortcuts import render,redirect, get_object_or_404
from .models import Docente, Alumno, Ciclo, Curso, CicloCurso
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
def home(request):
    
    return render(request, 'home.html')
#Docente
def RegistrarDocente(request):
    dniExiste = False

    if request.method == 'POST':
        dniRegistro = request.POST['dni-registro']
        nombreRegistro = request.POST['nombre-registro']
        apellidoRegistro = request.POST['apellido-registro']
        telefonoRegistro = request.POST['telefono-registro']
        direccionRegistro = request.POST['direccion-registro']

        # Verificar si el Dni ya existe
        dniExiste = Docente.objects.filter(dni__iexact=dniRegistro).exists()

        # Si el Dni ya existe, mostrar SweetAlert and retornar a la misma página
        if dniExiste:
            messages.error(request, "El Docente ya existe")
        # Si el Dni no existe, crear el objeto Docente
        else:
            Docente.objects.create(dni=dniRegistro, nombre=nombreRegistro, apellido=apellidoRegistro, telefono=telefonoRegistro, direccion=direccionRegistro)
            messages.success(request, "Docente Registrado Correctamente")
            return redirect('admin-docente')

    return render(request, 'admin-docente.html', {'dniExiste': dniExiste})
    

def ListaDocente(request):
    listaDocente = Docente.objects.all().order_by('apellido')
    paginator = Paginator(listaDocente, 10)
    pagina = request.GET.get('page') or 1
    listaDocente = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaDocente.paginator.num_pages + 1)
    context = {
        'listaDocente': listaDocente,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    return render(request, 'admin-lista-docente.html', context)

def BuscarDocente(request):
    if 'buscar' in request.GET:
        buscarDocente = request.GET['buscar']
        listabusquedaDocente = Docente.objects.filter(
            Q(dni__icontains=buscarDocente) |
            Q(apellido__icontains=buscarDocente)
        ).order_by('apellido')
    else:
        listabusquedaDocente = Docente.objects.all().order_by('apellido')

    paginator = Paginator(listabusquedaDocente, 10)
    pagina = request.GET.get('page') or 1
    listabusquedaDocente = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listabusquedaDocente.paginator.num_pages + 1)

    context = {
        'listabusquedaDocente': listabusquedaDocente,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }

    return render(request, 'admin-buscar-docente.html', context)

def EditarDocente(request, docente_id):
    docente = get_object_or_404(Docente, pk=docente_id)
    context = {
        'docente': docente,
    }
    return render(request, 'admin-editar-docente.html', context)

def GuardarEditarDocente(request, docente_id):
    docente = get_object_or_404(Docente, pk=docente_id)

    if request.method == 'POST':
        dniRegistro = request.POST['dni-registro']
        nombreRegistro = request.POST['nombre-registro']
        apellidoRegistro = request.POST['apellido-registro']
        telefonoRegistro = request.POST['telefono-registro']
        direccionRegistro = request.POST['direccion-registro']

        docente.dni = dniRegistro
        docente.nombre = nombreRegistro
        docente.apellido = apellidoRegistro
        docente.telefono = telefonoRegistro
        docente.direccion = direccionRegistro
        docente.save()

        messages.success(request, "Docente actualizado correctamente.")
        return redirect('lista-docente')

    # Redireccionar a la vista de detalles del docente actualizado
    return redirect('lista-docente', docente_id=docente.id)


def EliminarDocente(request,docente_id):
    DocenteEliminar = Docente.objects.get(pk=docente_id)
    DocenteEliminar.delete()
    messages.success(request, "Docente eliminado correctamente.")
    return redirect('/lista-docente')


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

#Ciclo
def Ciclo(request):
    
    return render(request, 'admin-ciclo.html')

def ListaCiclo(request):
    
    return render(request, 'admin-lista-ciclo.html')

def BuscarCiclo(request):
    
    return render(request, 'admin-buscar-ciclo.html')

#GestionarCiclo
def GestionarCiclo(request):
    
    return render(request, 'admin-gestionar-ciclo.html')

def ListaGestionarCiclo(request):
    
    return render(request, 'admin-lista-gestionar-ciclo.html')

def BuscarGestionarCiclo(request):
    
    return render(request, 'admin-buscar-gestionar-ciclo.html')

#Matrícula
def Matricula(request):
    
    return render(request, 'admin-matricula.html')

def ListaMatricula(request):
    
    return render(request, 'admin-lista-matricula.html')

def BuscarMatricula(request):
    
    return render(request, 'admin-buscar-matricula.html')