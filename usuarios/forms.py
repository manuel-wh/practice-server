#!
# -*- coding: utf-8 -*-
from django import forms
from usuarios.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad']