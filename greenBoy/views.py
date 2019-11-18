from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User,greenhouse,graphs
from django.db.models import Q
from .serializers import UserSerializer,GreenhouseSerializer,GraphSerializer

import pdb


class UserList(APIView):
    def get(self,request):
        print(request)
        user1 = User.objects.all()
        serializer = UserSerializer(user1,many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request)
        user1 = User.objects.filter(Q(username="Darksw20")|Q(password="Prueba"))
        serializer = UserSerializer(user1,many=True)
        return Response(serializer.data)

def index(request):
    return render(request,"login/login.html")
def register(request):
    return render(request,"register/register.html")
def dashboard(request):
    return render(request,"dashboard/dash.html")

# Create your views here.
