from django.urls import path
from .views import RegisterUser, addBook, allBooks, allUsers, borrowBook, borrowedBooks, homepage, returnBook

urlpatterns = [
    path('', homepage, name="home"),

    #These urls are for user related routes
    path('user_add', RegisterUser, name="user_add"),
    path('all_users/', allUsers, name="all_users"),

    #These urls are for book related routes
    path('add_book', addBook, name="add_book"),
    path('all_books/', allBooks, name="all_books"),

    #These urls are for book borrowing related routes
    path('borrow/', borrowBook, name="borrow"),
    path('borrowed/', borrowedBooks, name="borrowed_book"),
 

    #The urls are for borrowed book returns
    path('return', returnBook, name="return"),

]
