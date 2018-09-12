from django.urls import path
from .views import *
from django.contrib.auth.models import User 

urlpatterns = [
	path('about/',vista_about),
	path('casa/',vista_casa),
	path('seccion/',vista_seccion),
	path('contacto/',vista_contacto),
	path('',vista_inicio),
	path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
	path('lista_producto/', vista_lista_producto, name='vista_lista_producto'),
	path('ver_producto/<int:id_product>/', vista_ver_producto, name='vista_ver_producto' ),
	path('editar_producto/<int:id_product>/', vista_editar_producto, name='vista_editar_producto' ),
	path('eliminar_producto/<int:id_product>/', vista_eliminar_producto, name='vista_eliminar_producto' ),
	path('login/',vista_login, name ='vista_login'),
	path('logout/',vista_logout, name ='vista_logout'),
	path('register/',vista_register, name= 'vista_register'),
	path('crear_perfil/',vista_crear_perfil, name= 'crear_perfil'),
	path('ws/productos/',ws_productos_vista, name = 'ws_productos_vista'),
]
