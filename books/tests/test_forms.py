from django.test import TestCase
from django.core.exceptions import NON_FIELD_ERRORS
from books.forms import ReviewForm, BookForm
from books.factories import AuthorFactory, BookFactory

class ReviewFormTest(TestCase):
    def test_no_review(self):
        form = ReviewForm(data={ 'is_favourite' : False })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('review', code='required'))
        
    def test_review_too_short(self):
        form = ReviewForm(data={ 'is_favourite' : False, 'review' : 'short review' })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('review', code='min_length'))

class BookFormTest(TestCase):
    def setUp(self):
        self.author = AuthorFactory()
        self.book = BookFactory(title='My Book', authors=[self.author,])
        
    def test_custom_validation_rejects_book_that_already_exists(self):
        form = BookForm(data={'title' : 'My Book', 'authors': [self.author.pk,]})
        
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, code='BookExists'))
        
    def test_custom_validation_accepts_new_book(self):
        new_author = AuthorFactory()
        
        form = BookForm(data={'title' : 'My New Book', 'authors': [new_author.pk,]})

        self.assertTrue(form.is_valid())

        