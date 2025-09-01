# Book API view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def book_list_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
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

    # Add this line to get only active readers
    active_readers = [r for r in readers_list if r.active]

    return render(request, 'readers.html', {
        "title": "Readers",
        "current_tab": "readers",
        "readers": readers_list,
        "active_readers": active_readers,  # <-- add this
        "query": query,
    })

def books(request):
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre=genre)
    else:
        books = Book.objects.all()
    genres = Book.GENRE_CHOICES
    return render(request, 'books.html', {
        "books": books,
        "genres": genres,
        "selected_genre": genre,
        "title": "Books",
        "current_tab": "books"
    })

def mybag(request):
    return render(request, 'mybag.html', {"title": "My Bag", "current_tab": "mybag"})

def returns(request):
    return render(request, 'returns.html', {"title": "Returns", "current_tab": "returns"})