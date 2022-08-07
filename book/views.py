from django.shortcuts import render, get_object_or_404
from .models import Book




def book_list(request):
     books = Book.published.all()
     # print(posts)

     return render(request, 'books/BookList.html', {'books':books})


def book_detail(request,id ):

     book = get_object_or_404(Book, 
                              id=id,
                              status='published',
                                )
     return render(request, 'books/BookDetail.html',{'book':book})