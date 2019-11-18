from django.urls import path
from rest_framework.routers import DefaultRouter
#from .views import UserViewSet
from . import views

router = DefaultRouter()
#router.register('user',UserViewSet,base_name='user')

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register',views.register,name = 'register'),
    path('dash',views.dashboard,name = 'dashboard'),
    path('webservices/',views.UserList.as_view()),
    path('webservices/signin',views.UserList.as_view())

]