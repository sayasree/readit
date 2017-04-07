from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Author, Book
from .forms import ReviewForm

from django.views.generic import View, DetailView
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

    
# The following is a class-based view    
class AuthorList(View):
    def get(self, request):
        # authors = Author.objects.all()
        authors = Author.objects.annotate(
                                published_books=Count('books')
                        ).filter(published_books__gt = 0)
                                        
        context = { 'authors' : authors, }
        return render(request, "authors.html", context)
   
# This is class-based generic view
class BookDetail(DetailView):
    model = Book
    template_name = "book.html"
    
# This is class-based generic view
class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"
    
# The following is a function-based view
def review_books(request):
	"""
	List all of the books that we want to review.
	"""
	books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
	
	context = {
		'books': books,
	}
	
	return render(request, "list-to-review.html", context)
	
# The following is a function-based view
def review_book(request, pk):
	"""
	Review an individual book
	"""
	book = get_object_or_404(Book, pk=pk)
	form = ReviewForm
    
	context = {
		'book': book,
        'form': form,
	}
	
	return render(request, "review-book.html", context)
	
 
    