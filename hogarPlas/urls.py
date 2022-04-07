from django.contrib import admin
from django.urls import path, include

# Patrones url dentro se pueden apreciar las asignaciones de url para adimin 
# Para barra diagonal 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
 