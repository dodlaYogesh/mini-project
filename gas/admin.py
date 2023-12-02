from django.contrib import admin
from .models import bookings,UserProfile

# Register your models here.
admin.site.register(bookings)
admin.site.register(UserProfile)
