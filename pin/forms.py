#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = [
            "pin",
        ]
