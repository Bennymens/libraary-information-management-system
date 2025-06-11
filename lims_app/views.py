from django.shortcuts import render
from django.http import HttpResponse
from .models import reader  # use the correct model name (lowercase 'r')

def home(request):
    return render(request, 'home.html', {
        "title": "Home",
        "current_tab": "home"
    })

def readers(request):
    readers_list = reader.objects.all()
    return render(request, 'readers.html', {
        "title": "Readers",
        "current_tab": "readers",
        "readers": readers_list
    })