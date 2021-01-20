from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookShop

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def second(request):
    books = BookShop.objects.all()
    return render(request, "books.html", {"books": books})


def add_todo(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)


def add_book(request):
    form = request.POST
    title = form['book_title']
    subtitle = form['book_subtitle']
    description = form['book_description']
    price = form['book_price']
    genre = form['book_genre']
    author = form['book_author']
    year = form['book_year']
    book = BookShop(title = title,subtitle = subtitle,description = description,price = price,genre = genre,author = author,year = year)
    book.save()
    return redirect(second)


def delete_book(request, id):
    book = BookShop.objects.get(id=id)
    book.delete()
    return redirect(second)


def mark_book(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(second)


def unmark_book(request, id):
    book = BookShop.objects.get(id=id)
    book.is_favorites = False
    book.save()
    return redirect(second)


def books_detail(request, id):
    book = BookShop.objects.get(id=id)
    return render(request, "books_detail.html", {"book": book})
