# views.py
import requests
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

def home(request):
    # Hacemos una petición GET a la URL de la API
    response = requests.get("http://localhost:8000/api/mensajes/")
    # Convertimos la respuesta en un objeto JSON
    mensajes = response.json()
    # Renderizamos la plantilla HTML con los datos de los mensajes
    return render(request, "home.html", {"mensajes": mensajes})

@require_http_methods(["GET", "POST"])
def crear_mensaje(request):
    if request.method == "GET":
        # Renderizamos la plantilla HTML con el formulario para crear un mensaje
        return render(request, "crear_mensaje.html")
    elif request.method == "POST":
        # Obtenemos los datos del formulario
        texto = request.POST.get("texto")
        # Hacemos una petición POST a la URL de la API con los datos del mensaje
        response = requests.post("http://localhost:8000/api/mensajes/", data={"texto": texto})
        # Redirigimos a la página principal
        return redirect("/")

@require_http_methods(["GET", "POST"])
def editar_mensaje(request, id):
    if request.method == "GET":
        # Hacemos una petición GET a la URL de la API para obtener el mensaje por su id
        response = requests.get(f"http://localhost:8000/api/mensajes/{id}/")
        # Convertimos la respuesta en un objeto JSON
        mensaje = response.json()
        # Renderizamos la plantilla HTML con el formulario para editar el mensaje
        return render(request, "editar_mensaje.html", {"mensaje": mensaje})
    elif request.method == "POST":
        # Obtenemos los datos del formulario
        texto = request.POST.get("texto")
        # Hacemos una petición PUT a la URL de la API con los datos del mensaje
        response = requests.put(f"http://localhost:8000/api/mensajes/{id}/", data={"texto": texto})
        # Redirigimos a la página principal
        return redirect("/")

@require_http_methods(["POST"])
def eliminar_mensaje(request, id):
    # Hacemos una petición DELETE a la URL de la API para eliminar el mensaje por su id
    response = requests.delete(f"http://localhost:8000/api/mensajes/{id}/")
    # Redirigimos a la página principal
    return redirect("/")



    