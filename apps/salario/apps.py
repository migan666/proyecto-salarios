from django.apps import AppConfig


class SalarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.salario'

    def ready(self):
        import apps.salario.signals
