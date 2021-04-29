from django.contrib import admin
from django.urls import path
from Myapp import views

app_name = 'Myapp'

urlpatterns = [
    path('', views.index, name ='index'),
    #book/1 or book/2 or book/3 .....
    path('book/<int:book_id>/', views.detail, name = 'Detail'),
    path('add/', views.add_book, name = 'add_book'),
    path('update/<int:id>/', views.update, name = 'update'),
    path('delete/<int:id>/', views.delete, name = 'delete'),
]