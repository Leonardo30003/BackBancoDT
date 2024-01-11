# Generated by Django 4.2.6 on 2023-10-24 20:25

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Nombres")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Username"
                    ),
                ),
                ("password", models.CharField(max_length=100, verbose_name="Password")),
                (
                    "genero",
                    models.CharField(
                        choices=[("h", "Hombre"), ("m", "Mujer")],
                        max_length=1,
                        verbose_name="Género",
                    ),
                ),
                (
                    "documento_identificacion",
                    models.CharField(max_length=50, verbose_name="Cédula"),
                ),
                ("email", models.EmailField(max_length=50, verbose_name="Email")),
                ("telefono", models.CharField(max_length=50, verbose_name="Teléfono")),
                (
                    "fecha_nacimiento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de Nacimiento"
                    ),
                ),
                (
                    "direccion",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Dirección"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_categoria",
                    models.CharField(
                        max_length=100, verbose_name="Nombre de Categoría"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(max_length=200, verbose_name="Descripción"),
                ),
                ("fecha_creacion", models.DateField(verbose_name="Fecha de Creación")),
            ],
        ),
        migrations.CreateModel(
            name="Rol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_rol",
                    models.CharField(
                        choices=[
                            ("administrador", "Administrador"),
                            ("cliente", "Cliente"),
                        ],
                        max_length=50,
                        verbose_name="Nombre de Rol",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Servicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ROL_CHOICES",
                    models.CharField(
                        blank=True,
                        choices=[("Oferta", "Oferta"), ("Demanda", "Demanda")],
                        max_length=15,
                        null=True,
                        verbose_name="oferta/demanda",
                    ),
                ),
                ("titulo", models.CharField(max_length=150, verbose_name="Título")),
                (
                    "descripcion_actividad",
                    models.CharField(max_length=256, verbose_name="Descripción"),
                ),
                (
                    "tiempo_requerido",
                    models.IntegerField(verbose_name="Horas Requeridas"),
                ),
                ("fecha_creacion", models.DateField(verbose_name="Fecha de Creación")),
                ("fecha_vigente", models.DateField(verbose_name="Fecha Vigente")),
                (
                    "estadoVigencia",
                    models.CharField(
                        choices=[("Vigente", "Vigente"), ("No vigente", "No vigente")],
                        max_length=20,
                        verbose_name="Estado",
                    ),
                ),
                (
                    "estadoServicio",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("solicitada", "Solicitada"),
                            ("en_proceso", "En Proceso"),
                            ("aprobada", "Aprobada"),
                            ("rechazada", "Rechazada"),
                            ("cancelada", "Cancelada"),
                            ("completada", "Completada"),
                            ("pendiente", "Pendiente"),
                            ("error", "Error"),
                            ("en_revision", "En Revisión"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="EstadoServicio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TransaccionTiempo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero_horas",
                    models.IntegerField(verbose_name="Horas de Transferencia"),
                ),
                ("numero_minutos", models.IntegerField(verbose_name="Minutos")),
                (
                    "descripcion",
                    models.CharField(max_length=256, verbose_name="Descripción"),
                ),
                (
                    "fecha_transaccion",
                    models.DateField(verbose_name="Fecha de Transacción"),
                ),
                (
                    "estadoTransaccion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("aprobada", "Aprobada"),
                            ("en_proceso", "En Proceso"),
                            ("rechazada", "Rechazada"),
                            ("cancelada", "Cancelada"),
                            ("completada", "Completada"),
                            ("pendiente", "Pendiente"),
                            ("error", "Error"),
                            ("en_revision", "En Revisión"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="EstadoTransaccion",
                    ),
                ),
                (
                    "servicio",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="tiempo.servicio",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Calificacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("puntuacion", models.IntegerField(verbose_name="Puntuación")),
                (
                    "comentarios",
                    models.CharField(max_length=50, verbose_name="Comentarios"),
                ),
                (
                    "transaccioncalificacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="TransaccionCalificacion",
                        to="tiempo.transacciontiempo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "rol",
                    models.ManyToManyField(
                        blank=True, null=True, related_name="usuarios", to="tiempo.rol"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("tiempo.persona",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="transacciontiempo",
            name="demandante",
            field=models.ManyToManyField(
                blank=True, related_name="transacciones_demandante", to="tiempo.usuario"
            ),
        ),
        migrations.AddField(
            model_name="servicio",
            name="propietario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="tiempo.usuario",
            ),
        ),
        migrations.CreateModel(
            name="Interes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categoria",
                    models.ManyToManyField(
                        blank=True, related_name="categorias", to="tiempo.categoria"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="UsuarioInteres",
                        to="tiempo.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cuenta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_creacion", models.DateField(verbose_name="Fecha de Creación")),
                (
                    "fecha_actualizacion",
                    models.DateField(verbose_name="Fecha de Actualización"),
                ),
                (
                    "imagen",
                    models.ImageField(upload_to="fotos/", verbose_name="Imagen"),
                ),
                ("numero_horas", models.IntegerField(verbose_name="Número de Horas")),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cuentasUsuario",
                        to="tiempo.usuario",
                    ),
                ),
            ],
        ),
    ]
