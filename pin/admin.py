from django.contrib import admin

from django.contrib import admin
from .models import Pin, Type, Category, Channel, Log

admin.site.register(Pin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(Log)
