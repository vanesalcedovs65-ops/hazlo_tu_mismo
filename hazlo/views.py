from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Platillo

def inicio(request):
    # Página de inicio; puedes ajustar el template si usas otro
    return render(request, "hazlo/inicio.html")
from .models import Platillo

def ver_menu(request):
    personales = Platillo.objects.filter(categoria="personal")
    familiares = Platillo.objects.filter(categoria="familiar")
    bebidas = Platillo.objects.filter(categoria="bebida")

    return render(request, "hazlo/ver_menu.html", {
        "personales": personales,
        "familiares": familiares,
        "bebidas": bebidas,
    })
