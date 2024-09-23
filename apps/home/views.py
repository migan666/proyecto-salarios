
import base64
from io import BytesIO


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import *

from apps.salario.models import Salario

import matplotlib.pyplot as plt
from collections import Counter



# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.user.is_authenticated:
        return redirect(reverse_lazy("dashboard"))

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("dashboard"))
            else:
                msg = 'Credenciales no válidas'
        else:
            errors = form.errors
            msg = 'Error al validar el formulario'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout_view(request):
  logout(request)
  return redirect('/')

class Dashboard(TemplateView):
    template_name = "home/dashboard.html"

    # Función para generar gráfico de barras
    def generar_grafico_barras(self):
        salarios = Salario.objects.all()
        edades = [salario.edad for salario in salarios]
        salarios_vals = [salario.salario for salario in salarios]

        plt.figure(figsize=(10, 6))
        plt.bar(edades, salarios_vals, color='blue')
        plt.xlabel('Edad')
        plt.ylabel('Salario')
        plt.title('Relación entre Edad y Salario')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        grafico_base64 = base64.b64encode(image_png).decode('utf-8')
        return grafico_base64

    # Función para generar gráfico circular
    def generar_grafico_pie(self):
        salarios = Salario.objects.all()
        ciudades = [salario.ciudad for salario in salarios]
        conteo_por_ciudad = Counter(ciudades)

        labels = list(conteo_por_ciudad.keys())
        sizes = list(conteo_por_ciudad.values())

        plt.figure(figsize=(7, 7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        grafico_base64 = base64.b64encode(image_png).decode('utf-8')
        return grafico_base64
    def get_context_data(self, **kwargs):
        context = {}
        try:
            context = super().get_context_data(**kwargs)

            # Generar gráfico de barras (edad vs salario)
            context['grafico_barras'] = self.generar_grafico_barras()

            # Generar gráfico circular (personas por ciudad)
            context['grafico_pie'] = self.generar_grafico_pie()
            
        except Exception as e:
            context["error"] = str(e)
        context['segment'] = 'dashboard'
        return context