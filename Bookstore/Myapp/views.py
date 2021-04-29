from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookStore
from .forms import BookStoreForm

# Create your views here.

def index(request):

    book_list = BookStore.objects.all()

    context = {
        'book_list':book_list
    } 
    
    return render(request, 'Myapp/index.html', context)

def detail(request, book_id):

    book = BookStore.objects.get(id = book_id)

    return render( request, 'Myapp/detail.html', {'book':book} )
    

def add_book(request):

    if request.method == "POST":
        
        name = request.POST.get('name',)
        decs = request.POST.get('decs',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = BookStore(name=name, decs=decs, price=price, book_image=book_image)
        book.save()
    return render(request, 'Myapp/add_book.html')

def update(request,id):
    book = BookStore.objects.get(id = id)
    form = BookStoreForm(request.POST or None, request.FILES, instance = book)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'Myapp/edit.html', {'form':form , 'book':book})


def delete(request, id):

    if request.method == "POST":
        book = BookStore.objects.get(id = id)
        book.delete()
        return redirect('/')



    return render(request, 'Myapp/delete.html')