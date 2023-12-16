from django.contrib import admin
from .models import bookings,registerUser,contactus,searchings

# Register your models here.
admin.site.register(bookings)
admin.site.register(registerUser)
admin.site.register(contactus)
admin.site.register(searchings)
