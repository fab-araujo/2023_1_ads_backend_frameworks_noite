from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo!")

def detail(request):
    return HttpResponse("Página detail!")

def contact(request):
    return HttpResponse("Página contact!")