from rest_framework import routers
from django.urls import path, include
from .views import MensajeViewSet

router = routers.DefaultRouter()
router.register("mensajes", MensajeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
