from rest_framework import serializers
from .models import Usuario,Rol,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo,CanalMensaje, CanalUsuario, Canal
from django.contrib.auth.models import User

        
class CuentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        read_only_fields = ['id','user_permisssions','groups','is_superuser','date_joined','groups','user_permissions','last_login','fecha_nacimiento','rol','imagen']

class ServicioSerializers(serializers.ModelSerializer):
    ##propietario= UsuarioSerializers()
    class Meta:
        model = Servicio
        fields = ['id','ROL_CHOICES','titulo','descripcion_actividad','tiempo_requerido','fecha_creacion','fecha_vigente','propietario','estadoVigencia','estadoServicio']
        # fields = '_all_'
        read_only_fields = ['id']
        
class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        
        
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class InteresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Interes
        fields = '__all__'
        
class CalificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class TransaccionSerializers(serializers.ModelSerializer):
    #servicio=ServicioSerializers()
    class Meta:
        model = TransaccionTiempo
        fields = '__all__'
        read_only_fields = ['demandante']


#serializer chat

class CanalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields='__all__'

class CanalMensajeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CanalMensaje
        fields='__all__'
        read_only_fields=['actualizar']

class CanalUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model:CanalUsuario
        fields='__all__'