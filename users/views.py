from django.shortcuts import render
 
# Create your views here.

def users_list(request):
    return render(request,"users/users_list.html")

def users_form(request):
    return render(request,"users/users_form.html")

def users_delete(request):
    return