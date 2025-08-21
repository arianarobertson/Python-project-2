from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            id=1,
            name="Book One",
            author_name="Author One",
            price=12.99,
            genre='ro',
            book_type='hc',
            pic='no_picture.jpg'
        )
        self.book2 = Book.objects.create(
            id=2,
            name="Book Two",
            author_name="Author Two",
            price=8.99,
            genre='fa',
            book_type='eb',
            pic='no_picture.jpg'
        )

    def test_get_absolute_url_book1(self):
        self.assertEqual(self.book1.get_absolute_url(), '/books/list/1/')

    def test_get_absolute_url_book2(self):
        self.assertEqual(self.book2.get_absolute_url(), '/books/list/2/')

