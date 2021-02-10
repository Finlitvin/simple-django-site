from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
#from .forms import AddBookForm
from .models import Book


class IndexView(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['num_books'] = Book.objects.all().count()
        return context

class BookAboutView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'about_book.html'

class BookCreate(CreateView):
    model = Book
    template_name = 'book_form.html'
    fields = '__all__'




######## or ########
#def add_book(request):
#    form = AddBookForm()
#
#    return render(
#        request,
#        'add_book.html',
#        {'form': form}
#    )

#def index(request):
#    num_books = Book.objects.all().count()
#    books = Book.objects.all()
#
#    return render(
#        request,
#        'index.html',
#        context = {'num_books':num_books, 'books': books}
#    )

#def about(request, pk):
#    about_book = Book.objects.get(pk=pk)
#
#    return render(
#        request,
#        'about_book.html',
#        context = {'about_book': about_book}
#    )