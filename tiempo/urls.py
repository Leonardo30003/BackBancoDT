from django.urls import path
from .views import ServicioViewSet,CuentaViewSet,RolViewSet,UsuarioViewSet,CategoriaViewSet,InteresViewSet,CalificacionViewSet,TransaccionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #path para Servicios
    path('api/servicios',ServicioViewSet.as_view({'get':'list','post':'create'}), name="lista-servicios"),
    path('api/servicio/<int:pk>', ServicioViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-servicio"),
    #path para Cuenta
    path('api/cuentas',CuentaViewSet.as_view({'get':'list','post':'create'}), name="lista-cuentas"),
    path('api/cuenta/<int:pk>', CuentaViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-cuenta"),
    #path para  Usuario
    path('api/usuarios', UsuarioViewSet.as_view({'get':'list','post':'create'}), name="lista-usuarios"),
    path('api/usuario/<int:pk>', UsuarioViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-usuario"),
     #path para  Rol
    path('api/rols',RolViewSet.as_view({'get':'list','post':'create'}), name="lista-rols"),
    path('api/rol/<int:pk>', RolViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-rol"),     
     #path para  Categoria
    path('api/categorias',CategoriaViewSet.as_view({'get':'list','post':'create'}), name="lista-categorias"),
    path('api/categoria/<int:pk>', CategoriaViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-categoria"), 
     #path para  Intereses
    path('api/intereses',InteresViewSet.as_view({'get':'list','post':'create'}), name="lista-intereses"),
    path('api/interes/<int:pk>', InteresViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-interes"), 
     #path para  Calificacion
    path('api/calificaciones',CalificacionViewSet.as_view({'get':'list','post':'create'}), name="lista-calificaciones"),
    path('api/calificacion/<int:pk>',CalificacionViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-calificacion"), 
     #path para  TransaccionTiempo
    path('api/transacciones',TransaccionViewSet.as_view({'get':'list','post':'create'}), name="lista-transacciones"),
    path('api/transaccion/<int:pk>', TransaccionViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-transaccion"), 
    #autentificacion
    path('api/login',TokenObtainPairView.as_view(),name="token_obtain_pair")
]


