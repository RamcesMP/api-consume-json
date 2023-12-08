from rest_framework import serializers, viewsets, routers
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from rest_framework import viewsets


# Definimos un modelo de datos para guardar los mensajes
class Mensaje(models.Model):
    texto = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto





