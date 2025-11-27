from django.contrib import admin
from .models import Platillo, Pedido, PedidoItem

admin.site.register(Platillo)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
