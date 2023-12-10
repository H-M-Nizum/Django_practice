from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Buitin module for authentication, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account create succesfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']
                
                # check database contain user or not
                user = authenticate(username = name, password = userpassword)
                
                if user is not None:
                    login(request, user)
                    return redirect('profile')
            
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form':form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')
    
def userlogout(request):
    logout(request)
    return redirect('home')