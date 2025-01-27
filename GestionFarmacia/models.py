from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    sucursal_origen = models.ForeignKey(Sucursal, related_name='pedidos_origen', on_delete=models.CASCADE)
    sucursal_destino = models.ForeignKey(Sucursal, related_name='pedidos_destino', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.fecha}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Detalle Pedido {self.pedido.id} - {self.medicamento.nombre}"
