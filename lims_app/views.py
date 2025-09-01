from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        from django.contrib import messages
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')
    return render(request, 'edit_profile.html', {
        "title": "Edit Profile",
        "current_tab": "profile"
    })
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html', {
        "title": "Profile",
        "current_tab": "profile"
    })

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('login')
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    return render(request, 'register.html', {
        "title": "Register",
        "current_tab": "register"
    })
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            from django.contrib import messages
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html', {
        "title": "Login",
        "current_tab": "login"
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