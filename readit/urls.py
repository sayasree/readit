"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from books.views import list_books, AuthorList, BookDetail, AuthorDetail
from books.views import review_book, review_books


# Access the pages with the following URLs
#   http://127.0.0.1:8000/
#   http://127.0.0.1:8000/admin
#   http://127.0.0.1:8000/authors/
#   http://127.0.0.1:8000/books/3
#   http://127.0.0.1:8000/authors/1

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books, name="books"),
    url(r'^authors/$', AuthorList.as_view(), name="authors"),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name="book-detail"),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name="author-detail"),

    url(r'^review/$', review_books, name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
    
]

from django.conf import settings
from django.conf.urls import include

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^debug/', include(debug_toolbar.urls)),] + urlpatterns
    
    