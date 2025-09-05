from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'у нас большой выбор книг, у Читай-города меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available =\
        BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects
    num_author = Author.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session['num_visits'] = num_visits + 1
    context = {'text_head': text_head,
               'books': books, 'num_books':num_books,
               'num_instance': num_instance,
               'num_instance_available': num_instance_available,
               'author': author, 'num_author': num_author,
               'num_visits': num_visits}
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'


def about(request):
    text_head = 'у нас большой выбор книг, у Читай-города меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available =\
        BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects
    num_author = Author.objects.count()
    context = {'text_head': text_head,
               'books': books, 'num_books':num_books,
               'num_instance': num_instance,
               'num_instance_available': num_instance_available,
               'author': author, 'num_author': num_author}
    return render(request, 'catalog/about.html')


def contact(request):
    text_head = 'у нас большой выбор книг, у Читай-города меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available =\
        BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects
    num_author = Author.objects.count()
    context = {'text_head': text_head,
               'books': books, 'num_books':num_books,
               'num_instance': num_instance,
               'num_instance_available': num_instance_available,
               'author': author, 'num_author': num_author}
    return render(request, 'catalog/contact.html', context)