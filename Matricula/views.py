from django.shortcuts import render,redirect, get_object_or_404
from .models import Docente,Alumno,Ciclo,Curso,CicloCurso,Matricula
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q



def home(request):
    total_cursos = Curso.objects.all().count()
    total_docentes = Docente.objects.all().count()
    total_alumnos = Alumno.objects.all().count()
    total_matriculados = Matricula.objects.all().count()
    context = {
        'total_cursos': total_cursos,
        'total_docentes': total_docentes,
        'total_alumnos': total_alumnos,
        'total_matriculados': total_matriculados
    }
    return render(request, 'home.html', context)
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

def EliminarGestionarCiclo(request,gestionarcurso_id):
    GestionarCicloEliminar = CicloCurso.objects.get(pk=gestionarcurso_id)
    GestionarCicloEliminar.delete()
    messages.success(request, "Curso del ciclo eliminado correctamente.")
    return redirect('lista-gestionar-ciclo')

#Matrícula
def BuscarAlumnosAMatricular(request):
    ciclos = Ciclo.objects.all()
    buscarAlumno = request.GET.get('buscar', '').strip()

    if buscarAlumno:
        listabusquedaAlumno = Alumno.objects.filter(
            Q(dni__icontains=buscarAlumno) |
            Q(apellido__icontains=buscarAlumno)
        ).order_by('apellido')
    else:
        listabusquedaAlumno = Alumno.objects.all().order_by('apellido')
    
    
    context = {
        'listabusquedaAlumno': listabusquedaAlumno,
        'ciclos': ciclos,
        
    }
    return render(request, 'admin-matricula.html', context)

def RegistrarMatricula(request):
    alumnos = Alumno.objects.all()
    ciclos = Ciclo.objects.all()
    listabusquedaAlumno = []
    alumno_id = None

    if 'buscar' in request.GET:
        buscarAlumno = request.GET['buscar']
        listabusquedaAlumno = Alumno.objects.filter(
            Q(dni__icontains=buscarAlumno) |
            Q(apellido__icontains=buscarAlumno)
        ).order_by('apellido')
        if listabusquedaAlumno.exists():
            alumno_id = listabusquedaAlumno[0].id  # Obtenemos el ID del alumno buscado
    
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        fecha = request.POST.get('fecha-reg')
        alumno_id = request.POST.get('alumno-reg')
        turno = request.POST.get('turno-reg')
        modalidad = request.POST.get('modalidad-reg')
        ciclo_id = request.POST.get('ciclo-reg')
        
        if not alumno_id:
            messages.error(request, "Debes seleccionar un Alumno.")
            return render(request, 'admin-matricula.html', {'alumnos': alumnos,'ciclos': ciclos})
        if not ciclo_id:
            messages.error(request, "Debes seleccionar un Ciclo.")
            return render(request, 'admin-matricula.html', {'alumnos': alumnos,'ciclos': ciclos})
        if not turno or turno == 'opcion1':
            messages.error(request, "Debes seleccionar un turno válido.")
            return render(request, 'admin-matricula.html', {'alumnos': alumnos,'ciclos': ciclos})
        if not modalidad or modalidad == 'opcion1':
            messages.error(request, "Debes seleccionar una modalidad válida.")
            return render(request, 'admin-matricula.html', {'alumnos': alumnos,'ciclos': ciclos})
        
        # Obtener las instancias de Alumno y Ciclo asociadas a los IDs
        alumno = Alumno.objects.get(pk=alumno_id)
        ciclo = Ciclo.objects.get(pk=ciclo_id)
        
        # Verificar si el alumno está matriculado
        if Matricula.objects.filter(alumnoMatricula=alumno).exists():
            messages.error(request, "El Alumno ya está matriculado")
            return render(request, 'admin-matricula.html', {'alumnos': alumnos,'ciclos': ciclos})

        # Crear una nueva instancia de Matricula y guardarla en la base de datos
        matricula = Matricula(fecha=fecha, alumnoMatricula=alumno, cicloMatricula=ciclo, turno=turno, modalidad=modalidad)

        matricula.save()

        
        messages.success(request, "Matrícula registrada correctamente.")
        return redirect('lista-matricula')
    context = {
        'alumnos': alumnos,
        'ciclos': ciclos,
        'listabusquedaAlumno': listabusquedaAlumno,
        'alumno_id': alumno_id,
        
    }

    return render(request, 'admin-matricula.html', context)


def ListaMatricula(request):
    listaMatricula = Matricula.objects.all().order_by('-id')
    paginator = Paginator(listaMatricula, 10)
    pagina = request.GET.get('page') or 1
    listaMatricula = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaMatricula.paginator.num_pages + 1)

    # Creamos un diccionario para almacenar los cursos asociados a cada ciclo
    cursos_por_ciclo = {}

    for matricula in listaMatricula:
        ciclo = matricula.cicloMatricula
        # Filtramos los CicloCurso asociados al ciclo actual
        cursos = CicloCurso.objects.filter(ciclo=ciclo)
        cursos_por_ciclo[ciclo.id] = cursos

    context = {
        'listaMatricula': listaMatricula,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'cursos_por_ciclo': cursos_por_ciclo  # Pasamos el diccionario al contexto
    }

    return render(request, 'admin-lista-matricula.html', context)

def BuscarMatricula(request):
    
    buscarAlumno = request.GET.get('buscar', '')
    

    listabusquedaAlumno = Alumno.objects.filter(
        Q(dni__icontains=buscarAlumno) |
        Q(apellido__icontains=buscarAlumno)
    ).order_by('apellido')

    listaMatricula = Matricula.objects.filter(
        alumnoMatricula__in=listabusquedaAlumno
    ).order_by('-id')

    paginator = Paginator(listaMatricula, 10)
    pagina = request.GET.get('page') or 1
    listaMatricula = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, listaMatricula.paginator.num_pages + 1)

    cursos_por_ciclo = {}
    for matricula in listaMatricula:
        ciclo = matricula.cicloMatricula
        cursos = CicloCurso.objects.filter(ciclo=ciclo)
        cursos_por_ciclo[ciclo.id] = cursos

    context = {
        'listaMatricula': listaMatricula,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'cursos_por_ciclo': cursos_por_ciclo,
        'listabusquedaAlumno': listabusquedaAlumno,
        'buscarAlumno': buscarAlumno
    }

    return render(request, 'admin-buscar-matricula.html', context)

def EditarMatricula(request, matricula_id):
    editarMatricula = get_object_or_404(Matricula, pk=matricula_id)
    ciclos = Ciclo.objects.all()
    alumnos = Alumno.objects.all()

    context = {
        'editarMatricula': editarMatricula,
        'ciclos': ciclos,
        'alumnos': alumnos,
    }
    return render(request, 'admin-editar-matricula.html', context)

def GuardarEditarMatricula(request, matricula_id):
    editarMatricula = get_object_or_404(Matricula, pk=matricula_id)
    ciclos = Ciclo.objects.all()
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        fecha = request.POST.get('fecha-reg')
        nombre_ciclo_id = request.POST.get('ciclo-reg')
        alumno_id = request.POST.get('alumno-reg')
        turno = request.POST.get('turno-reg')
        modalidad = request.POST.get('modalidad-reg')
        

        if not nombre_ciclo_id:
            messages.error(request, "Debes seleccionar un ciclo.")
            return render(request, 'admin-editar-matricula.html', {'editarMatricula': editarMatricula, 'ciclos': ciclos, 'alumnos': alumnos})
        
        ciclo = Ciclo.objects.get(pk=nombre_ciclo_id)
        alumno = Alumno.objects.get(pk=alumno_id)

        # Si todo está bien, actualizamos la matricula
        editarMatricula.fecha = fecha
        editarMatricula.cicloMatricula = ciclo
        editarMatricula.alumnoMatricula = alumno
        editarMatricula.turno = turno
        editarMatricula.modalidad = modalidad 
        editarMatricula.save()

        messages.success(request, "Matricula actualizada correctamente.")
        return redirect('lista-matricula')

    return render(request, 'admin-editar-matricula.html', {'editarMatricula': editarMatricula, 'ciclos': ciclos, 'alumnos': alumnos})

def EliminarMatricula(request,matricula_id):
    MatriculaEliminar = Matricula.objects.get(pk=matricula_id)
    MatriculaEliminar.delete()
    messages.success(request, "Matrícula eliminada correctamente.")
    return redirect('lista-matricula')