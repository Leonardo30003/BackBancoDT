from django.contrib import admin
from .models import Rol,Usuario,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo,Canal, CanalUsuario, CanalMensaje

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Interes)
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Calificacion)
admin.site.register(Servicio)
admin.site.register(TransaccionTiempo)

#CHAT DEL BANCO DEL TIEMPO
class CanalMensajeInline(admin.TabularInline):
	model = CanalMensaje
	extra = 1

class CanalUsuarioInline(admin.TabularInline):
	model = CanalUsuario
	extra = 1


class CanalAdmin(admin.ModelAdmin):
	inlines = [CanalMensajeInline, CanalUsuarioInline]

	class Meta:
		model = Canal

admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)
