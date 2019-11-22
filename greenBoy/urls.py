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
    path('webservices/getInfoGreen',views.GetInfoGreen.as_view()),
    path('webservices/InvAPI',views.InvAPI.as_view()),

    path('webservices/newGreen',views.NewGreen.as_view()),
    path('webservices/delGreen',views.DelGreen.as_view()),
    path('webservices/setDataGreen',views.setDataGreen.as_view()),

]