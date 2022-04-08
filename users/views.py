from django.shortcuts import render
 
# Create your views here.
# Solicitudes actuales que se pueden hacer dentro de estas vistas por archivo
# Definida para podificar y mostrar todo

def users_list(request):
    return render(request,"users/users_list.html")

def users_form(request):
    return render(request,"users/users_form.html")

def users_delete(request):
    return

#def login(request):
 #   return