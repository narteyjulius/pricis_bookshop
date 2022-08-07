from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [

     path('product/<uuid:id>', views.book_detail, name='book_detail'),

     path('', views.book_list, name='book_list'),

]