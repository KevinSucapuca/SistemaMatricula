from django.shortcuts import render,redirect, get_object_or_404
from .models import Docente,Alumno,Ciclo,Curso,CicloCurso
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
def RegistrarAlumno(request):
    DniAlumnoExiste = False

    if request.method == 'POST':
        dniRegistro = request.POST['dni-registro']
        nombreRegistro = request.POST['nombre-registro']
        apellidoRegistro = request.POST['apellido-registro']
        telefonoRegistro = request.POST['telefono-registro']
        direccionRegistro = request.POST['direccion-registro']

        # Verificar si el Dni ya existe
        DniAlumnoExiste = Alumno.objects.filter(dni__iexact=dniRegistro).exists()

        # Si el Dni ya existe, mostrar SweetAlert and retornar a la misma página
        if DniAlumnoExiste:
            messages.error(request, "El Estudiante ya existe")
        # Si el Dni no existe, crear el objeto Alumno
        else:
            Alumno.objects.create(dni=dniRegistro, nombre=nombreRegistro, apellido=apellidoRegistro, telefono=telefonoRegistro, direccion=direccionRegistro)
            messages.success(request, "Estudiante Registrado Correctamente")
            return redirect('admin-alumno')
    context ={
            'DniAlumnoExiste': DniAlumnoExiste,
            }
    return render(request, 'admin-alumno.html', context) 

def ListaAlumno(request):
    listaAlumno = Alumno.objects.all().order_by('apellido')
    paginator = Paginator(listaAlumno, 10)
    pagina = request.GET.get('page') or 1
    listaAlumno = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaAlumno.paginator.num_pages + 1)
    context = {
        'listaAlumno': listaAlumno,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    
    return render(request, 'admin-lista-alumno.html', context)

def BuscarAlumno(request):
    if 'buscar' in request.GET:
        buscarAlumno = request.GET['buscar']
        listabusquedaAlumno = Alumno.objects.filter(
            Q(dni__icontains=buscarAlumno) |
            Q(apellido__icontains=buscarAlumno)
        ).order_by('apellido')
    else:
        listabusquedaAlumno = Alumno.objects.all().order_by('apellido')

    paginator = Paginator(listabusquedaAlumno, 10)
    pagina = request.GET.get('page') or 1
    listabusquedaAlumno = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listabusquedaAlumno.paginator.num_pages + 1)

    context = {
        'listabusquedaAlumno': listabusquedaAlumno,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    
    return render(request, 'admin-buscar-alumno.html', context)

def EditarAlumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    context = {
        'alumno': alumno,
    }
    return render(request, 'admin-editar-alumno.html', context)

def GuardarEditarAlumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)

    if request.method == 'POST':
        dniRegistro = request.POST['dni-registro']
        nombreRegistro = request.POST['nombre-registro']
        apellidoRegistro = request.POST['apellido-registro']
        telefonoRegistro = request.POST['telefono-registro']
        direccionRegistro = request.POST['direccion-registro']

        alumno.dni = dniRegistro
        alumno.nombre = nombreRegistro
        alumno.apellido = apellidoRegistro
        alumno.telefono = telefonoRegistro
        alumno.direccion = direccionRegistro
        alumno.save()

        messages.success(request, "Alumno actualizado correctamente.")
        return redirect('lista-alumno')

    # Redireccionar a la vista de detalles del alumno actualizado
    return redirect('lista-alumno', alumno_id=alumno.id)

def EliminarAlumno(request,alumno_id):
    AlumnoEliminar = Alumno.objects.get(pk=alumno_id)
    AlumnoEliminar.delete()
    messages.success(request, "Estudiante eliminado correctamente.")
    return redirect('/lista-alumno')

#Curso
def RegistrarCurso(request):
    docentes = Docente.objects.all()  # Obtener todos los docentes de la base de datos

    if request.method == 'POST':
        # Obtener los datos del formulario enviado por el usuario
        nombre_curso = request.POST.get('nombrecurso-reg')
        vacantes_str = request.POST.get('vacantes-reg')
        docente_id = request.POST.get('direccion-reg')

        # Validar que se haya seleccionado un docente
        if not docente_id:
            messages.error(request, "Debes seleccionar un docente.")
            return render(request, 'admin-curso.html', {'docentes': docentes})

        # Validar que el campo de "Vacantes" no esté vacío
        if not vacantes_str:
            messages.error(request, "El campo Vacantes no puede estar vacío.")
            return render(request, 'admin-curso.html', {'docentes': docentes})

        # Convertir el campo de "Vacantes" a entero
        try:
            vacantes = int(vacantes_str)
        except ValueError:
            messages.error(request, "El valor de Vacantes debe ser un número entero válido.")
            return render(request, 'admin-curso.html', {'docentes': docentes})

        try:
            # Buscar el docente seleccionado por su ID
            docente = Docente.objects.get(pk=docente_id)

            # Crear un nuevo objeto Curso y guardar en la base de datos
            nuevo_curso = Curso(nombreCurso=nombre_curso, vacantes=vacantes, docente=docente)
            nuevo_curso.save()

            messages.success(request, "Curso agregado correctamente.")
            return redirect('lista-curso')
        except Docente.DoesNotExist:
            # Si el docente no existe, manejar el error y mostrar mensaje de error
            messages.error(request, "El docente no existe.")
            return render(request, 'admin-curso.html', {'docentes': docentes})

    context = {'docentes': docentes}
    return render(request, 'admin-curso.html', context)


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