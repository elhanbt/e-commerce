from django.db import models
from django import forms

from common.models import BaseModel
from users.models import UserProfile
# Create your models here.

class DialShape(BaseModel):
    shape = models.CharField(max_length=100)
    watchcategory = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.shape
  
    
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'category_products'
        verbose_name_plural = 'Categories'
        ordering = ('category_name',)
    
    def __str__(self):
        return self.category_name


class SubCategory(BaseModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'subcategory_products'
        verbose_name_plural = 'Subcategories'
        ordering = ('name',)
        
    def __str__(self):
        return f"{self.category}:{self.name}"


class Feature(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

"""Model containing product details"""
class Product(BaseModel):
    name = models.CharField(max_length=255)
    original_price = models.FloatField(blank=True, null=True)
    discount_price = models.FloatField(null=True, blank=True)
    rating = models.FloatField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='.\products', blank=True, null=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    top_product = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(blank=True, null=True)
    package_contents = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'product_products'
        ordering = ('category',)

    def __str__(self):
        return f"{self.category}: {self.name} "

    def save(self, *args, **kwargs):
        self.discount_price = self.original_price - (self.original_price * self.discount/100)
        super(Product, self).save(*args, **kwargs)
        

class UserWishlist(BaseModel):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    # class Meta:
    #     db_table = 'userwishlist_products'
        # ordering = ('userprofile',)
        
    def __str__(self):
        return f"{self.userprofile}'s wishlist"
    
    
class UserCart(BaseModel):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'userwishlist_products'
        
    def __str__(self):
        return f"{self.userprofile}'s cart"