from django.shortcuts import render
# from django.http import HttpResponse
from .models import Author, Book

from django.views.generic import View
from django.db.models import Count

# Create your views here.
# The following is a function-based view
def list_books(request):
    '''
    List the books that have the reviews
    '''
    #books = Book.objects.exclude(date_reviewed__isnull=True)
    books = Book.objects.all().exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = { 'books' : books, }
    
    #return HttpResponse("Logged in User is: {}".format(request.user.username))
    return render(request, "list.html", context)

    
class AuthorList(View):
    def get(self, request):
        # authors = Author.objects.all()
        authors = Author.objects.annotate(
                                published_books=Count('books')
                        ).filter(published_books__gt = 0)
                                        
        context = { 'authors' : authors, }
        return render(request, "authors.html", context)