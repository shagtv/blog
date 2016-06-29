from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from pin.forms import PinForm


def index(request):
    form = PinForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'pin/index.html', {"form": form})
