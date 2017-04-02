# This creates records in the books model

# Run this code after running the command: 
#   python manange.py shell

from books.models import Book

mybook = Book(title="Introduction to Python", author="Sreeni Saya", review="Awesome")
mybook.save()

mybook = Book(title="Introduction to Django", author="Sreeni Saya", review="Very Good")
mybook.save()

mybook = Book(title="Introduction to Yoga", author="Varnika Saya", review="Very Good")
mybook.save()

# Get all the books with:  Book.objects.all()

for i, book in enumerate(Book.objects.all()):
    print("Book-{}: {}".format(i, book))
    
# Filtering by an author
for i, book in enumerate(Book.objects.filter(author="Varnika Saya")):
    print("Book-{}: {}".format(i, book))
    
for i, book in enumerate(Book.objects.filter(author__contains="Saya")):
    print("Book-{}: {}".format(i, book))
    
for i, book in enumerate(Book.objects.filter(author__startswith="Sreeni")):
    print("Book-{}: {}".format(i, book))    
    
for i, book in enumerate(Book.objects.filter(author__endswith="Saya")):
    print("Book-{}: {}".format(i, book))    

# Filter chaining
for i, book in enumerate(Book.objects.filter(author__endswith="Saya").filter(title__contains="Python")):
    print("Book-{}: {}".format(i, book))  
    
    