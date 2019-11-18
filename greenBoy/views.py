from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User,greenhouse,graphs
from .serializers import UserSerializer,GreenhouseSerializer,GraphSerializer

class UserList(APIView):
    def get(self,request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1,many=True)
        return Response(serializer.data)

def index(request):
    return render(request,"login/login.html")
def register(request):
    return HttpResponse("Hello World. Registro conectado")
def dashboard(request):
    return HttpResponse("Hello World. Dashboard conectado")

# Create your views here.
