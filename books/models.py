from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('book', args=[self.id])