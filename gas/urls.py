from django.urls import path
from .views import gas,login,book,faq,services,mybookings,contact,register,index,adminlogin,adminbookings,searching

urlpatterns=[
    path('home/', gas),
    path('login/', login),
    path('',index),
    path('book/', book),
    path('faq/',faq),
    path('services/',services),
    path('bookings/',mybookings),
    path('contact/',contact),
    path('register/',register),
    path('adminlogin/',adminlogin),
    path('adminbookings/',adminbookings),
    path('adminsearch/',searching,name="search"),
    
] 