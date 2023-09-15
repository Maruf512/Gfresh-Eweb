from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html')


def view(request):
    return render(request, 'view.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def account(request):
    return render(request, 'account.html')


def profile_info(request):
    return render(request, 'profile-info.html')


def manage_address(request):
    return render(request, 'manage-address.html')


def change_password(request):
    return render(request, 'change-password.html')
