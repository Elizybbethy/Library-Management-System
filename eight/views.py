from datetime import datetime
from django.shortcuts import render, redirect

from .models import Book, BorrowedBook, Register
from .forms import BorrowBookForm, RegisterBook, RegisterUserForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

#This view handles user registration
def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_users")
    else:
        form = RegisterUserForm()
    return render(request, 'add_user.html', {'form': form})

#This view is querying all the registered users
def allUsers(request):
    users_data = Register.objects.all()
    return render(request, 'all_users.html',{'users':users_data})

#This view handles book registration
def addBook(request):
    if request.method == 'POST':
        form = RegisterBook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            genre = form.cleaned_data['genre']
            copies_number = form.cleaned_data['copies_number']
            availability = form.cleaned_data['availability']  
            existing_book = Book.objects.filter(Title=title, genre=genre).first()
            if existing_book:
                # If the book already exists update the copies_number and availability
                existing_book.copies_number += copies_number
                existing_book.availability = availability
                existing_book.save()
            else:
                # If the book doesn't exist, a new record is created
                form.save()
            return redirect("all_books")
        else:
            print(form.errors)
    else:
        form = RegisterBook()
    return render(request, 'books/add_book.html', {'form': form})


def allBooks(request):
    books_data = Book.objects.all()
    return render(request, 'books/all_books.html', {'books': books_data})


#This view handle the book borrowing request
def borrowBook(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrowing_book = form.save(commit=False)
            book = borrowing_book.book
            if book.copies_number > 0:
                book.copies_number -= 1
                book.save()
                borrowing_book.save()
                return redirect('borrowed_book')
    else:
        form = BorrowBookForm()
    return render(request, 'books/borrow_book.html', {"form": form})




#This view is for all borrowed books
def borrowedBooks(request):
    borrowed_books_data = BorrowedBook.objects.all()
    return render(request, 'books/borrowed_book.html', {'borrowed_books': borrowed_books_data})



#This view handle the book Return 
def returnBook(request, pk):
    record = BorrowedBook.objects.get(id=pk)
    if record.user == request.user and not record.returned:
        record.return_date = datetime.now().date()
        record.returned = True
        record.save()
        return redirect('book_return_success')
    else:
        return redirect('book_return-fail')
    







