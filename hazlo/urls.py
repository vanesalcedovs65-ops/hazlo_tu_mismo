from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('registro/', views.registro, name="registro"),
    path('menu/', views.menu, name="menu"),
    path('ver_menu/', views.ver_menu, name="ver_menu"),
    path('pedidos/', views.pedidos, name="pedidos"),
    path('logout/', views.cerrar_sesion, name="logout"),
]
