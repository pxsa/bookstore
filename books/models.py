from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])