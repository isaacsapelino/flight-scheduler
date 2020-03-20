from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .forms import CreateUserForm

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            remember_me = request.POST.get('remember_me')
            if remember_me is not None:
                request.session.set_expiry(1209600)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect.')
                return redirect('/')

    return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('/')

def reg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/')

    context = {'form': form}
    return render(request, 'reg.html', context)

