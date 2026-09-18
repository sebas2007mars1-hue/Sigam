from django.contrib import admin
from django.urls import path

from backend.usuarios.views_password import (
    RecuperarPasswordView,
    RecuperarEnviadoView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    recuperar_password_api,
)

urlpatterns = [
    path("admin/", admin.site.urls),

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

    # API para Angular
    path(
        "api/recuperar/",
        recuperar_password_api,
        name="api_recuperar",
    ),
]