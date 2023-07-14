from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin-docente/', views.Docente,name='admin-docente'),
    path('lista-docente/', views.ListaDocente,name='lista-docente'),
    path('buscar-docente/', views.BuscarDocente,name='buscar-docente'),
    path('admin-alumno/', views.Alumno,name='admin-alumno'),
    path('lista-alumno/', views.ListaAlumno,name='lista-alumno'),
    path('buscar-alumno/', views.BuscarAlumno,name='buscar-alumno'),
    path('admin-curso/', views.Curso,name='admin-curso'),
    path('lista-curso/', views.ListaCurso,name='lista-curso'),
    path('buscar-curso/', views.BuscarCurso,name='buscar-curso'),
    
]