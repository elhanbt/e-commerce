from django.contrib import admin
from django.urls import path, include

from .views import login_view, login_otp, registration, wishlist, deleteWishlist, addWishlist, logout_view, cart, addCart
from .views import deleteCart, userAddress, deleteAddress
urlpatterns = [
    path('', login_view, name='login'),
    path('login_otp/<str:phone_number>', login_otp, name='login_otp'),
    path('logut', logout_view, name='logout'),
    path('signinform', registration, name='signinform'),
    path('wishlist', wishlist, name='wishlist'),
    path('delete/<str:value>', deleteWishlist, name='delete_item'),
    path('add/<str:value>/<str:category>', addWishlist, name='add_item'),
    path('cart', cart, name='cart'),
    path('addcart/<str:id>/<str:name>', addCart, name='addtocart'),
    path('deletecart/<str:id>', deleteCart, name='removefromcart'),
    path('address', userAddress, name='address'),
    path('del_address/<str:id>', deleteAddress, name='delete_address')

]