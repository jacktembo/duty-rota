from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewUserForm
from django.contrib.auth.models import User
from dutyrota.utils import OneTimePassword
import random
from django.core.mail import send_mail


def generate_otp():
    """generating one time password"""
    start = 100000
    stop = 900000
    return random.randrange(start, stop)


def dashboard(request):
    """Dashboard where a user is redirected after they login"""
    return HttpResponse('welcome to the dashboard')


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
    """Login a user in"""
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
    """Changing user password"""
    if request.method != "POST":
        user = request.user
        form = PasswordChangeForm(user)
        return render(request, "password_change.html", {"form": form})
    else:
        user = request.user
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            """Keep a user logged in after Changing their password"""
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/dashboard')


def password_reset_confirm(request, email):
    """entering one time password sent

    Args:
        request ([type]): [description]
        email ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method != 'POST':
        return render(request, 'password_reset_confirm.html')
    else:
        otp = request.POST.get('otp', False)
        db_otps = OneTimePassword.objects.get(email=email)


def password_reset(request):
    if request.method != 'POST':
        return render(request, 'password_reset.html')
    else:
        try:
            email_address = request.POST.get('email', False)
            user = User.objects.get(email=email_address)
            otp_number = generate_otp()  # generated otp.
            # Create otp object.
            otp = OneTimePassword(user=user, otp=otp_number)
            otp.save()  # Save one time password to database.
            subject = 'Your One Time Password'
            message = f"Your one time password is {otp_number}"
            email_from = 'no-reply@jacktembo.com'
            recipient_list = [str(user.email)]
            send_mail(subject, message, email_from, recipient_list)
            return HttpResponseRedirect(reverse('password-reset-confirm', args=(email_address,)))

        except NameError:
            return HttpResponse('email not resgistered')
