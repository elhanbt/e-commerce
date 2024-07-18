from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.response import Response
# from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Otp, UserAddress
from products.models import UserWishlist, UserCart
from django.urls import reverse
import random

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        phone = phone.replace(" ","")
        print(phone)
        if UserProfile.objects.filter(phone_number=phone).exists():
            otp = random.randint(1000, 9999)
            Otp.objects.create(otp_number=otp, phone=phone, isActive = True)
            return redirect('login_otp', phone_number = phone)
        else:
            return render(request, 'login.html', {'message':"Phone number not registered."})   
    return render(request, 'login.html')

def login_otp(request, phone_number):
    if request.method == 'POST':
        box1 = request.POST.get('box1')
        box2 = request.POST.get('box2')
        box3 = request.POST.get('box3')
        box4 = request.POST.get('box4')
        entered_otp = int(box1+box2+box3+box4)
        
        auth_otp = Otp.objects.filter(isActive = True, phone = phone_number).first()
        if auth_otp.otp_number == entered_otp:
            auth_user = UserProfile.objects.get(phone_number=auth_otp.phone)
            
            username = auth_user.username
            password = f"{auth_user.fname}@123"
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                print('hii')
                auth_otp.isActive = False
                auth_otp.save()
                return redirect('index')
        else:
            return render(request, 'login_otp.html', {'message':"Invalid OTP"})
    return render(request, 'login_otp.html')



def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        # print(gender) 
        phone = phone.replace(" ","")
        
        username = f"{phone}@{email}"
        password = f"{first_name}@123" 
        
        # if not UserProfile.objects.filter(email = email, phone_number = phone).exists():
        if not User.objects.filter(username=username):
            user = User.objects.create_user(username=username, password=password, first_name=first_name, email=email, last_name=last_name)
            
            UserProfile.objects.create(
                fname=first_name,
                lname=last_name,
                email=email,
                gender=gender,
                phone_number = phone,
                username = username,
                user = user,
            )
            
            return redirect('login')
        
        else:
            return render(request, 'signinform.html', {'message':"User already exists"})
        
        
              
    return render(request, 'signinform.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

def wishlist(request):
    products = UserWishlist.objects.filter(userprofile__username = request.user.username)
    
    context = {
       'wishlist': products,
       'count':len(products),
    }
    
    return render(request, 'wishlist.html', context=context)

# Veiws for Wishlist (creating, deleting and template view)
def deleteWishlist(request, value):
    product = UserWishlist.objects.get(id = value)
    if(product):
        product.delete()
    
    return redirect(reverse('wishlist'))

def addWishlist(request, value, category):
    product_id = value
    username = request.user.username
    user_id  = UserProfile.objects.get(username = username)
    if not (UserWishlist.objects.filter(userprofile__username = username, product = product_id).exists()):
        UserWishlist.objects.create(
            userprofile_id=user_id.id,
            product_id=product_id 
        )
    elif category != 'cart':
        item = UserWishlist.objects.get(userprofile__username = username, product=product_id)
        if item:
            item.delete()
            
    if category == 'index': 
        return redirect('index')
    elif category == 'cart':
        return redirect('cart')
    else:
        return redirect('search',value=category)
    


# Views for cart (creating, deleting and template view)
@api_view(['GET'])
# @renderer_classes([TemplateHTMLRenderer])
def cart(request):
    cart_items = UserCart.objects.filter(userprofile__username = request.user.username)
    address = UserAddress.objects.get(userprofile__user = request.user, isDefault = True)
    
    context = {
        'products':cart_items,
        'count':len(cart_items),
        'name':address.name,
        'city':address.city,
        'pin':address.pin_code
    }
    return render(request, 'cart.html', context=context)  

def addCart(request, id, name):
    
    username = request.user.username
    user_id = UserProfile.objects.get(username = username)
    if not UserCart.objects.filter(userprofile__username = username, product = id).exists():
        UserCart.objects.create(userprofile_id = user_id.id, product_id = id)
    if name == 'wishlist':  
        return redirect('wishlist')
    elif name == 'single':
        return redirect('singlepage', value = id)

def deleteCart(request, id):
    item = UserCart.objects.get(id = id)
    if item:
        item.delete()
    return redirect('cart')


def userAddress(request):
    user = request.user
    
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address_line = request.POST.get('address')
        pin_code = request.POST.get('pin')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        landmark = request.POST.get('landmark')
        type = request.POST.get('type')
        id = request.POST.get('id', None)
        
        if UserAddress.objects.filter(userprofile__user = request.user, isDefault = True).exists():
            isDefault = False
        else:
            isDefault = True
        
        user_id = UserProfile.objects.get(user=user)
        
        address, created =  UserAddress.objects.get_or_create(
            userprofile_id = user_id.id,
            
            id = id,
            # type = type,
            defaults={
                'address':address_line,
                'phone':phone,
                'pin_code':pin_code,
                'city':city,
                'district':district, 
                'state':state,
                'landmark':landmark,
                'isDefault':isDefault,
                'name' : name,
                'type': type
            }    
        )
        if not created:
            address.name = name
            address.address = address_line
            address.phone = phone
            address.pin_code = pin_code
            address.city = city
            address.district = district 
            address.state = state
            address.landmark = landmark
            address.type = type
            address.isDefault = isDefault
            address.userprofile_id = user_id.id
            address.save()
        return redirect('address')
        
    full_address = UserAddress.objects.filter(userprofile__username=user.username)
    # print(full_address)
    context = {
        'address':full_address
    }
    
    return render(request, 'address_page.html', context)

def deleteAddress(request, id):
    address = UserAddress.objects.get(id = id)
    if address:
        address.delete()
    addDefaultAddress(request)
    return redirect('address')


def addDefaultAddress(request):
    address = UserAddress.objects.filter(userprofile__user = request.user, isDefault = True).exists()
    addresses = UserAddress.objects.filter(userprofile__user = request.user).first()
    
    if not address:
        addresses.isDefault = True
        addresses.save()
    