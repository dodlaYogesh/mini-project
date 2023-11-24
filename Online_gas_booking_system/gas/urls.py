from django.urls import path
from .views import gas,login,book,faq,services
urlpatterns=[
    path('', gas),
    path('login/', login),
    path('book/', book),
    path('faq',faq),
    path('services',services),
]