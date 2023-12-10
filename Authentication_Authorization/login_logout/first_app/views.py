from django.shortcuts import render, redirect
from .forms import RegisterForm, changeUserData
from django.contrib import messages
# Buitin module for authentication, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

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
        if request.method == 'POST':
            form = changeUserData(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request, 'Account updated succesfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = changeUserData(instance= request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')
    
    
def userlogout(request):
    logout(request)
    return redirect('home')


def passward_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
            
        return render(request, 'passwordChange.html', {'form': form})

    else:
        return redirect('login')


def passward_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
            
        return render(request, 'passwordChange.html', {'form': form})
    else:
        return redirect('login')
    
    
    # change password end


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = changeUserData(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request, 'Account updated succesfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = changeUserData()
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('signup')
