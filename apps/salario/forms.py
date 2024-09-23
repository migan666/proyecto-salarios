
from .models import *

from decimal import Decimal
from django.forms import ModelForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,HTML,ButtonHolder

class FormSalario(ModelForm):
    class Meta:
        model = Salario
        fields = "__all__"
        widgets = {
            'nombre':forms.TextInput(attrs={'autocomplete':'off'}),
            'edad':forms.TextInput(attrs={'autocomplete':'off'}),
            'ciudad':forms.TextInput(attrs={'autocomplete':'off'}),
            'salario':forms.TextInput(attrs={'autocomplete':'off'}),
            }
        exclude = ['activo','usuario_creador','usuario_editor','fecha_modificacion','usuario_registro']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'formulario_salario'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn-primary mt-2'))
        self.helper.layout = Layout(
            Row(
                Column('nombre', css_class='col-md-10 mb-0'),
                Column('edad', css_class='col-md-2 mb-0'),
                css_class='row'
            ),
            Row(
                Column('ciudad', css_class='col-md-6 mb-0'),
                Column('salario', css_class='col-md-6 mb-0'),
                css_class='row'
            ),
        )

    def clean(self):
        cd = self.cleaned_data        
        edad = cd.get('edad')
        salario = cd.get('salario')
        if edad:
            try:
                int(edad)
            except ValueError:
                self.add_error('edad', 'El valor debe ser un número entero.')
        
        if int(edad) < 15 or (edad) > 80:
            self.add_error('edad', 'Edad invalida.')      
       
        if salario:
            try:
                Decimal(salario)
            except ValueError:
                self.add_error('salario', 'El valor debe ser un número decimal válido.')

        return cd

