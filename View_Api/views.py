from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password   # to make a hash password and to read that password
from .models import User


# =======================================================
# ========== Additional Veriabl =========================
# =======================================================
logged_in_user = "Login/Register"


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
    return render(request, 'home.html', {'user_data':logged_in_user})


# =======================================================
# ========== Shop Section ===============================
# =======================================================
def shop(request):
    print("Shop")
    return render(request, 'shop.html')


# =======================================================
# ========== View Section ===============================
# =======================================================
def view(request):
    return render(request, 'view.html')


def wishlist(request):
    return render(request, 'wishlist.html')


# =======================================================
# ========== Login Section ==============================
# =======================================================
def login(request):
    if request.method == "POST":
        login_data = request.POST.dict()
        emailAddress = login_data.get("email")
        password = login_data.get("passwd")
        if emailAddress != "" and password != "":
            checkpt = User.objects.filter(email=emailAddress)       # check if user email exists or not
            if checkpt:
                data = get_user_data(emailAddress)
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
        # handel logic system
        if full_name != "" and email_address != "" and passward != "" and check_passwd != "":
            checkpt = User.objects.filter(email=email_address)       # check if user email exists or not
            if checkpt != '':
                # check if the password matches with the confirm password field
                if passward == check_passwd:
                    # check terms and condition's
                    # generate hash password
                    Hash_passward = make_password(passward)
                    if check_terms == "on":
                        # push all data to database
                        user = User(first_name=full_name, email=email_address, passwd=Hash_passward)
                        user.save()
                        return render(request, 'login.html')
                    else:
                        print("Do you agry to our terms and conditions?")
                else:
                    print("password didnt match!")
            else:
                print("This email already exists!")
                print("Try to login!")
                print("reset password if needed")
                return render(request, 'login.html')
        else:
            print("Empty Fields Detected!")

        return render(request, 'register.html')
    
    return render(request, 'register.html')



# =======================================================
# ========== Account Section ============================
# =======================================================
def account(request):
    return render(request, 'account.html')


# =======================================================
# ========== Profile-Info Section =======================
# =======================================================
def profile_info(request):
    return render(request, 'profile-info.html')


# =======================================================
# ========== Manage-Address Section =====================
# =======================================================
def manage_address(request):
    return render(request, 'manage-address.html')


# =======================================================
# ========== Change-password Section ====================
# =======================================================
def change_password(request):
    return render(request, 'change-password.html')


# =======================================================
# ========== Order-complete Section =====================
# =======================================================
def order_complete(request):
    return render(request, 'order-complete.html')


# =======================================================
# ========== Cart Section ===============================
# =======================================================
def cart(request):
    return render(request, 'cart.html')


# =======================================================
# ========== Checkout Section ===========================
# =======================================================
def checkout(request):
    return render(request, 'checkout.html')
