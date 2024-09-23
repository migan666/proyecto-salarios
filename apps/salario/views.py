import json


from django.views.generic.base import TemplateView
from django.views import View , generic
from django.urls import reverse_lazy
from django.http import  JsonResponse, HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import *
from .forms import *


class ListaSalarios( TemplateView):
    """
    Vista basada en clase (CBV) que hereda de TemplateView. Muestra una lista de salarios.

    Atributos:
    ----------
    template_name : str
        Define la plantilla HTML que se utilizará para renderizar la página.

    Métodos:
    --------
    get_context_data(self, **kwargs):
        Obtiene el contexto adicional que será pasado a la plantilla.
        - `segment`: Indica qué sección está activa en el menú de navegación.
        - `encabezado`: Proporciona un encabezado para la sección de la lista de salarios.
    """
    template_name = "salario/lista.html"
    def get_context_data(self, **kwargs):
        context = {}
        try:
            context = super().get_context_data(**kwargs)
        except Exception as e:
            context["error"] = str(e)
        context['segment'] = 'salarios'
        context['encabezado'] = 'Lista de salarios'
        return context

class ListaSalariosjax(generic.ListView):
    """
    Vista basada en clase (CBV) que hereda de ListView. Devuelve una lista de salarios filtrados, principalmente diseñada para solicitudes AJAX.

    Atributos:
    ----------
    model : Salario
        Modelo asociado a la vista para listar los objetos de Salario.

    Métodos:
    --------
    get_datos(self):
        Filtra los datos activos del modelo Salario y los devuelve en formato de diccionario.

    get(self, request, *args, **kwargs):
        Maneja solicitudes GET y verifica si la solicitud es AJAX. Si es así, devuelve una lista paginada de salarios en formato JSON.
    """
    model = Salario
    def get_datos(self):
        filtro = self.request.GET.get('filtro', None)
        datos = self.model.objects.filter(activo=True)

        return datos.values(
            'nombre',
            'edad',
            'ciudad',
            'salario',
        ).order_by('-fecha_registro')
    def get(self, request, *args, **kwargs):
        try:
            if request.is_ajax():
                list_data = []
                inicio = int(request.GET.get('inicio'))
                fin = int(request.GET.get('limite'))

                for indice, valor in enumerate(self.get_datos()[inicio:inicio + fin], inicio):
                    data = {}
                    indice += 1
                    data['nombre'] = valor['nombre']
                    data['edad'] = str(valor['edad'])
                    data['ciudad'] = valor['ciudad']
                    data['salario'] = str(valor['salario'])
                    data['indice'] = str(indice)
                    list_data.append(data)
                datos = {
                    'length': self.get_datos().count(),
                    'objects': list_data,
                }
                return HttpResponse(json.dumps(datos), 'application/json')
        except Exception as e:
            mensaje = str(e)
            return HttpResponse({'error': mensaje}, 'application/json')

class NuevoSalario(generic.CreateView):
    """
    Vista basada en clase (CBV) que hereda de CreateView. Maneja la creación de nuevos registros de salario.

    Atributos:
    ----------
    model : Salario
        Modelo asociado a la vista.
    form_class : FormSalario
        Formulario asociado al modelo Salario.
    template_name : str
        Define la plantilla HTML para renderizar el formulario de creación.
    success_url : str
        URL de redirección después de crear un nuevo salario.

    Métodos:
    --------
    get_context_data(self, **kwargs):
        Añade al contexto datos adicionales como el segmento activo y el encabezado.

    post(self, request, *args, **kwargs):
        Maneja la solicitud POST, valida el formulario, guarda el nuevo registro y redirige a la URL de éxito. Muestra mensajes de éxito o error.
    """
    model = Salario
    form_class = FormSalario
    template_name = "salario/nuevo.html"
    success_url = reverse_lazy("lista_salarios")
    def get_context_data(self, **kwargs):
        context = {}
        try:
            context = super().get_context_data(**kwargs)
        except Exception as e:
            context["error"] = str(e)
        context['segment'] = 'salarios'
        context['encabezado'] = 'Nuevo Salario'
        return context
    def post(self,request,*args,**kwargs):
        context = {}
        try:
            form = self.get_form()
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, '¡Salario Registrado!')
                return redirect(self.success_url)
            context['form'] = form
            context['segment'] = 'salarios'
            context['encabezado'] = 'Nuevo Salario'
            return render(request,self.template_name,context)
        except Exception as e:
            context["error"] = str(e)
            context['segment'] = 'salarios'
            context['encabezado'] = 'Nuevo Salario'
            return render(request,self.template_name,context)

