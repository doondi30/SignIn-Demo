from django.shortcuts import render, redirect
from .templates import *
from .models import CustomUser
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login



def login_page(request):
    return render(request, 'index.html')

def signup_page(request):
    return render(request, 'signup.html')
 
# def home(request):
#     return render(request, "homepage.html")

def signup(request):
    if request.method=="POST":
        mail=request.POST.get('email').strip().lower()
        password=request.POST.get('password')
        conf_pass=request.POST.get('conf_pass')
        
        if len(password)<8:
            messages.error(request, "Password should atleast contain 8 characters!")
            return redirect('signup_page')

        if password != conf_pass:
            messages.error(request, "Passwords do not match!")
            return redirect('signup_page')
        
        try:
            user = CustomUser.objects.create_user(username=mail, email=mail,password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('loginpage')
        except IntegrityError:
            messages.error(request, "Username already exists!")
            return redirect('signup_page')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip().lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('loginpage')  
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('loginpage')
