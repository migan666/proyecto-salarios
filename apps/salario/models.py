from django.db import models
from apps.modelobase.models import ModeloBase
from crum import get_current_user



class Salario(ModeloBase):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=70)
    salario = models.DecimalField(default=0,max_digits=8, decimal_places=2)
    class Meta:
        verbose_name_plural = "Salarios"
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario_creador = user
            else:
                self.usuario_editor = user
        super(Salario,self).save()
    def __str__(self):
        return self.nombre
    def clean(self):
        self.nombre = self.nombre.upper()
        self.ciudad = self.ciudad.upper()

