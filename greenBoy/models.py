from django.db import models

# Create your models here.
class User(models.Model,):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40,default="")

    def __str__(self):
        return self.username

class Greenhouse(models.Model,):
    id_green = models.AutoField(primary_key=True)
    greenName = models.CharField(max_length=40,default="")
    temp_max = models.FloatField()
    temp_min = models.FloatField()
    hum_max = models.FloatField()
    hum_min = models.FloatField()
    fk_id_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_green)

class Graphs(models.Model,):
    id_graph = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()
    hum = models.FloatField()
    fk_id_green = models.ForeignKey(Greenhouse,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_graph)