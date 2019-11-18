from django.contrib import admin
from .models import User,graphs,greenhouse

# Register your models here.
admin.site.register(User)
admin.site.register(graphs)
admin.site.register(greenhouse)