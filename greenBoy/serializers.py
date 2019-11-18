from rest_framework.serializers import ModelSerializer

from .models import User,greenhouse,graphs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user','username','password')

class GreenhouseSerializer(ModelSerializer):
    class Meta:
        model = greenhouse
        fields = ('id_green','temp_max','temp_min','hum_max','hum_min','fk_id_user')

class GraphSerializer(ModelSerializer):
    class Meta:
        model = graphs
        fields = ('id_graph','time','temp','hum','fk_id_green')