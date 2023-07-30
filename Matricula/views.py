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
    listaCurso = Curso.objects.all().order_by('nombreCurso')
    paginator = Paginator(listaCurso, 10)
    pagina = request.GET.get('page') or 1
    listaCurso = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaCurso.paginator.num_pages + 1)
    context = {
        'listaCurso': listaCurso,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    
    return render(request, 'admin-lista-curso.html', context)

def BuscarCurso(request):
    if 'buscar' in request.GET:
        buscarCurso = request.GET['buscar']
        listaCurso = Curso.objects.filter(
            Q(nombreCurso__icontains=buscarCurso) |
            Q(docente__apellido__icontains=buscarCurso)
        ).order_by('nombreCurso')
    else:
        listaCurso = Curso.objects.all().order_by('nombreCurso')

    paginator = Paginator(listaCurso, 10)
    pagina = request.GET.get('page') or 1
    listaCurso = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaCurso.paginator.num_pages + 1)

    context = {
        'listaCurso': listaCurso,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    
    return render(request, 'admin-buscar-curso.html', context)

def EditarCurso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    docentes = Docente.objects.all()

    context = {
        'curso': curso,
        'docentes': docentes,
    }
    return render(request, 'admin-editar-curso.html', context)

def GuardarEditarCurso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    docentes = Docente.objects.all()

    if request.method == 'POST':
        nombre_curso = request.POST['nombrecurso-reg']
        vacantes = request.POST['vacantes-reg']
        docente_id = request.POST['direccion-reg']

        if not docente_id:
            messages.error(request, "Debes seleccionar un docente.")
            return render(request, 'admin-editar-curso.html', {'curso': curso, 'docentes': docentes})

        docente = get_object_or_404(Docente, pk=docente_id)

        curso.nombreCurso = nombre_curso
        curso.vacantes = vacantes
        curso.docente = docente

        curso.save()

        messages.success(request, "Curso actualizado correctamente.")
        return redirect('lista-curso')

    return render(request, 'admin-editar-curso.html', {'curso': curso, 'docentes': docentes})

def EliminarCurso(request,curso_id):
    CursoEliminar = Curso.objects.get(pk=curso_id)
    CursoEliminar.delete()
    messages.success(request, "Curso eliminado correctamente.")
    return redirect('/lista-curso')

#Ciclo
def RegistrarCiclo(request):
    if request.method == 'POST':
        # Obtener los datos del formulario enviado por el usuario
        nombre_ciclo = request.POST.get('numerociclo-reg')
        carrera = request.POST.get('direccion-reg')

        # Validar que se haya seleccionado una carrera
        if not carrera or carrera == 'opcion1':
            messages.error(request, "Debes seleccionar una carrera válida.")
            return redirect('admin-ciclo')

        # Crear el objeto Ciclo y guardarlo en la base de datos
        ciclo = Ciclo.objects.create(nombreCiclo=nombre_ciclo, carrera=carrera)
        messages.success(request, "Ciclo Registrado Correctamente.")
        return redirect('lista-ciclo')

    return render(request, 'admin-ciclo.html')

def ListaCiclo(request):
    listaCiclo = Ciclo.objects.all().order_by('-id')
    paginator = Paginator(listaCiclo, 10)
    pagina = request.GET.get('page') or 1
    listaCiclo = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaCiclo.paginator.num_pages + 1)
    context = {
        'listaCiclo': listaCiclo,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    
    return render(request, 'admin-lista-ciclo.html', context)

def BuscarCiclo(request):
    if 'buscar' in request.GET:
        buscarCiclo = request.GET['buscar']
        listaCiclo = Ciclo.objects.filter(
            Q(nombreCiclo__icontains=buscarCiclo) |
            Q(carrera__icontains=buscarCiclo)
        ).order_by('-id')
    else:
        listaCiclo = Ciclo.objects.all().order_by('-id')

    paginator = Paginator(listaCiclo, 10)
    pagina = request.GET.get('page') or 1
    listaCiclo = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaCiclo.paginator.num_pages + 1)

    context = {
        'listaCiclo': listaCiclo,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    
    return render(request, 'admin-buscar-ciclo.html', context)

def EditarCiclo(request, ciclo_id):
    ciclo = get_object_or_404(Ciclo, pk=ciclo_id)
    context = {
        'ciclo': ciclo,
    }
    return render(request, 'admin-editar-ciclo.html', context)

def GuardarEditarCiclo(request, ciclo_id):
    ciclo = get_object_or_404(Ciclo, pk=ciclo_id)

    if request.method == 'POST':
        nombre_ciclo = request.POST['nombreCiclo']
        carrera = request.POST['direccion-reg']
        
        # Validar que se haya seleccionado una carrera
        if not carrera or carrera == 'opcion1':
            messages.error(request, "Debes seleccionar una carrera válida.")
            return redirect('editar-ciclo', ciclo_id=ciclo_id)
        
        ciclo.nombreCiclo = nombre_ciclo
        ciclo.carrera = carrera
    
        ciclo.save()

        messages.success(request, "Ciclo actualizado correctamente.")
        return redirect('lista-ciclo')

    # Redireccionar a la vista de detalles del ciclo actualizado
    return redirect('lista-ciclo', ciclo_id=ciclo_id)

def EliminarCiclo(request,ciclo_id):
    CicloEliminar = Ciclo.objects.get(pk=ciclo_id)
    CicloEliminar.delete()
    messages.success(request, "Ciclo eliminado correctamente.")
    return redirect('/lista-ciclo')

#GestionarCiclo
def GestionarCiclo(request):
    ciclos = Ciclo.objects.all()
    cursos = Curso.objects.all()

    if request.method == 'POST':
        nombre_ciclo_id = request.POST.get('ciclo-reg')
        curso_id = request.POST.get('curso-reg')

        if not nombre_ciclo_id:
            messages.error(request, "Debes seleccionar un ciclo.")
            return render(request, 'admin-gestionar-ciclo.html', {'ciclos': ciclos, 'cursos': cursos})

        if not curso_id:
            messages.error(request, "Selecciona un curso válido.")
            return render(request, 'admin-gestionar-ciclo.html', {'ciclos': ciclos, 'cursos': cursos})

        ciclo = Ciclo.objects.get(pk=nombre_ciclo_id)
        curso = Curso.objects.get(pk=curso_id)

        # Verificar si el curso ya está asociado al ciclo
        if CicloCurso.objects.filter(ciclo=ciclo, curso=curso).exists():
            messages.error(request, "El curso ya está asociado a este ciclo.")
            return render(request, 'admin-gestionar-ciclo.html', {'ciclos': ciclos, 'cursos': cursos})

        # Verificar la cantidad de cursos asociados al ciclo
        cantidad_cursos = CicloCurso.objects.filter(ciclo=ciclo).count()
        if cantidad_cursos >= 5:
            messages.error(request, "El ciclo ya tiene el máximo de cursos permitidos (5).")
            return render(request, 'admin-gestionar-ciclo.html', {'ciclos': ciclos, 'cursos': cursos})

        # Si el curso no está duplicado y la cantidad de cursos es menor a 5, agregarlo al ciclo
        CicloCurso.objects.create(ciclo=ciclo, curso=curso)

        messages.success(request, "Curso agregado al ciclo correctamente.")
        return redirect('lista-gestionar-ciclo')

    context = {'ciclos': ciclos, 'cursos': cursos}
    return render(request, 'admin-gestionar-ciclo.html', context) 

def ListaGestionarCiclo(request):
    
    listaGestionarCiclo = CicloCurso.objects.all().order_by('-ciclo_id')
    paginator = Paginator(listaGestionarCiclo, 10)
    pagina = request.GET.get('page') or 1
    listaGestionarCiclo = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaGestionarCiclo.paginator.num_pages + 1)
    context = {
        'listaGestionarCiclo': listaGestionarCiclo,
        'paginas': paginas, 
        'pagina_actual': pagina_actual
        }
    
    return render(request, 'admin-lista-gestionar-ciclo.html', context)

def BuscarGestionarCiclo(request):
    if 'buscar' in request.GET:
        buscarGestionarCiclo = request.GET['buscar']
        listaGestionarCiclo = CicloCurso.objects.filter(
            Q(ciclo__nombreCiclo__icontains=buscarGestionarCiclo) |
            Q(curso__nombreCurso__icontains=buscarGestionarCiclo) |
            Q(ciclo__carrera__icontains=buscarGestionarCiclo)
        ).order_by('-ciclo_id')
    else:
        listaGestionarCiclo = CicloCurso.objects.all().order_by('-ciclo_id')

    paginator = Paginator(listaGestionarCiclo, 10)
    pagina = request.GET.get('page') or 1
    listaGestionarCiclo = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaGestionarCiclo.paginator.num_pages + 1)

    context = {
        'listaGestionarCiclo': listaGestionarCiclo,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
    }
    
    return render(request, 'admin-buscar-gestionar-ciclo.html', context)

def EditarGestionarCiclo(request, ciclo_id):
    ciclocurso = get_object_or_404(CicloCurso, pk=ciclo_id)
    ciclos = Ciclo.objects.all()
    cursos = Curso.objects.all()

    context = {
        'ciclocurso': ciclocurso,
        'ciclos': ciclos,
        'cursos': cursos,
    }
    return render(request, 'admin-editar-gestionar-ciclo.html', context)

def GuardarEditarGestionarCiclo(request, ciclo_id):
    ciclocurso = get_object_or_404(CicloCurso, pk=ciclo_id)
    ciclos = Ciclo.objects.all()
    cursos = Curso.objects.all()

    if request.method == 'POST':
        nombre_ciclo_id = request.POST.get('ciclo-reg')
        curso_id = request.POST.get('curso-reg')

        if not nombre_ciclo_id:
            messages.error(request, "Debes seleccionar un ciclo.")
            return render(request, 'admin-editar-gestionar-ciclo.html', {'ciclocurso': ciclocurso, 'ciclos': ciclos, 'cursos': cursos})

        if not curso_id:
            messages.error(request, "Selecciona un curso válido.")
            return render(request, 'admin-editar-gestionar-ciclo.html', {'ciclocurso': ciclocurso, 'ciclos': ciclos, 'cursos': cursos})

        ciclo = Ciclo.objects.get(pk=nombre_ciclo_id)
        curso = Curso.objects.get(pk=curso_id)

        
        # Verificar si el ciclo ya tiene 5 cursos asociados, pero permitir editar el curso
        if CicloCurso.objects.filter(ciclo=ciclo).count() > 5:
            ciclocurso.ciclo = ciclo
            ciclocurso.curso = curso
            ciclocurso.save()
            messages.success(request, "Curso actualizado correctamente.")
            return redirect('lista-gestionar-ciclo')

        # Si el curso ya está asociado a este ciclo
        if CicloCurso.objects.filter(ciclo=ciclo, curso=curso).exists():
            messages.info(request, "El curso ya está asociado a este ciclo.")
            return render(request, 'admin-editar-gestionar-ciclo.html', {'ciclocurso': ciclocurso, 'ciclos': ciclos, 'cursos': cursos})

        # Si todo está bien, actualizamos el ciclo y el curso en el objeto CicloCurso
        ciclocurso.ciclo = ciclo
        ciclocurso.curso = curso
        ciclocurso.save()

        messages.success(request, "CicloCurso actualizado correctamente.")
        return redirect('lista-gestionar-ciclo')

    return render(request, 'admin-editar-gestionar-ciclo.html', {'ciclocurso': ciclocurso, 'ciclos': ciclos, 'cursos': cursos})



#Matrícula
def Matricula(request):
    
    return render(request, 'admin-matricula.html')

def ListaMatricula(request):
    
    return render(request, 'admin-lista-matricula.html')

def BuscarMatricula(request):
    
    return render(request, 'admin-buscar-matricula.html')