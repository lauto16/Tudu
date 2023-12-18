from django.contrib import admin
from django.urls import path
from gestionNotas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', vista_login, name="vista_login"),
    path('register/', vista_register),
    path('Tudu/', vista_principal, name="vista_principal"),
]
