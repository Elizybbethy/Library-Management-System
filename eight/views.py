from django.shortcuts import render, redirect

from .models import Register
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def RegisterUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_users")
    else:
        form = RegisterForm()
    return render(request, 'add_user.html', {'form': form})

def allUsers(request):
    users_data = Register.objects.all()
    return render(request, 'all_users.html',{'users':users_data})