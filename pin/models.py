#!/user/bin/env python3
# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User


class Channel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    length = models.IntegerField(default=10)
    
    def __str__(self):
        return self.title


class Pin(models.Model):
    pin = models.CharField(max_length=30, unique=True)
    generated = models.DateTimeField(auto_now=False, auto_now_add=True)
    activated = models.DateTimeField(auto_now=False, auto_now_add=False, default=None, null=True, blank=True)
    type = models.ForeignKey(Type)
    channel = models.ForeignKey(Channel)
    user = models.ForeignKey(User, null=True, default=None, blank=True)
    
    def __str__(self):
        return self.pin


class Log(models.Model):
    pin = models.ForeignKey(Pin)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User)
