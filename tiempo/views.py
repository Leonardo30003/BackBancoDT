from django.shortcuts import render

from .serializer import ServicioSerializers,CuentaSerializers,UsuarioSerializers,RolSerializers,CategoriaSerializers,InteresSerializers,CalificacionSerializers,TransaccionSerializers,CanalUsuarioSerializers, CanalMensajeSerializers, CanalSerializers
from .models import Rol,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo,Usuario,CanalUsuario, CanalMensaje, Canal

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import action

#from django.http import QueryDict


# Create your views here.
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializers
    def buscar_por_cuenta(self, request, *args, **kwargs):
        cuenta = request.query_params.get('cuenta')  # Obtener el parámetro de consulta 'cuenta'
        tipo = request.query_params.get('rolChoices')
        print("Correo proporcionado:", cuenta)
        if cuenta:
            try:
                # usuario = Usuario.objects.get(email=cuenta)
                print(Servicio.objects.filter(propietario=cuenta).__dict__)
                servicios = Servicio.objects.filter(Q(propietario=cuenta) & Q(ROL_CHOICES = tipo))
                # servicios = Servicio.objects.filter(Q(propietario=cuenta))
                print("Servicios encontrado:", servicios)
                for servicio in servicios:
                    print(servicio.propietario,"", servicio.ROL_CHOICES)
                serializer = self.get_serializer(servicios,many=True)
                return Response(serializer.data)
            except Servicio.DoesNotExist:
                print("Servicios no encontrado")
                return Response("Servicios no encontrado", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Se requiere el parámetro 'cuenta'", status=status.HTTP_400_BAD_REQUEST)


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializers

    
    def buscarCuentaUsuario(self, request, *args, **kwargs):
        cuenta = request.query_params.get('usuario')  # Obtener el parámetro de consulta 'cuenta'
        print("cuenta proporcionado:", cuenta)
        
        if cuenta:
            try:
                cuenta_obj = Cuenta.objects.get(usuario=cuenta)
                print("Cuenta encontrado:", cuenta_obj)
                serializer = self.get_serializer(cuenta_obj)
                return Response(serializer.data)
            except Cuenta.DoesNotExist:
                print("Cuenta no encontrada")
                return Response("Cuenta no encontrada", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Se requiere el parámetro 'usuario'", status=status.HTTP_400_BAD_REQUEST)
        
    def buscarCuentaIdCuenta(self, request, *args, **kwargs):
        cuenta = request.query_params.get('idCuenta')  # Obtener el parámetro de consulta 'usuario'
        print("Usuario proporcionado:", cuenta)
        
        if cuenta:
            try:
                cuenta_obj = Cuenta.objects.get(id=cuenta)
                print("Cuenta encontrado:", cuenta_obj)
                serializer = self.get_serializer(cuenta_obj)
                return Response(serializer.data)
            except Cuenta.DoesNotExist:
                print("Cuenta no encontrada")
                return Response("Cuenta no encontrada", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Se requiere el parámetro 'usuario'", status=status.HTTP_400_BAD_REQUEST)



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crear una copia mutable
        password = mutable_data.get('password')
        if password:
            mutable_data['password'] = make_password(password)
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        mutable_data = request.data.copy()  # Crear una copia mutable
        password = mutable_data.get('password')
        if password:
            mutable_data['password'] = make_password(password)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=mutable_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def buscar_por_correo(self, request, *args, **kwargs):
        correo = request.query_params.get('correo')  # Obtener el parámetro de consulta 'correo'
        print("Correo proporcionado:", correo)
        if correo:
            try:
                # usuario = Usuario.objects.get(email=correo)
                usuario = Usuario.objects.filter(username=correo).first()
                print("Usuario encontrado:", usuario)
                serializer = self.get_serializer(usuario)
                return Response(serializer.data)
            except Usuario.DoesNotExist:
                print("Usuario no encontrado")
                return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Se requiere el parámetro 'correo'", status=status.HTTP_400_BAD_REQUEST)



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

#views chat
class CanalUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CanalUsuario.objects.all()
    serializer_class = CanalUsuarioSerializers

class CanalMensajeViewSet(viewsets.ModelViewSet):
    queryset = CanalMensaje.objects.all()
    serializer_class = CanalMensajeSerializers
    #--------------------------------------BUSCA LOS MENSAJES POR CUENTA Y LOS PRESENTA EN FORMA DE LISTA-------------

    def buscar_por_id(self, request, *args, **kwargs):
        usuario_id = request.query_params.get('id')
        
        if usuario_id:
            # Filtrar los mensajes por el ID del usuario proporcionado
            mensajes = CanalMensaje.objects.filter(usuario=usuario_id)
            
            if mensajes.exists():
                serializer = self.get_serializer(mensajes, many=True)
                return Response(serializer.data)
            else:
                return Response("No se encontraron mensajes para el usuario especificado", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Se requiere el parámetro 'usuario_id'", status=status.HTTP_400_BAD_REQUEST)

class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializers
