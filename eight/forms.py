from django import forms
from .models import Book, BorrowedBook, Register

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

class RegisterBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "Title",
            "genre",
            "copies_number",
            "availability",
        ]

class DateInput(forms.DateInput):
    input_type = "date"

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = [
            "book",
            "client_name",
            "book_copies",
            "return_date",
        ]
        widgets = {
            "return_date": DateInput(),
        }