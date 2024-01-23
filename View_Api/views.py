from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password   # to make a hash password and to read that password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# =======================================================
# ========== Additional Methods =========================
# =======================================================
def get_user_data(get_data_by):
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


# =======================================================
# ========== Home Section ===============================
# =======================================================
def home(request):
    if request.user.is_authenticated:
        print("Authenticated user")
        logged_in_user = request.user
    else:
        logged_in_user = "Login/Register"
        print("non authenticated")
    return render(request, 'home.html', {'user_data':logged_in_user})


# =======================================================
# ========== Shop Section ===============================
# =======================================================
def shop(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        print("Authenticated user")
    else:
        logged_in_user = "Login/Register"
        print("non authenticated")
    print("Shop")
    return render(request, 'shop.html', {'user_data':logged_in_user})


# =======================================================
# ========== View Section ===============================
# =======================================================
def view(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        print("Authenticated user")
    else:
        logged_in_user = "Login/Register"
        print("non authenticated")
    print("Shop")
    return render(request, 'view.html', {'user_data':logged_in_user})


def wishlist(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        print("Authenticated user")
    else:
        logged_in_user = "Login/Register"
        print("non authenticated")
    print("Shop")
    return render(request, 'wishlist.html', {'user_data':logged_in_user})


# =======================================================
# ========== Login Section ==============================
# =======================================================
def Login(request):
    if request.method == "POST":
        login_data = request.POST.dict()                            # [ GET ALL THE INPUT FIELDS DATA ]
        username = login_data.get("username")
        emailAddress = login_data.get("email")
        password = login_data.get("passwd")

        user = authenticate(request, username=username, email=emailAddress, password=password)

        if user is not None:
            print("redirect to a success page")
            login(request, user)
            return account(request)
        
        else:
            print("Login failed")
            return render(request, 'login.html')






        # if emailAddress != "" and password != "":
        #     checkpt = User.objects.filter(email=emailAddress)       # check if user email exists or not
        #     if checkpt:
        #         data = get_user_data(emailAddress)
        #         check_passwd = check_password(password, data[2])
        #         user = authenticate(request)
        #         if check_passwd:
        #             print("login successfull")
        #             # change page
        #             # to home page
        #             return render(request, 'home.html')
        #         else:
        #             print("Wrong Password")
        #     else:
        #         print("User dosent exist on database!")
        #         print("please register.")
        #         # send to register page
        #         return render(request, 'register.html')
        # else:
        #     print("Empty Field detected!")
        # return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# =======================================================
# ========== Register Section ===========================
# =======================================================
def register(request):
    if request.method == "POST":
        # get all data from form
        register_data = request.POST.dict()
        full_name = register_data.get("first_name")
        email_address = register_data.get("email")
        passward = register_data.get("Password")
        check_passwd = register_data.get("ck_password")
        check_terms = register_data.get("check_terms")


        user = User.objects.create_user(username=full_name, email=email_address, password=passward)
        user.save()


        # handel logic system
        # if full_name != "" and email_address != "" and passward != "" and check_passwd != "":
        #     checkpt = User.objects.filter(email=email_address)       # check if user email exists or not
        #     if checkpt != '':
        #         # check if the password matches with the confirm password field
        #         if passward == check_passwd:
        #             # check terms and condition's
        #             # generate hash password
        #             Hash_passward = make_password(passward)
        #             if check_terms == "on":
        #                 # push all data to database
        #                 user = User.objects.create_user(username=full_name, email=email_address, password=Hash_passward)
        #                 user.save()
        #                 return render(request, 'login.html')
        #             else:
        #                 print("Do you agry to our terms and conditions?")
        #         else:
        #             print("password didnt match!")
        #     else:
        #         print("This email already exists!")
        #         print("Try to login!")
        #         print("reset password if needed")
        #         return render(request, 'login.html')
        # else:
        #     print("Empty Fields Detected!")

        return render(request, 'register.html')
    
    return render(request, 'register.html')



# =======================================================
# ========== Account Section ============================
# =======================================================
def account(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'account.html')


# =======================================================
# ========== Profile-Info Section =======================
# =======================================================
def profile_info(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'profile-info.html')


# =======================================================
# ========== Manage-Address Section =====================
# =======================================================
def manage_address(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'manage-address.html')


# =======================================================
# ========== Change-password Section ====================
# =======================================================
def change_password(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'change-password.html')


# =======================================================
# ========== Order-complete Section =====================
# =======================================================
def order_complete(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'order-complete.html')


# =======================================================
# ========== Cart Section ===============================
# =======================================================
def cart(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'cart.html')


# =======================================================
# ========== Checkout Section ===========================
# =======================================================
def checkout(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'checkout.html')


# =======================================================
# ========== Logout Section ===============================
# =======================================================
def Logout(request):
    logout(request)
    if request.user.is_authenticated:
        logged_in_user = request.user
        print("Authenticated user")
    else:
        logged_in_user = "Login/Register"
        print("non authenticated")
    return render(request, 'home.html', {'user_data':logged_in_user})


# =======================================================
# ========== Test Section ===============================
# =======================================================
def test(request):
    if request.user.is_authenticated:
        print("Authenticated user")
    else:
        print("non authenticated")
    return render(request, 'test.html')

