from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('signup/', views.get_signup, name='signup'),
    path('login/', views.get_login, name='login'),
    path('logout/', views.get_logout, name='logout'),
    path('profile/', views.get_profile, name='profile'),
    path('subscription/', views.get_subcription, name='subscription'),
    path('payment/', views.get_payment, name='payment'),
    path('startapp/', views.get_startapp, name='startapp'),
    path('otpverify/', views.otp_verify, name='otpverify'),
    path('resend/', views.resend_otp, name='resendotp'),
    path('forgot/', views.get_forgot, name='forgot'),
    path('reset/', views.get_reset, name='reset')
]
