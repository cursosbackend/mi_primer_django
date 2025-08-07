
from django.urls import path 
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoUpdateView,
    ProductoDeleteView,
    desafio,
    base,
    test,
    nombre,
    test2,
    test3,
    layout,
    herencia
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="lista_productos"),
    path("crear", ProductoCreateView.as_view(), name="crear_producto"),
    path("producto/detalle/<int:pk>", ProductoDetailView.as_view(), name="detail_producto"),
    path("producto/actualizacion/<int:pk>", ProductoUpdateView.as_view(), name="update_producto"),
    path("producto/borrar/<int:pk>", ProductoDeleteView.as_view(), name="borrar_producto"),
    path("desafio/", desafio , name="desafio"),
    path("base/", base , name="base"),
    path("test/", test , name="test"),
    path("nombre/", nombre , name="nombre"),
    path("test2/",test2, name="test2"),
    path("test3/", test3, name="test3"),
    path("layout/", layout, name="layout"),
    path("herencia/", herencia, name="herencia"),
]