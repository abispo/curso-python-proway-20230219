from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path("pre/", views.pre_registro, name="pre_registro"),
    path("confirmacao/", views.registrar, name="registrar"),
]
