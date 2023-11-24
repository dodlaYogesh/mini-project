from django.db import models
# Create your models here.

class bookings(models.Model):
    customerName=models.CharField(max_length=30, null=False, blank=False)
    contactNumber=models.CharField(max_length=30, null=False, blank=False)
    quantity=models.IntegerField(default=14 , null=False, blank=False)

    def __str__(self):
        return self.customerName

