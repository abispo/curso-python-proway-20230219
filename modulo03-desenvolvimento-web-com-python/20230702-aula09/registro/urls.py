from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path("pre/", views.pre_registro, name="pre_registro"),
    path("pre/<uuid>/reenviar", views.reenviar_pre_registro, name="reenviar_pre_registro"),
    path("confirmacao/", views.registrar, name="registrar"),
    path("processar-login/", views.processar_login, name="processar_login"),
]
