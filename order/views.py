from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse


class PayOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Pagar")


class CloseOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Fechar Pedido")


class Detail(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe")
