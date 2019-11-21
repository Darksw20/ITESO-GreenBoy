from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User,Greenhouse,Graphs
from django.db.models import Q
from .serializers import UserSerializer,GreenhouseSerializer,GraphSerializer


class AuthLogin(APIView):
    def get(self,request):
        print(request)
        user1 = User.objects.all()
        serializer = UserSerializer(user1,many=True)
        return Response(serializer.data)
    def post(self,request):
        user1 = User.objects.filter(Q(username=request.data["user"])&Q(password=request.data["passw"]))
        if user1.count() == 1:
            print("Ingreso"+ user1["id_user"])
            #request.session["id_user"] = user1["id_user"]
            serializer = UserSerializer(user1,many=True)
            return Response(1)
        elif user1.count() == 0:
            print("Invalid user")
            return Response(0)
        else:
            print("BD ERROR")
            return Response(0)
class Register(APIView):
    def post(self,request):
        user1 = User.objects.filter(Q(username=request.data["user"])|Q(password=request.data["email"]))
        if user1.count() >= 1:
            print("Ya existe el usuario")
            return Response(0)
        elif user1.count() == 0:
            print("Usuario no existe")
            userinsert = User.objects.create(username=request.data["user"],password=request.data["passw"],email=request.data["email"])
            userinsert.save()
            return Response(1)
        else:
            print("BD ERROR")
            return Response(0)
        
    #greenhouse1 = Greenhouse.objects.filter(fk_id_user_id=user1[0].id_user)
     #       print(greenhouse1)

class GetInfoGreen(APIView):
    def get(self,response):
        pass

def index(request):
    return render(request,"login/login.html")
def register(request):
    return render(request,"register/register.html")
def dashboard(request):
    return render(request,"dashboard/dash.html")

# Create your views here.
