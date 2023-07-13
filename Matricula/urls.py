from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('admin-docente/', views.Docente,name='admin-docente'),
    path('lista-docente/', views.ListaDocente,name='lista-docente'),
    path('buscar-docente/', views.BuscarDocente,name='buscar-docente'),
]