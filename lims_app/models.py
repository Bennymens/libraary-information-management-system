from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id = models.CharField(max_length=100)
    reader_name = models.CharField(max_length=200)
    reader_email = models.EmailField(max_length=100)
    reader_address = models.TextField(default='')
    active = models.BooleanField(default=True)

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('Comics', 'Comics'),
        ('Christian', 'Christian'),
        ('Children', 'Children'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Fantasy', 'Fantasy'),
        ('Biography', 'Biography'),
        # Add more genres as needed
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES, default='fiction')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    file = models.FileField(upload_to='books/', blank=True, null=True)  # For PDF/ebook files
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # <-- Add this line

    def __str__(self):
        return self.title