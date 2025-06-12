from django.shortcuts import render, redirect
from .models import reader
from django.db.models import Q

def home(request):
    return render(request, 'home.html', {
        "title": "Home",
        "current_tab": "home"
    })

def readers(request):
    query = request.GET.get('q', '')
    if query:
        readers_list = reader.objects.filter(
            Q(reader_name__icontains=query) |
            Q(reader_email__icontains=query) |
            Q(reference_id__icontains=query)
        )
    else:
        readers_list = reader.objects.all()

    if request.method == 'POST':
        reader.objects.create(
            reader_name=request.POST['reader_name'],
            reader_email=request.POST['reader_email'],
            reference_id=request.POST['reference_id'],
            reader_address=request.POST['reader_address'],
            active=True
        )
        return redirect('readers')

    return render(request, 'readers.html', {
        "title": "Readers",
        "current_tab": "readers",
        "readers": readers_list,
        "query": query,
    })