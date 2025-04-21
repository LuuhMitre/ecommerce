from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


class Create(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Criar")


class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Atualizar")


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Login")


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Logout")
