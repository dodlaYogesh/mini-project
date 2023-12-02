from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import bookings,UserProfile
from django.contrib.auth import authenticate
from django.contrib import auth

#from .forms import bookingForm
# Create your views here.
def gas(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def services(request):
    return render(request,'services.html')

def mybookings(request):
    data=bookings.objects.all()
    return render(request,'bookings.html',{'objects':data})

def book(request):
    if request.method =='POST':
        custName=request.POST['customerName']
        contact=request.POST['contactNumber']
        gastype=request.POST['gasType']
        quantity=request.POST['quantity']
        adding_data=bookings(customerName=custName,contactNumber=contact,gastype=gastype,quantity=quantity)
        adding_data.save()
    return render(request,'book.html',{})

'''def formss(request):
    if request.method == 'POST':
        form=bookingForm(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('/')

    else:
        form=bookingForm
    return render(request,'form.html',{'form':form}) '''

from django.contrib import messages   

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # type: ignore
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Invalid username or password.')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Basic password validation
        if password == confirm_password:
            # In a real application, hash the password and save to the database
            # For simplicity, this example stores the password in plain text
            UserProfile.objects.create(username=username, password=password)

            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'registration.html')



