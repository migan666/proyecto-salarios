from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    path('salarios/lista/',login_required(ListaSalarios.as_view()),name="lista_salarios"),
    path('salarios/lista_ajax/',login_required(ListaSalariosjax.as_view())),
    path('salarios/nuevo/',login_required(NuevoSalario.as_view()),name="nuevo_salario"),
	#path('salarios/detalle/<int:pk>/',login_required(DetalleVentaView.as_view()),name='detalle_salario'),

]
