from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth.models import User


"""
The function below is a view for students to create an account. First, we display
the blank form. After the user fills in correct registration information,
the program generates their unique id.
"""


def dashboard(request):
    return HttpResponse('welcom to the dashboard')


def register(request):
    """"Registering users in the system"""
    if request.method != 'POST':
        form = NewUserForm()
    else:
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            form = NewUserForm()
            return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("today-rota"))


def login_view(request):
    if request.method != "POST":
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return HttpResponse("something went wrong.")


def change_password(request):
    if request.method != "POST":
        user = request.user
        form = PasswordChangeForm(user)
        return render(request, "password_change.html", {"form": form})
    else:
        user = request.user
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/dashboard')
