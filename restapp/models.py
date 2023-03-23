from django.db import models
from restapp.manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    username  = models.CharField(max_length=255,default="")
    email 		= models.EmailField(_('email'),unique=True)
    password    = models.CharField(max_length=255,default="")
    is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
    is_active 	= models.BooleanField(default=True,
		help_text='Designates whether this user should be treated as active.\
		Unselect this instead of deleting accounts.')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at =  models.DateTimeField(auto_now=True)
    
    

    USERNAME_FIELD 	='email'
    
    objects 		= CustomUserManager()
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Store(models.Model):
  userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  store_name=models.CharField(max_length=255,null=True,blank=True)
  code=models.CharField(max_length=255,null=True,blank=True)
  token=models.CharField(max_length=255,blank=True,null=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)


class Campaign(models.Model):
  userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  Influencerid=models.ForeignKey("Influencer",on_delete=models.CASCADE,null=True)
  campaign_name=models.CharField(max_length=255,default="")
  product_name=models.CharField(max_length=255,default="")
  influencer_name=models.CharField(max_length=255,default="")
  coupon=models.CharField(max_length=255,default="")
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)


class Influencer(models.Model):
  userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  username  = models.CharField(max_length=255,default="")
  email 		= models.EmailField(_('email'),unique=True)
  password    = models.CharField(max_length=255,default="")
  is_staff 	= models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
  is_active 	= models.BooleanField(default=True,
  help_text='Designates whether this user should be treated as active.\
  Unselect this instead of deleting accounts.')
  created_at = models.DateTimeField(auto_now_add=True,null=True)
  updated_at =  models.DateTimeField(auto_now=True)
  country  = models.CharField(max_length=255,default="")
  