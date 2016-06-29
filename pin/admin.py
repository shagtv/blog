#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Pin, Type, Category, Channel, Log, Item, Bonus

admin.site.register(Pin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(Log)
admin.site.register(Item)
admin.site.register(Bonus)
