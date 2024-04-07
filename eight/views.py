from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect

from .models import Book, BorrowedBook, Register
from .forms import BorrowBookForm, RegisterBook, RegisterUserForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_users")
    else:
        form = RegisterUserForm()
    return render(request, 'add_user.html', {'form': form})

def allUsers(request):
    users_data = Register.objects.all()
    return render(request, 'all_users.html',{'users':users_data})

def addBook(request):
    if request.method == 'POST':
        form = RegisterBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_books')
    else:
        form = RegisterBook()
    return render(request, 'books/add_book.html', {'form': form})

def allBooks(request):
    books_data = Book.objects.all()
    return render(request, 'books/all_books.html', {'books': books_data})


#These views handle the book borrowing request
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





def borrowedBooks(request):
    borrowed_books_data = BorrowedBook.objects.all()
    return render(request, 'books/borrowed_book.html', {'borrowed_books': borrowed_books_data})

def borrowFail(request):
    return render(request, 'books/borrow_fail.html')


#These views handle the book Return 
def returnBook(request, pk):
    record = BorrowedBook.objects.get(id=pk)
    if record.user == request.user and not record.returned:
        record.return_date = datetime.now().date()
        record.returned = True
        record.save()
        return redirect('book_return_success')
    else:
        return redirect('book_return-fail')
    

def returnSuccess(request):
    return render(request, 'return_success.html')

def returnFailure(request):
    return render(request, 'return_fail.html')


# def borrowBook(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         form = BorrowBookForm(request.POST)
#         if form.is_valid():
#             # client = form.cleaned_data['client_name']
#             # BorrowedBook.objects.create( client=client)
#             form.save()
#             return redirect('borrowed_book')
#     else:
#         form = BorrowBookForm()
#     return render(request, 'books/borrow_book.html', {'form': form})


