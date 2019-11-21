from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from . import views

router = DefaultRouter()

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register',views.register,name = 'register'),
    path('dash',views.dashboard,name = 'dashboard'),
    path('webservices/signin',views.AuthLogin.as_view()),
    path('webservices/register',views.Register.as_view()),

    path('webservices/getConfig',views.AuthLogin.as_view()),
    path('webservices/newData',views.AuthLogin.as_view()),

    path('webservices/getInfoGreen',views.GetInfoGreen.as_view()),
    
    path('webservices/newGreen',views.AuthLogin.as_view()),
    path('webservices/delGreen',views.AuthLogin.as_view()),

    path('webservices/getDataGreen',views.AuthLogin.as_view()),
    path('webservices/setDataGreen',views.AuthLogin.as_view()),

]