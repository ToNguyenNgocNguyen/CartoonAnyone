from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import authenticate
import os
from .models import *
from .forms import *
import math, random


# Create your views here.

def get_home(request):
    context = {}
    return render(request, "app/home.html", context)


def sent_otp(email):
    digits = "0123456789"
    OTP = ""
    for _ in range(4) :
        OTP += digits[math.floor(random.random() * 10)]

    send_mail(subject="OTP from Wibu United",
              message=f"Don't send it to anyone. Here is your OTP: {OTP}",
              from_email=os.environ.get('EMAIL_HOST_USER'),
              recipient_list=[email])
    
    return OTP


def get_signup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            OTP = sent_otp(email)
            request.session['OTP'] = OTP
            request.session['form_data'] = form.cleaned_data
            request.session.set_expiry(timezone.now() + timezone.timedelta(seconds=60))
            return redirect('otpverify')
            
        else:
            messages.info(request, form.errors)
    context = {"form": form}
    return render(request, "app/signup.html", context)


def resend_otp(request):
    form_data = request.session.get('form_data')
    if not form_data:
        messages.error(request, 'Your session is expired. Please sign up again!')
        return redirect('signup')
    
    email = form_data['email']
    OTP = sent_otp(email)
    request.session['OTP'] = OTP
    return redirect('otpverify')


def otp_verify(request):
    context = {}
    messages.warning(request, 'Your OTP only remains 60s!')
    if request.method == "POST":
        stored_otp = request.session.get('OTP')
        form_data = request.session.get('form_data')
        email = request.session.get('email')
        submitted_otp = ''.join(request.POST.get(f'otp{i}', '') for i in range(1, 5))
        if email:
            return redirect('reset')

        if not form_data:
            messages.error(request, 'Your session is expired. Please sign up again!')
            return redirect('signup')

        if stored_otp == submitted_otp:
            form = CustomUserCreationForm(form_data)
            if form.is_valid():
                form.save()
                del request.session['OTP']
                del request.session['form_data']
            return redirect('login')
    
    return render(request, "app/otpverify.html", context)


def get_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "User Name or Password is Incorrect!")
    context = {}
    return render(request, "app/login.html", context)


def get_logout(request):
    logout(request)
    return redirect("login")


def get_profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    context = {}
    return render(request, "app/profile.html", context)


def get_subcription(request):
    context = {}
    if request.method == "POST":
        request.session['code'] = request.POST.get('code')
        return redirect('payment')
    return render(request, "app/subscription.html", context)


def get_payment(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access the payment page.')
        return redirect('login')
    
    code = request.session.get('code')
    image_url = f'images/{code}.png'
    context = {'image_url':image_url}
    return render(request, "app/payment.html", context)


def get_startapp(request):
    context = {}
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to start app.')
        return redirect('login')
    
    if request.user.type_user.lower() == "normal":
        return redirect("https://colab.research.google.com/drive/1lYoscLxFgTUd78bYhWiYofiA8b0qrVFF?usp=sharing")
    
    elif request.user.type_user.lower() == "basic":
        return redirect("https://colab.research.google.com/drive/1lYoscLxFgTUd78bYhWiYofiA8b0qrVFF?usp=sharing")
    
    elif request.user.type_user.lower() == "standard":
        return redirect("https://colab.research.google.com/drive/1lYoscLxFgTUd78bYhWiYofiA8b0qrVFF?usp=sharing")
    
    elif request.user.type_user.lower() == "premium":
        return redirect("https://colab.research.google.com/drive/1lYoscLxFgTUd78bYhWiYofiA8b0qrVFF?usp=sharing")


def get_forgot(request):
    context = {}
    if request.method == "POST":    
        email = request.POST.get('email')
        OTP = sent_otp(email)
        request.session['OTP'] = OTP
        request.session['email'] = email
        request.session.set_expiry(timezone.now() + timezone.timedelta(seconds=60))
        return redirect('otpverify')
    return render(request, "app/forgot.html", context)


def get_reset(request):
    context = {}
    if request.method == "POST":    
        email = request.session.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request, "The two password fields didn’t match.")
            return render(request, "app/reset.html", context)
        else:
            user = CustomerUser.objects.get(username=username, email=email)
            if not user:
                messages.warning(request, "Your username and email is not in one user.")
                return render(request, "app/reset.html", context)
            
            user.set_password(password1)
            user.save()
            return redirect("login")
    return render(request, "app/reset.html", context)
