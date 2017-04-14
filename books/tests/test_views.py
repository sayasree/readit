from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from books.views import list_books
from books.factories import AuthorFactory, BookFactory, ReviewFactory


class TestListBooks(TestCase):
    def test_list_books_url(self):
        url = resolve("/")
        self.assertEqual(url.func, list_books)
        
    def test_list_books_template(self):
        response = self.client.get(reverse(list_books))
        self.assertTemplateUsed(response, 'list.html')
        
    def test_list_books_returns_with_reviews(self):
        # setup the data required
        author = AuthorFactory()
        books_with_reviews = ReviewFactory.create_batch(2, authors=[author,])
        books_without_reviews = BookFactory.create_batch(4, authors=[author,])
        
        response = self.client.get(reverse(list_books))
        books = list(response.context['books'])
        
        self.assertEqual(books_with_reviews, books)
        self.assertNotEqual(books_without_reviews, books)