from django.urls import path, include
from . import views

urlpatterns = [

    # Patrones URL hay que especificar las direcciones url el punto de registro de la app 
    # Patrones url dentro se pueden apreciar las asignaciones de url para adimin 
    # Para barra diagonal - Formulario

    path('', views.users_form),
    path('list/', views.users_list),
]