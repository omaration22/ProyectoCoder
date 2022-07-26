from django.urls import path

from App_Coder.views import curso, cursos, entregables, estudiante, inicio, lista_curso, profesores

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiante, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('entregables/', entregables, name="Entregables"),
]
