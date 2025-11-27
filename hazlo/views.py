from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Platillo, Pedido

# ==========================================
#   PÁGINA DE INICIO
# ==========================================
def inicio(request):
    return render(request, "hazlo/menu.html")


# ==========================================
#   MOSTRAR MENÚ
# ==========================================
def ver_menu(request):
    personales = Platillo.objects.filter(categoria="personal")
    familiares = Platillo.objects.filter(categoria="familiar")
    bebidas = Platillo.objects.filter(categoria="bebida")

    return render(request, "hazlo/ver_menu.html", {
        "personales": personales,
        "familiares": familiares,
        "bebidas": bebidas,
    })


# ==========================================
#   AGREGAR PEDIDO
# ==========================================
def agregar_pedido(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 1))

        pedido = Pedido(
            nombre=platillo.nombre,
            categoria=platillo.categoria,
            cantidad=cantidad,
            precio_unitario=platillo.precio,
            total=platillo.precio * cantidad
        )
        pedido.save()

        messages.success(request, f"Agregado: {cantidad} x {platillo.nombre}")
        return redirect("ver_menu")

    return redirect("ver_menu")


# ==========================================
#   VER PEDIDOS
# ==========================================
def pedidos(request):
    lista = Pedido.objects.all()
    total = sum(p.total for p in lista)

    return render(request, "hazlo/pedidos.html", {
        "pedidos": lista,
        "total": total
    })


# ==========================================
#   ELIMINAR PEDIDO
# ==========================================
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    messages.success(request, "Pedido eliminado")
    return redirect("pedidos")


# ==========================================
#   ELIMINAR TODOS LOS PEDIDOS
# ==========================================
def limpiar_pedidos(request):
    Pedido.objects.all().delete()
    messages.success(request, "Todos los pedidos eliminados")
    return redirect("pedidos")
