from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Medicamento, Sucursal, Pedido, DetallePedido
from django.db import transaction

def registrar_pedido(request):
    if request.method == 'POST':
        medicamento_id = request.POST['medicamento']
        sucursal_origen_id = request.POST['sucursal_origen']
        sucursal_destino_id = request.POST.get('sucursal_destino')
        cantidad = int(request.POST['cantidad'])

        # Obtener las entidades necesarias
        medicamento = Medicamento.objects.get(id=medicamento_id)
        sucursal_origen = Sucursal.objects.get(id=sucursal_origen_id)
        sucursal_destino = Sucursal.objects.get(id=sucursal_destino_id) if sucursal_destino_id else None

        try:
            with transaction.atomic():
                # Crear el pedido
                pedido = Pedido.objects.create(
                    sucursal_origen=sucursal_origen,
                    sucursal_destino=sucursal_destino
                )

                # Crear el detalle del pedido
                DetallePedido.objects.create(
                    pedido=pedido,
                    medicamento=medicamento,
                    cantidad=cantidad
                )

                # Actualizar inventario
                inventario_origen = sucursal_origen.inventario_set.get(medicamento=medicamento)
                inventario_origen.restar_stock(cantidad)

                if sucursal_destino:
                    inventario_destino, created = sucursal_destino.inventario_set.get_or_create(
                        medicamento=medicamento
                    )
                    inventario_destino.stock += cantidad
                    inventario_destino.save()

                messages.success(request, "Pedido registrado con éxito.")
                return redirect('pedidos')

        except Exception as e:
            messages.error(request, f"Error al registrar el pedido: {e}")
            return redirect('registrar_pedido')

    medicamentos = Medicamento.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'pedido_form.html', {
        'medicamentos': medicamentos,
        'sucursales': sucursales
    })
