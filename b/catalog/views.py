from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status = 'a').count()
    num_authors = Author.objects.all().count
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    while num_visits == 20:
        num_visits = 0
        request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_visits': num_visits,
                 }
        )   


class BookListView(generic.ListView):
    model = Book
    #context_object_name = 'my_book_list'
    #queryset = Book.objects.filter(title__icontains = 'war')[:5]
    #template_name = 'books/my_arbitrary_template_name_list.html'
    #def get_queryset(self):
        #return Book.objects.filter(title__icontains = 'war')[:5]
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact='o').order_by('due_back')
    
