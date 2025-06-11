from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def home(request):
    return render(request, 'home.html', {
        "title": "Home",
        "current_tab": "home"
    })

def readers(request):
    return render(request, 'readers.html', {
        "title": "Readers",
        "current_tab": "readers"
    })

def readers_tab(request):
    readers=reader.objects.all()
    return render(request, 'readers_tab.html',
                  context= {"current_tab": "readers", "readers": readers})