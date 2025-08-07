from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse


# Create your views here.


class ProductoListView(ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_Detail.html"
    context_object_name = "producto"


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre","descripcion","precio","stock","imagen"]
    success_url = reverse_lazy("lista_productos")


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre","descripcion","precio","stock","imagen"]
    success_url = reverse_lazy("lista_productos")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm.html"
    success_url = reverse_lazy("lista_productos")



def desafio(request):

    empleados=[
            'María González',
            'Carlos Rodríguez',
            'Laura Sánchez',
            'Miguel Díaz',
            'Sofía Ramírez',
            'David Fernández',
            'Lucía Morales',
            'José Castillo',
            'Paula Herrera',]

    return render(request, "desafio.html",{"empleados": empleados})


def base(request):
    return render(request, "base.html",{})

def test(request):
    return HttpResponse("<h1>empleados</h1>")



def nombre(request):
    return render(request,"nombre.html",{})


def test2(request):
    return render(request, "test2.html",{})


def test3(request):
    return render(request, "test2.html",{})



def layout(request):
    return render(request, "mi_app/layout.html",{})



def herencia(request):
    return render(request, "mi_app/herencia.html",{})











