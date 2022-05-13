from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
<<<<<<< HEAD

from django.shortcuts import render, redirect
from django.contrib.auth import logout
=======
>>>>>>> aebad852be2e87463ef7fb34d56d042c603f1f40

# Create your views here.

def index(request):
    hotels = Hotel_Branches.objects.all()
    context = {'hotels':hotels}
    return render(request, 'dbcep/index.html',context)

def reservation(request):
    books = Booking.objects.all()
    context1 = {'books':books}
    return render(request, 'dbcep/reservation.html',context1)


def about(request):
    return render(request,'dbcep/about.html')

def contact(request):
    return render(request,'dbcep/contact.html')

def gallery(request):
    return render(request,'dbcep/gallery.html')

def menu(request):
    return render(request,'dbcep/menu.html')

<<<<<<< HEAD


def signup_user(request):
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
>>>>>>> aebad852be2e87463ef7fb34d56d042c603f1f40
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
<<<<<<< HEAD
            return render(request, 'dbcep/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'dbcep/signup.html', {'form': form})

def signin_user(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
=======
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
>>>>>>> aebad852be2e87463ef7fb34d56d042c603f1f40
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
<<<<<<< HEAD
            return render(request, 'dbcep/signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'dbcep/signin.html', {'form': form})



def signout_user(request):
=======
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import logout

def signout(request):
>>>>>>> aebad852be2e87463ef7fb34d56d042c603f1f40
    logout(request)
    return redirect('/')

    