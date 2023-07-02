from django.urls import path

from . import views

app_name = "alunos"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
]
