from django.contrib import admin

# Register your models here.

from .models import DialShape, Product, Category, SubCategory, Feature, UserWishlist, UserCart


admin.site.register(Product)

admin.site.register(DialShape)

admin.site.register(Category)

admin.site.register(SubCategory)

admin.site.register(Feature)

admin.site.register(UserWishlist)

admin.site.register(UserCart)