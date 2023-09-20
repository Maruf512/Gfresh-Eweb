from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import make_password, check_password   # to make a hash password and to read that password
from .models import User

# Create your views here.

def get_data(get_data_by):
    data = []
    all_users = User.objects.all()        #read data from the model
    
    for items in all_users:
        if items.email == get_data_by:
            
            data.append(items.email)
            data.append(items.first_name)
            data.append(items.passwd)
        else:
            continue
    
    return data


def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def view(request):
    return render(request, 'view.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def login(request):

    # print(make_password("1212"))
    # print(check_password('1212','pbkdf2_sha256$600000$giYToBZw4wPEquRnsEtL3d$NRKJk/QdQBBCjaq2BuxiHW+J7jdPLMS8EKz68x1D4EE='))

    

    if request.method == "POST":
        login_data = request.POST.dict()
        emailAddress = login_data.get("email")
        password = login_data.get("passwd")
        
        if emailAddress != "" and password != "":
            checkpt = User.objects.filter(email=emailAddress)       # check if user email exists or not
            if checkpt:
                data = get_data(emailAddress)
                check_passwd = check_password(password, data[2])
                if check_passwd:
                    print("login successfull")
                    # change page
                    # to home page
                    return render(request, 'home.html')

            else:
                print("User dosent exist on database!")
                print("please register.")
                # send to register page
                return render(request, 'register.html')
        else:
            print("Empty Field detected!")

        return render(request, 'login.html')
    else:
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


def order_complete(request):
    return render(request, 'order-complete.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
