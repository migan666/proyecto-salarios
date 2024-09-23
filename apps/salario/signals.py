from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Salario

@receiver(post_migrate)
def insertar_registros_iniciales(sender, **kwargs):
    # Verificar si la tabla Salario está vacía antes de insertar
    if not Salario.objects.exists():
        registros = [
            {"nombre": "Juan", "edad": 25, "ciudad": "Lima", "salario": 2500.50},
            {"nombre": "Pedro", "edad": 30, "ciudad": "Trujillo", "salario": 3200.00},
            {"nombre": "Ana", "edad": 28, "ciudad": "Lima", "salario": 2900.75},
            {"nombre": "Laura", "edad": 35, "ciudad": "Chiclayo", "salario": 4000.00},
            {"nombre": "Carlos", "edad": 22, "ciudad": "Piura", "salario": 1800.25},
        ]
        
        for registro in registros:
            Salario.objects.create(**registro)

        print("Registros iniciales insertados correctamente")
