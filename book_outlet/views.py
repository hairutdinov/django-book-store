from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import ObjectDoesNotExist

# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books
    })


def book_detail(request, slug: str):
    # try:
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book,
    })
    # except ObjectDoesNotExist:
    #     raise Http404()
