from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import CommentForm


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.book = book
            new_comment.save()
            form = CommentForm()
    
    else:
        form = CommentForm()

    context = {
        'book': book,
        'comments':comments,
        'form': form,
    }
    return render(request, 'books/book_detail.html', context=context)


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price', 'cover']
    success_url = reverse_lazy('book_list')


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'price', 'cover']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
