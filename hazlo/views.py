from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Platillo


def inicio(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasena = request.POST["contrasena"]

        user = authenticate(username=usuario, password=contrasena)

        if user is not None:
            login(request, user)
            return redirect("menu")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "hazlo/inicio.html")


def registro(request):
    from django.contrib.auth.models import User

    if request.method == "POST":
        usuario = request.POST["usuario"]
        contrasena = request.POST["contrasena"]

        if User.objects.filter(username=usuario).exists():
            messages.error(request, "Este usuario ya existe")
        else:
            User.objects.create_user(username=usuario, password=contrasena)
            messages.success(request, "Usuario registrado correctamente")
            return redirect("inicio")

    return render(request, "hazlo/registro.html")


def menu(request):
    return render(request, "hazlo/menu.html")


def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


def ver_menu(request):
    """
    En este punto tu modelo Platillo NO tiene categoría aún,
    así que temporalmente devolvemos todo sin filtrar.
    Cuando te mande el nuevo models.py lo corregimos.
    """

    personales = Platillo.objects.all()
    familiares = Platillo.objects.all()
    bebidas = Platillo.objects.all()

    return render(request, "hazlo/ver_menu.html", {
        "personales": personales,
        "familiares": familiares,
        "bebidas": bebidas
    })


def pedidos(request):
    return render(request, "hazlo/pedidos.html")
