from django.contrib import admin
from .models import Rol,Usuario,Cuenta,Categoria,Interes,Calificacion,Servicio,TransaccionTiempo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(Interes)
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Calificacion)
admin.site.register(Servicio)
admin.site.register(TransaccionTiempo)
