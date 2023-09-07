from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import ObjectDoesNotExist
from django.db.models import Avg, Max, Min

# Create your views here.


def index(request):
    books = Book.objects.all()
    total_num_of_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_number_of_books': total_num_of_books,
        'average_rating': avg_rating['rating__avg'],
    })


def book_detail(request, slug: str):
    # try:
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'book': book,
    })
    # except ObjectDoesNotExist:
    #     raise Http404()
