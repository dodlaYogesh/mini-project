from django.shortcuts import render
from django.http import HttpResponse
from .models import bookings

# Create your views here.
def gas(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def faq(request):
    return render(request,'faq.html')

def services(request):
    return render(request,'services.html')

def book(request):
    if request.method =='POST':
        custName=request.POST['customerName']
        contact=request.POST['contactNumber']
        quantity=request.POST['quantity']

        adding_data=bookings(customerName=custName,contactNumber=contact,quantity=quantity)
        adding_data.save()

    return render(request,'book.html',{})




