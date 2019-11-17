from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. Esto anda comenzando")
def register(request):
    return HttpResponse("Hello World. Registro conectado")
def dashboard(request):
    return HttpResponse("Hello World. Dashboard conectado")

# Create your views here.
