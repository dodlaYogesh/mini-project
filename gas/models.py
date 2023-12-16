from django.db import models
# Create your models here.

class bookings(models.Model):
    customerName=models.CharField(max_length=30, null=False, blank=False)
    contactNumber=models.CharField(max_length=30, null=False, blank=False)
    gastype=models.CharField(max_length=30, null=False, blank=False)
    quantity=models.IntegerField(default=14 , null=False, blank=False)
    address=models.TextField()

    def __str__(self):
        return self.customerName

class registerUser(models.Model):
    username = models.CharField(max_length=50)
    email=models.EmailField()
    password = models.CharField(max_length=50)
    conformpassword=models.CharField(max_length=50)
    def __str__(self):
        return self.username


class contactus(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
    
class searchings(models.Model):
    selectfields=models.CharField(max_length=30)
    search=models.CharField(max_length=40)
    def __str__(self):
        return self.search