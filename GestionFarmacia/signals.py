from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DetallePedido


@receiver(post_save, sender=DetallePedido)
def actualizar_inventario(sender, instance, created, **kwargs):
    if created:
        try:
            instance.restar_stock()
        except ValueError as e:
            print(f"Error al actualizar inventario: {e}")
