from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Post

# Create your views here.
def index(request):
    postsQuerySet=Post.objects.all()
    return render(request, 'index.html', {'posts': postsQuerySet})

    #return HttpResponse("Hello, World");
    #bookQuerySet=Book.objects.all()
    #return render(request, 'index.html', {'books': bookQuerySet})

def detail(request, book_id):
    return HttpResponse(book_id)