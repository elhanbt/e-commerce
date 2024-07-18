from django.contrib import admin

# Register your models here.

from .models import Otp, UserProfile, UserAddress

admin.site.register(UserProfile)

admin.site.register(UserAddress)

admin.site.register(Otp)
