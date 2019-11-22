from rest_framework.serializers import ModelSerializer

from .models import User,Greenhouse,Graphs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user','username','password','email')

class GreenhouseSerializer(ModelSerializer):
    class Meta:
        model = Greenhouse
        fields = ('id_green','temp_max','temp_min','hum_max','hum_min','fk_id_user','greenName')

class GraphSerializer(ModelSerializer):
    class Meta:
        model = Graphs
        fields = ('id_graph','time','temp','hum','fk_id_green')