from django.urls import path
from GestionFarmacia import views


urlpatterns = [
    path('registrar_pedido/', views.registrar_pedido, name='registrar_pedido'),
    path('pedidos/', views.pedidos_view, name='pedidos'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('sucursales/', views.sucursales_view, name='sucursales'),
]
