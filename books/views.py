from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_queryset(self):
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        return Book.objects.filter(id=book.id)
    

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price']


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books')
