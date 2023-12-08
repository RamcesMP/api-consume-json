# urls.py
from django.urls import path
from .views import home, crear_mensaje, editar_mensaje, eliminar_mensaje

urlpatterns = [
    path("", home , name="home"), # La ruta / muestra la lista de mensajes
    path("crear/", crear_mensaje , name="crear"), # La ruta /crear/ muestra el formulario para crear un mensaje
    path("<int:id>/editar/", editar_mensaje , name="editar"), # La ruta /<id>/editar/ muestra el formulario para editar un mensaje específico por su id
    path("<int:id>/eliminar/", eliminar_mensaje , name="eliminar"), # La ruta /<id>/eliminar/ elimina un mensaje específico por su id
]


