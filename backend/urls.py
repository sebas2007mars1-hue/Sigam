"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backend.usuarios.views import login_usuario, inicio
from backend.usuarios.views_password import (
    RecuperarPasswordView,
    RecuperarEnviadoView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login e inicio
    path("login/", login_usuario, name="login"),
    path("inicio/", inicio, name="inicio"),

    # Recuperación de contraseña
    path(
        "recuperar/",
        RecuperarPasswordView.as_view(),
        name="recuperar",
    ),

    path(
        "recuperar/enviado/",
        RecuperarEnviadoView.as_view(),
        name="recuperar_enviado",
    ),

    path(
        "recuperar/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),

    path(
        "recuperar/completado/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]