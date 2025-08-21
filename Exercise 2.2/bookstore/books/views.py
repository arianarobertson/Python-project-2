from django.views.generic import ListView
from .models import Book
from django.views.generic import DetailView

class BookListView(ListView):
    model = Book
    template_name = 'books/main.html'  # points to books/templates/books/main.html

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'