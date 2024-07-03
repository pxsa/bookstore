from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price']
    success_url = reverse_lazy('book_list')
