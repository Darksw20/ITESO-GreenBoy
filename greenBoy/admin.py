from django.contrib import admin
from .models import User,Graphs,Greenhouse

# Register your models here.
admin.site.register(User)
admin.site.register(Graphs)
admin.site.register(Greenhouse)