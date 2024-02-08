from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

#LIBRERIAS DEL CHAT 
from django.conf import settings
import uuid

from django.apps import apps

from django.db.models import Count

# Create your models here.

class Persona(AbstractUser):
    GENDER_CHOICES = [('h', 'Hombre'), ('m', 'Mujer')]
    first_name = models.CharField(verbose_name="Nombres", max_length=50)
    last_name = models.CharField(verbose_name="Apellidos", max_length=50)
    username=models.CharField(verbose_name="Username", max_length=100, unique=True)
    password=models.CharField(verbose_name="Password", max_length=100)
    confirm_password = models.CharField(verbose_name="Confirmar Password", max_length=100, null=True, blank=True)
    genero = models.CharField(verbose_name="Género", max_length=1, choices=GENDER_CHOICES)
    documento_identificacion = models.CharField(verbose_name="Cédula", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=50)
    telefono = models.CharField(verbose_name="Teléfono", max_length=50)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento",null=True, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=150,null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True, blank=True )
	

    def _str_(self):
        return self.first_name
    
    # def save(self, *args, **kwargs):
    #     # Hashear la contraseña antes de guardar el objeto
    #     if self.password and not self.confirm_password:
    #         self.confirm_password = self.password

    #     if self.password and self.password != self.confirm_password:
    #         # Manejar la lógica de error si las contraseñas no coinciden
    #         raise ValueError("Las contraseñas no coinciden")

    #     if self.password:
    #         self.password = make_password(self.password)

    #     super().save(*args, **kwargs)

    
    
class Rol(models.Model):
    ROLE_CHOICES = [('administrador', 'Administrador'), ('cliente', 'Cliente')]
    nombre_rol = models.CharField(verbose_name="Nombre de Rol", max_length=50, choices=ROLE_CHOICES)

    def _str_(self):
        return self.nombre_rol

class Usuario(Persona):
    rol = models.ManyToManyField(Rol, related_name="usuarios", null = True, blank=True)
    imagen = models.ImageField(upload_to="fotos/",verbose_name="Imagen")
	

class Cuenta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentasUsuario", null=True, blank=True)
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(verbose_name="Fecha de Actualización")
    numero_horas = models.IntegerField(verbose_name="Número de Horas")

class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre de Categoría", max_length=100)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    ESTADO_CHOICES = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")

    def _str_(self):
        return self.nombre_categoria

class Interes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioInteres", null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="categorias", blank=True)

class Servicio(models.Model):
    ROL_CHOICES = models.CharField (verbose_name= "oferta/demanda",max_length=15, choices=[('Oferta', 'Oferta'), ('Demanda', 'Demanda')], null= True, blank=True)
    titulo = models.CharField(verbose_name="Título", max_length=150)
    descripcion_actividad = models.CharField(verbose_name="Descripción", max_length=256)
    tiempo_requerido = models.IntegerField(verbose_name="Horas Requeridas")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación",null= True, blank= True)
    fecha_vigente = models.DateField(verbose_name="Fecha Vigente",null= True, blank= True)
    propietario = models.ForeignKey(Cuenta, on_delete= models.RESTRICT, null= True, blank= True)
    estadoVigencia = models.CharField(verbose_name="Estado", max_length=20, choices=[('vigente', 'Vigente'), ('no_vigente', 'No vigente')])
    estadoServicio = models.CharField(verbose_name="EstadoServicio",max_length=20,choices=[('solicitada', 'Solicitada'),('en_proceso', 'En Proceso'),('aprobada', 'Aprobada'),('rechazada', 'Rechazada'),('cancelada', 'Cancelada'),('completada', 'Completada'),('pendiente', 'Pendiente'),('error', 'Error'),('en_revision', 'En Revisión')], null= True, blank= True)
    def _str_(self):
        return self.titulo

class TransaccionTiempo(models.Model):
    servicio =  models.ForeignKey(Servicio, on_delete= models.RESTRICT)
    numero_horas = models.IntegerField(verbose_name="Horas de Transferencia")
    numero_minutos = models.IntegerField(verbose_name="Minutos", blank=True, null=True)
    descripcion = models.CharField(verbose_name="Descripción", max_length=256)
    propietario = models.ForeignKey("Cuenta", related_name="propietario_cuenta", blank=True, null=True, on_delete = models.RESTRICT)
    demandante = models.ManyToManyField(Usuario, related_name="transacciones_demandante") #la siguiente linea se debe eliminar
    demandanteCuenta = models.ForeignKey("Cuenta",verbose_name="quien oferta del servicio", blank=True, on_delete = models.RESTRICT)
    fecha_transaccion = models.DateField(verbose_name="Fecha de Transacción")
    estadoTransaccion = models.CharField(verbose_name="EstadoTransaccion",max_length=20,choices=[('aprobada', 'Aprobada'),('en_proceso', 'En Proceso'),('rechazada', 'Rechazada'),('cancelada', 'Cancelada'),('completada', 'Completada'),('pendiente', 'Pendiente'),('error', 'Error'),('en_revision', 'En Revisión')], null= True, blank= True)
    def str(self):
        return str(self.servicio)
	
class Calificacion(models.Model):
    puntuacion = models.IntegerField(verbose_name="Puntuación")
    comentarios = models.CharField(verbose_name="Comentarios", max_length=50)
    transaccioncalificacion=models.ForeignKey(TransaccionTiempo, on_delete=models.RESTRICT, related_name="TransaccionCalificacion", null=True, blank=True)
    def _str_(self):
        return str(self.puntuacion)
    
#MODELS DEL CHAT
# Usuario = settings.AUTH_USER_MODEL

class ModelBase(models.Model):
	id = models.AutoField(primary_key=True)
	tiempo = models.DateTimeField(auto_now_add=True)
	actualizar = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class CanalMensaje(ModelBase):
	canal   = models.ForeignKey("Canal", on_delete=models.CASCADE)
	usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
	texto =  models.TextField()
	

class CanalUsuario(ModelBase):
	canal  = models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
	usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)


class CanalQuerySet(models.QuerySet):

	def solo_uno(self):
		return self.annotate(num_usuarios=Count("usuarios")).filter(num_usuarios=1)

	def solo_dos(self):
		return self.annotate(num_usuarios= Count("usuarios")).filter(num_usuarios=2)

	def filtrar_por_username(self, username):
		return self.filter(canalusuario_usuario_username=username)


class CanalManager(models.Manager):
	
	def get_queryset(self, *args, **kwargs):
		return CanalQuerySet(self.model, using=self._db)

	def filtrar_ms_por_privado(self, username_a, username_b):
		return self.get_queryset().solo_dos().filtrar_por_username(username_a).filtrar_por_username(username_b)

	def obtener_o_crear_canal_usuario_actual(self, Usuario):
		qs = self.get_queryset().solo_uno().filtrar_por_username(Usuario.username)
		if qs.exists():
			return qs.order_by("tiempo").first, False

		canal_obj = Canal.objects.create()
		CanalUsuario.objects.create(usuario=Usuario, canal=canal_obj)
		return canal_obj, True

	def obtener_o_crear_canal_ms(self, username_a, username_b):
		qs = self.filtrar_ms_por_privado(username_a, username_b)
		if qs.exists():

			return qs.order_by("tiempo").first(), False #obj, created

		Usuario = apps.get_model("auth", model_name='Usuario')
		usuario_a, usuario_b = None, None
		try:
			usuario_a = Usuario.objects.get(username=username_a)
		except Usuario.DoesNotExist:
			return None, False

		try:
			usuario_b = Usuario.objects.get(username=username_b)
		except Usuario.DoesNotExist:
			return None, False

		if usuario_a == None or usuario_b==None:
			return None, False

		
		obj_canal =Canal.objects.create()
		canal_usuario_a = CanalUsuario(usuario=usuario_a, canal=obj_canal)
		canal_usuario_b = CanalUsuario(usuario=usuario_b, canal=obj_canal)
		CanalUsuario.objects.bulk_create([canal_usuario_a, canal_usuario_b])
		return obj_canal, True

class Canal(ModelBase):
	#como funciona slak
	#1 user
	#2 users
	#2+

	usuarios = models.ManyToManyField("Usuario", blank=True, through=CanalUsuario)

	objects = CanalManager()