from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(null=False, blank=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name