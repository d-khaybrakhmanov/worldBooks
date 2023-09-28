from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre

def index(request):
    # генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # доступные книги (статус = "на складе"
    # здесь метод 'all()' применен по умолчанию
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # авторы книг
    num_author = Author.objects.count()
    # отрисовка html шаблона index.html с данными
    # внутри переменной context
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_availavle': num_instances_available,
                           'num_author': num_author}
                  )