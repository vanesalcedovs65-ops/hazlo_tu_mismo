from django.db import models
from django.contrib.auth.models import User


class Platillo(models.Model):
    CATEGORIAS = (
        ("personal", "Porción personal"),
        ("familiar", "Porción familiar"),
        ("bebida", "Bebida"),
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.URLField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="personal")

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} de {self.usuario.username}"

    def total(self):
        total = sum(item.subtotal() for item in self.items.all())
        return total


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="items", on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.platillo.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.platillo.nombre}"
