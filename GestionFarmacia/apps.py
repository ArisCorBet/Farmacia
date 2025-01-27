from django.apps import AppConfig


class GestionFarmaciaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestionFarmacia'

    def ready(self):
        import GestionFarmacia.signals  # Esto importa y registra las señales
