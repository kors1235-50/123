from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.BookListView.as_view(), name = 'books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name = 'book-detail'),
    path('author/',views.AuthorListView.as_view(), name = 'author'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name = 'author-detail'),
    
]
urlpatterns +=[
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    ]

urlpatterns +=[
    path('book/<uuid:pk>/renew/',views.renew_book_librarian , name'renew-book-librarian'),
    ]
