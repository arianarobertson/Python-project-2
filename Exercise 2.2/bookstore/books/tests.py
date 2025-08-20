from django.test import TestCase
from .models import Book

# Create your tests here.

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create one test book object
        Book.objects.create(
            name='Pride and Prejudice',
            author_name='Jane Austen',
            genre='classic',
            book_type='hardcover',
            price=23.71
        )

    def test_book_name_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author_name').max_length
        self.assertEqual(max_length, 120)

    def test_object_str_method(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.name
        self.assertEqual(str(book), expected_object_name)
