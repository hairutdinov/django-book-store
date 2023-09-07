from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book-detail/<int:_id>', views.book_detail, name='book-detail'),
]
