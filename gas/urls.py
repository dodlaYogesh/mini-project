from django.urls import path
from .views import gas,login,book,faq,services,mybookings,contact,register_view
urlpatterns=[
    path('', gas),
    path('login/', login),
    path('book/', book),
    path('faq/',faq),
    path('services/',services),
    path('bookings/',mybookings),
    path('contact/',contact),
    path('register/',register_view),
]