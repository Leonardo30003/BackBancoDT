from django.urls import path
from .views import ServicioViewSet,CuentaViewSet,RolViewSet,UsuarioViewSet,CategoriaViewSet,InteresViewSet,CalificacionViewSet,TransaccionViewSet,CanalUsuarioViewSet,CanalMensajeViewSet,CanalViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #path para Servicios
    path('api/servicios',ServicioViewSet.as_view({'get':'list','post':'create'}), name="lista-servicios"),
    path('api/servicio/<int:pk>', ServicioViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-servicio"),
    path('api/servicio/buscar_por_cuenta/', ServicioViewSet.as_view({'get': 'buscar_por_cuenta'}), name='buscar_por_cuenta'),
    path('api/servicio/buscar_por_id/', ServicioViewSet.as_view({'get': 'buscar_por_id'}), name='buscar_por_id'),

    #path para Cuenta
    path('api/cuentas',CuentaViewSet.as_view({'get':'list','post':'create'}), name="lista-cuentas"),
    path('api/cuenta/<int:pk>', CuentaViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-cuenta"),
    path('api/cuenta/buscarCuentaUsuario/', CuentaViewSet.as_view({'get': 'buscarCuentaUsuario'}), name='buscarCuentaUsuario'),
<<<<<<< HEAD

=======
>>>>>>> 0434fdd673b28c72ea62f572d18b307e34c4164f
    #path para CuentaId
    path('api/cuenta/buscarCuentaIdCuenta/', CuentaViewSet.as_view({'get': 'buscarCuentaIdCuenta'}), name='buscarCuentaIdCuenta'),
    #path para  Usuario
    path('api/usuarios', UsuarioViewSet.as_view({'get':'list','post':'create'}), name="lista-usuarios"),
    path('api/usuario/<int:pk>', UsuarioViewSet.as_view({'get':'retrieve','put':'update'}), name="detalle-usuario"),
    # agregamos una nueva linea
    path('api/usuario/buscar_por_correo/', UsuarioViewSet.as_view({'get': 'buscar_por_correo'}), name='buscar_por_correo'),
    path('api/usuario/buscarPropietarioIdCuenta/', UsuarioViewSet.as_view({'get': 'buscarPropietarioIdCuenta'}), name='buscarPropietarioIdCuenta'),
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

    # Paths para CanalUsuario
    path('api/canalusuarios', CanalUsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name="lista-canalusuarios"),
    path('api/canalusuario/<int:pk>', CanalUsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="detalle-canalusuario"),

    # Paths para CanalMensaje
    path('api/canalmensajes/', CanalMensajeViewSet.as_view({'get': 'list', 'post': 'create'}), name="lista-canalmensajes"),
    path('api/canalmensaje/<int:pk>', CanalMensajeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="detalle-canalmensaje"),
    path('api/canalmensaje/buscar_por_id/', CanalMensajeViewSet.as_view({'get': 'buscar_por_id'}), name='buscar_por_id'),

    # Paths para Canal
    path('api/canales', CanalViewSet.as_view({'get': 'list', 'post': 'create'}), name="lista-canales"),
    path('api/canal/<int:pk>', CanalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="detalle-canal"),
    #autentificacion
    path('api/login',TokenObtainPairView.as_view(),name="token_obtain_pair")
    
]


