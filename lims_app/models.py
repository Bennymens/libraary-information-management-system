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