from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password   # to make a hash password and to read that password
from .models import User

# Create your views here.
print(make_password("1212"))
print(check_password('1212','pbkdf2_sha256$600000$giYToBZw4wPEquRnsEtL3d$NRKJk/QdQBBCjaq2BuxiHW+J7jdPLMS8EKz68x1D4EE='))

def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def view(request):
    return render(request, 'view.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def login(request):
    all_users = User.objects.all
    return render(request, 'test.html', {'users':all_users})


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


def order_complete(request):
    return render(request, 'order-complete.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
