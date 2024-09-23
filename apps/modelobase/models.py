from django.db import models
from django.conf import settings

# Create your models here.
class ModeloBase(models.Model):
    usuario_creador         = models.ForeignKey(
                                settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_creation',
                                null=True,blank=True)
    fecha_registro          = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    usuario_editor          = models.ForeignKey(
                                settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_updated',
                                null=True,blank=True)
    fecha_modificacion      = models.DateTimeField(auto_now=True,null=True,blank=True)
    activo                  = models.BooleanField(default=True)
    class Meta:
        abstract = True
