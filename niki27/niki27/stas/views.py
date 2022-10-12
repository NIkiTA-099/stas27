from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.core import serializers
from django.http import JsonResponse

from django.views.generic import ListView


def PostHome(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
           form.save()
    return render(request, 'stas/home.html', {'form': form})


def MyView(request):
    post = Value.objects.all()
    post_json = serializers.serialize('json', post)
    return HttpResponse(post_json, content_type='application/json')
