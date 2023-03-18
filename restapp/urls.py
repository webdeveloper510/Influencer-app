from django.urls import path
from restapp.views.SignupView import *
from restapp.views.LoginView import *
from restapp.views.ShopifyView import *
from restapp.views.ProductView import *
from restapp.views.CouponView import *
from restapp.views.InfluencerView import *
from restapp.views.CampaignView import *
from restapp.views.ModashView import *


urlpatterns = [
  #login/Register url
  path("register",Register.as_view(),name="register"),
  path("login",Login.as_view(),name="login"),
  path('password-reset/', PasswordResetView.as_view(),name="password-reset"),
  path('reset-password/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(),name="reset-password"),
  
  #shopifyapi url
  path("product",ProductList.as_view(),name="product"),
  path("createproduct",CreateProduct.as_view(),name="createproduct"),
  path("pricerule",CreateCoupon.as_view(),name="pricerule"),
  path("discount",DiscountCoupon.as_view(),name="discount"),
  path("coupon",CouponList.as_view(),name="coupon"),
  path("install/",InstallView.as_view(),name="install"),
  path("auth/",AuthView.as_view(),name="auth"),


  #Influencer url
  path('Influencer-list/', InfluencerList.as_view(),name="Influencer-list"),
  path('campaign/',CreateCampaign.as_view(),name="campaign"),
  
  
  #Modash url
  path('youtuber/',YoutubeFollower.as_view(),name="youtuber"),
  path('instagram/',InstagramFollower.as_view(),name="instagram"),

]