from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    return HttpResponse("Logged in User is: {}".format(request.user.username))
