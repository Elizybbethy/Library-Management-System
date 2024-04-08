from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Count
from django.utils import timezone

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
    user_count = users_data.count()
    return render(request, 'all_users.html',{'users':users_data, 'user_count': user_count})

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
    total_books = books_data.count()
    return render(request, 'books/all_books.html', {'books': books_data, 'total_books': total_books, })


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



#This view handles the book Return 
def returnBook(request, pk):
    record = BorrowedBook.objects.get(id=pk)
    if record.user == request.user and not record.returned:
        record.return_date = datetime.now().date()
        record.returned = True
        record.save()
        return redirect('book_return_success')
    else:
        return redirect('book_return-fail')
    

#This view handles the summary of inventory
def inventory(request):
    total_books = Book.objects.count() # for total books
    user_count = Register.objects.count() # for Users 
    available_books = Book.objects.filter(availability=True) # Available books for borrowing
    # for overdue books and a client 
    overdue_books = BorrowedBook.objects.filter(return_date__isnull=False, return_date__lt=timezone.now())
    # for popular book in the library
    popular_book = Book.objects.annotate(num_borrowed=Count('borrowedbook')).order_by('-num_borrowed').first()
    #for popular genre in the library
    popular_genre = Book.objects.values('genre').annotate(num_books=Count('id')).order_by('-num_books').first()
    context = {
        'total_books': total_books,
        'user_count': user_count,
        'available_books': available_books,
        'overdue_books': overdue_books,
        'popular_book': popular_book,
        'popular_genre': popular_genre['genre'] if popular_genre else None
    }
    return render(request, 'inventory.html', context)





