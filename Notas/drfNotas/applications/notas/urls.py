#
from django.urls import path

from . import views

app_name = "notas_app"

urlpatterns = [
    path(
        'lita-notas/',
        views.ListaNotas.as_view(),
        name="notas"
    ),
]
