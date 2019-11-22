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
        user1 = User.objects.all()
        serializer = UserSerializer(user1,many=True)
        return Response({"status":200,"message":"ALL_USERS_DELIVERED","data":serializer.data})

    def post(self,request):
        user1 = User.objects.filter(Q(username=request.data["user"])&Q(password=request.data["passw"]))
        if user1.count() == 1:
            request.session["id_user"] = user1[0].id_user
            request.session["user"] = user1[0].username
            return Response({"status":200, "message":"USER_AUTHENTICATED"})
        elif user1.count() == 0:
            return Response({"status":200, "message":"INVALID_USER"})
        else:
            return Response({"status":200, "message":"ERROR"})

class Register(APIView):
    def post(self,request):
        user1 = User.objects.filter(Q(username=request.data["user"])|Q(password=request.data["email"]))
        if user1.count() >= 1:
            return Response({"status":200,"message": "USER_ALREADY_EXIST"})
        elif user1.count() == 0:
            userinsert = User.objects.create(username=request.data["user"],password=request.data["passw"],email=request.data["email"])
            userinsert.save()
            request.session["id_user"] = userinsert.id_user
            request.session["user"] = userinsert.username
            return Response({"status":200,"message": "USER_REGISTRED"})
        else:
            return Response({"status":200,"message": "ERROR"})

class GetInfoGreen(APIView):
    def get(self,request):
        gH = Greenhouse.objects.filter(fk_id_user_id=request.session["id_user"])
        serializer = GreenhouseSerializer(gH, many=True)
        return Response({"status":200,"message":"GREEN_INFO_DELIVERED","user": request.session["user"],"greenData": serializer.data})
 
class InvAPI(APIView):
    def get(self,request):
        gH = Greenhouse.objects.filter(id_green=request.GET["id_green"])
        serializer = GreenhouseSerializer(gH, many=True)
        return Response({"status":200, "data": serializer.data,"message": "GREEN_CONFIG_DELIVERED"})

    def post(self,request):
        gH = Greenhouse(id_green=request.data["id_green"])
        graph = Graphs.objects.create(temp=request.data["temp"],hum=request.data["hum"],fk_id_green=gH)
        graph.save()
        return Response({"status":200,"message": "GRAPH_INSERTED"})

class NewGreen(APIView):
    def post(self,request):
        gHQ = Greenhouse.objects.filter(Q(greenName=request.data["greenName"])&Q(fk_id_user_id=request.session["id_user"]))
        if gHQ.count() == 0:
            #user = User(id_user=request.session["id_user"])
            gH = Greenhouse.objects.create(greenName=request.data["greenName"],temp_max=30.0,temp_min=25.0,hum_max=50.0,hum_min=45.0,fk_id_user_id=request.session["id_user"])
            gH.save()
            return Response({"status": 200,"message": "GREEN_CREATED"})
        else:
            return Response({"status": 200,"message": "GREEN_ALREADY_EXIST"})

class DelGreen(APIView):
    def post(self,request):
        Greenhouse.objects.filter(Q(greenName=request.data["greenName"])&Q(fk_id_user_id=request.session["id_user"])).delete()
        return Response({"status": 200,"message": "GREEN_DELETED"})

class setDataGreen(APIView):
    def post(self,request):
        gHQ = Greenhouse.objects.filter(Q(greenName=request.data["greenName"])&Q(fk_id_user_id=request.session["id_user"]))
        gHQ.update(temp_max = request.data["temp_max"])
        gHQ.update(temp_min = request.data["temp_min"])
        gHQ.update(hum_max = request.data["hum_max"])
        gHQ.update(hum_min = request.data["hum_min"])
        gHQ.update(greenName = request.data["nameInv"])
        return Response({"status": 200,"message": "GREEN_UPDATED"})

def index(request):
    return render(request,"login/login.html")
def register(request):
    return render(request,"register/register.html")
def dashboard(request):
    return render(request,"dashboard/dash.html")

# Create your views here.
