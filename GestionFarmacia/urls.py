from django.contrib import admin
from django.urls import path, include
from GestionFarmacia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('gestion/', include('GestionFarmacia.urls')),
]
