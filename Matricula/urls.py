from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin-docente/', views.RegistrarDocente,name='admin-docente'),
    path('lista-docente/', views.ListaDocente,name='lista-docente'),
    path('buscar-docente/', views.BuscarDocente,name='buscar-docente'),
    path('editar-docente/<int:docente_id>/', views.EditarDocente, name='editar-docente'),
    path('editar-docente/<int:docente_id>/guardar/', views.GuardarEditarDocente, name='guardar-editar-docente'),
    path('eliminar-docente/<int:docente_id>/', views.EliminarDocente, name='eliminar-docente'),
    path('admin-alumno/', views.RegistrarAlumno,name='admin-alumno'),
    path('lista-alumno/', views.ListaAlumno,name='lista-alumno'),
    path('buscar-alumno/', views.BuscarAlumno,name='buscar-alumno'),
    path('editar-alumno/<int:alumno_id>/', views.EditarAlumno, name='editar-alumno'),
    path('editar-alumno/<int:alumno_id>/guardar/', views.GuardarEditarAlumno, name='guardar-editar-alumno'),
    path('eliminar-alumno/<int:alumno_id>/', views.EliminarAlumno, name='eliminar-alumno'),
    path('admin-curso/', views.RegistrarCurso,name='admin-curso'),
    path('lista-curso/', views.ListaCurso,name='lista-curso'),
    path('buscar-curso/', views.BuscarCurso,name='buscar-curso'),
    path('admin-ciclo/', views.Ciclo,name='admin-ciclo'),
    path('lista-ciclo/', views.ListaCiclo,name='lista-ciclo'),
    path('buscar-ciclo/', views.BuscarCiclo,name='buscar-ciclo'),
    path('admin-gestionar-ciclo/', views.GestionarCiclo,name='admin-gestionar-ciclo'),
    path('lista-gestionar-ciclo/', views.ListaGestionarCiclo,name='lista-gestionar-ciclo'),
    path('buscar-gestionar-ciclo/', views.BuscarGestionarCiclo,name='buscar-gestionar-ciclo'),
    path('admin-matricula/', views.Matricula,name='admin-Matricula'),
    path('lista-matricula/', views.ListaMatricula,name='lista-matricula'),
    path('buscar-matricula/', views.BuscarMatricula,name='buscar-matricula'),
    
]
