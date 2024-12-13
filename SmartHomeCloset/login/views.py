from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("Username or Password Invalid"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})
    

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, ("You have been logged out!"))
        return redirect('login')  # Redirect to login page after logout
    return redirect('login')  # Also redirect if someone tries to GET this URL
    

