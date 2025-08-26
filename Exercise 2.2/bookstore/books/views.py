from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book
from django.views.generic import DetailView

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/main.html'  # points to books/templates/books/main.html

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'