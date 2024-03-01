# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from usuarios.models import Cliente
from forms import ClienteForm
from usuarios.tasks import log_create_action, log_update_action, log_delete_action

def index(request):

    usuarios = Cliente.objects.all()
    return render(request, "index.html", {"usuarios":usuarios})

def agregar_registro(request):

    usuario = ClienteForm()
    if request.method == 'POST':
        usuario = ClienteForm(request.POST)
        if usuario.is_valid():
            usuario.save()
            log_create_action.delay(usuario.instance.id)
            return HttpResponseRedirect(reverse('index'))

    return render(request, "agregar.html", {
        "cliente_form": usuario
    })


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            log_update_action.delay(cliente_id)
            return redirect('index')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    log_delete_action.delay(cliente_id)
    return redirect('index')