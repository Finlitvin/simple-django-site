from django.shortcuts import render
from .models import Book


def index(request):
    num_books = Book.objects.all().count()
    books = Book.objects.all()

    return render(
        request,
        'index.html',
        context = {'num_books':num_books, 'books': books}
    )

def about(request, pk):
    about_book = Book.objects.get(pk=pk)

    return render(
        request,
        'about_book.html',
        context = {'about_book': about_book}
    )