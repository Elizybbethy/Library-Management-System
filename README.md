#Project Name:
Library-Management-System

#Functionalities:
User registration,
User management,
Books registration,
Book management,
Book Borrowing and return,

#Installation
git clone https://github.com/Elizybbethy/Library-Management-System.git
Then Cd fifty

#Install dependencies 
pip install -r requirements.txt

#Run database migrations:
python manage.py migrate

#Start the development server:
python manage.py runserver

#navbar links:
LBM - This redirects to the inventory page that shows the Libray inventory
 - Total Number of Books in the Library
 - Users in the System
 -Popular Book in the Library
 - Popular Genre in the Library
 - Available Books for Borrowing
 - Overdue Books
 And it is still a default landing page after cicking on get started.

Users - This has several options
 - Add New User
 - All Users

Books - This also has several options
 - Add New Book
 - All Books
 - Borrow Book
 - Borrowed Books