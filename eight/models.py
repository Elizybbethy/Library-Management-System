from django.utils import timezone
from django.db import models

# This model is for user registration.
class Register(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
    
#This model is for book registration
class Book(models.Model):
    Title = models.CharField(max_length=100, blank=False, null=False)
    genre = models.CharField(max_length=50, blank=False, null=False)
    availability = models.BooleanField(default=True)
    copies_number = models.IntegerField(default=1)

    def __str__(self):
        return self.Title
    

#This model is for borrowing books
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100, blank=False, null=False)
    book_copies = models.IntegerField(default=0)
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    returned = models.BooleanField(default=False)
    
    def save(self, **args):
        if not self.pk:
            self.book.copies_number -= 1
            self.book.save()
        super().save(**args)

    def __str__(self):
        return str(self.book)
