from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request, 'Myapp/index.html',context)

def detail(request, book_id):
    book_detail = Book.objects.get(id = book_id)
    return render(request,'Myapp/detail.html',{'book_detail':book_detail})
    