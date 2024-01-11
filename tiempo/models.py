from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

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

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        # Hashear la contraseña antes de guardar el objeto
        if self.password and not self.confirm_password:
            self.confirm_password = self.password

        if self.password and self.password != self.confirm_password:
            # Manejar la lógica de error si las contraseñas no coinciden
            raise ValueError("Las contraseñas no coinciden")

        if self.password:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    
    
class Rol(models.Model):
    ROLE_CHOICES = [('administrador', 'Administrador'), ('cliente', 'Cliente')]
    nombre_rol = models.CharField(verbose_name="Nombre de Rol", max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.nombre_rol

class Usuario(Persona):
    rol = models.ManyToManyField(Rol, related_name="usuarios", null = True, blank=True)

class Cuenta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuentasUsuario", null=True, blank=True)
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(verbose_name="Fecha de Actualización")
    imagen = models.ImageField(upload_to="fotos/",verbose_name="Imagen")
    numero_horas = models.IntegerField(verbose_name="Número de Horas")

class Categoria(models.Model):
    nombre_categoria = models.CharField(verbose_name="Nombre de Categoría", max_length=100)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    ESTADO_CHOICES = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación")

    def __str__(self):
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
    propietario = models.ForeignKey(Usuario, on_delete= models.RESTRICT, null= True, blank= True)
    estadoVigencia = models.CharField(verbose_name="Estado", max_length=20, choices=[('vigente', 'Vigente'), ('no_vigente', 'No vigente')])
    estadoServicio = models.CharField(verbose_name="EstadoServicio",max_length=20,choices=[('solicitada', 'Solicitada'),('en_proceso', 'En Proceso'),('aprobada', 'Aprobada'),('rechazada', 'Rechazada'),('cancelada', 'Cancelada'),('completada', 'Completada'),('pendiente', 'Pendiente'),('error', 'Error'),('en_revision', 'En Revisión')], null= True, blank= True)
    def __str__(self):
        return self.titulo

class TransaccionTiempo(models.Model):
    servicio =  models.ForeignKey(Servicio, on_delete= models.RESTRICT, null= True, blank= True)
    numero_horas = models.IntegerField(verbose_name="Horas de Transferencia")
    numero_minutos = models.IntegerField(verbose_name="Minutos")
    descripcion = models.CharField(verbose_name="Descripción", max_length=256)
    demandante = models.ManyToManyField(Usuario, related_name="transacciones_demandante", blank=True)
    fecha_transaccion = models.DateField(verbose_name="Fecha de Transacción")
    estadoTransaccion = models.CharField(
    verbose_name="EstadoTransaccion",max_length=20,choices=[('aprobada', 'Aprobada'),('en_proceso', 'En Proceso'),('rechazada', 'Rechazada'),('cancelada', 'Cancelada'),('completada', 'Completada'),('pendiente', 'Pendiente'),('error', 'Error'),('en_revision', 'En Revisión')], null= True, blank= True)
    def __str__(self):
        return str(self.servicio)
    
class Calificacion(models.Model):
    puntuacion = models.IntegerField(verbose_name="Puntuación")
    comentarios = models.CharField(verbose_name="Comentarios", max_length=50)
    transaccioncalificacion=models.ForeignKey(TransaccionTiempo, on_delete=models.RESTRICT, related_name="TransaccionCalificacion", null=True, blank=True)
    def __str__(self):
        return str(self.puntuacion)
    