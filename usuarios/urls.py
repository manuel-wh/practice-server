from django.conf.urls import url
from . import views

urlpatterns = [
    url("agregar/$", views.agregar_registro, name="agregar_registro"),
    url(r"^editar/(?P<cliente_id>\d+)/$", views.editar_cliente, name='editar_cliente'),
    url(r'^eliminar/(?P<cliente_id>\d+)/$', views.eliminar_cliente, name='eliminar_cliente'),
]