from django.db import models
from django.contrib.auth.models import AbstractUser
from crum import get_current_user

# Create your models here.

class Usuario(AbstractUser):
    tipo_documento = models.CharField(max_length=50,null= True, blank= True)
    nro_documento = models.CharField(max_length=12, unique = True,null= True, blank= True)
    celular = models.CharField(max_length=9,unique = True,null= True, blank= True)
    class Meta:
        verbose_name_plural = "Usuarios"
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.usuario_creador = user
            else:
                self.usuario_editor = user
        super(Usuario,self).save()
    def __str__(self):
        return self.first_name