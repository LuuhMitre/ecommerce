from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from . import models


class ProductList(ListView):
    model = models.Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 6


class ProductDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe")


class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Adicionar carrinho")


class RemovefromCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remover Carrinho")


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Carrinho")


class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalizar")
