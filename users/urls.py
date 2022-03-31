from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users_form),
    path('list/', views.users_list),
]