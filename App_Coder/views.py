from django.http import HttpResponse
from django.shortcuts import render

from App_Coder.models import Curso, Entregable, Estudiante, Profesor

# Create your views here.
def curso(self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>
    """)

def estudiante(self, nombre, apellido, email):
    estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
    estudiante.save()
    return HttpResponse(f"""
        <p>Estudiante: {estudiante.nombre} - Apellido: {estudiante.apellido} - Email {estudiante.email} agregado</p>
    """)

def profesor(self, nombre, apellido, email, profesion):
    profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
    profesor.save()
    return HttpResponse(f"""
        <p>Profesor: {profesor.nombre} - Apellido: {profesor.apellido} - Email {profesor.email} - Profesion {profesor.profesion} agregado</p>
    """)

def entregable(self, nombre, fechaDeEntrega, entregado):
    entregable = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)
    entregable.save()
    return HttpResponse(f"""
        <p>Entregable: {entregable.nombre} - Fecha de Entrega: {entregable.fechaDeEntrega} - Entregado {entregable.entregado} agregado</p>
    """)    