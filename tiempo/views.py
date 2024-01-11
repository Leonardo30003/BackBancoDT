from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import ServicioSerializers,CuentaSerializers,UsuarioSerializers,RolSerializers,CategoriaSerializers,InteresSerializers,CalificacionSerializers,TransaccionSerializers
from .models import Rol,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo,Usuario

# Create your views here.
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializers

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializers

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class InteresViewSet(viewsets.ModelViewSet):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializers

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializers

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = TransaccionTiempo.objects.all()
    serializer_class = TransaccionSerializers

