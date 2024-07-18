from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from products.models import UserWishlist
from common.models  import BaseModel

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]

ADDRESS_TYPE = [
    ('home','Home'),
    ('office','Office'),
    ('other', 'Other')
]


class UserProfile(BaseModel):
    fname = models.CharField(max_length=200, verbose_name='First Name')
    lname = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.EmailField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    

    class Meta:
        db_table = 'userprofile_userprofile'
        ordering = ('fname'),



    def __str__(self):
        return f"{self.fname} {self.lname}"
    

class Otp(BaseModel):
    otp_number = models.IntegerField()
    phone = models.CharField(max_length=10)
    isActive = models.BooleanField(default=False)
    # resend_otp = models.BooleanField(default=False)

    class Meta:
        db_table = 'otp_users'
        ordering = ('-created_on',)

    def __str__(self):
        return str(self.otp_number)
    
    
class UserAddress(BaseModel):
    name = models.CharField(max_length=256)
    address = models.TextField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    district = models.CharField(max_length=256, blank=True, null=True)
    state = models.CharField(max_length=256, blank=True, null=True)
    landmark = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=100, choices=ADDRESS_TYPE)
    isDefault = models.BooleanField(default=False)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        db_table = 'useraddress_users'
        ordering = ('name',)
        verbose_name_plural = 'User adresses'
    
    def __str__(self):
        return f"{self.name}: {self.pin_code}"