from django.shortcuts import render
from .models import Books


def book (request):
    return render(request,'Books/book.html')



def books (request):
    return render(request,'Books/books.html', {'Book':Books.objects.all()})
