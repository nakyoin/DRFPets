from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Pets)
admin.site.register(StatusOf)
admin.site.register(Category)
admin.site.register(TypeOf)
admin.site.register(OrderOf)
admin.site.register(OrderStatus)
