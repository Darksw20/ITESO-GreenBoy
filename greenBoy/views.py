from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. Esto anda comenzando")

# Create your views here.
