from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from .models import Author, Book
from .forms import ReviewForm, BookForm

from django.views.generic import View, DetailView
from django.db.models import Count
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView

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
#def review_books(request):
class ReviewList(View):

    """
    List all of the books that we want to review.
    """
    def get(self, request):
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

        context = {
            'books': books,
            'form' : BookForm
        }

        return render(request, "list-to-review.html", context)
        
    def post(self, request):
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('review-books')
        
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
        context = {
            'books': books,
            'form' : form
        }  
        
        return render(request, "list-to-review.html", context)

# The following is a function-based view
def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book.is_favourite = form.cleaned_data['is_favourite']
            book.review = form.cleaned_data['review']
            book.save()
            return redirect('review-books')
    else:
        form = ReviewForm   
    
    context = {
        'book': book,
        'form': form,
    }

    return render(request, "review-book.html", context)

class CreateAuthor(CreateView):
    model = Author
    fields = ['name',]
    template_name = 'create-author.html'
    
    def get_success_url(self):
        return reverse('review-books')
  