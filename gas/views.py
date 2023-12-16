from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import bookings,contactus,registerUser,searchings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
#from .forms import bookingForm
# Create your views here.
def gas(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')

def contact(request):
    if request.method =='POST':
       
        cname=request.POST['name']
        mail=request.POST['email']
        msg=request.POST['message']
        adding_data=contactus(name=cname,email=mail,message=msg)
        adding_data.save()
        return redirect('/home')
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def services(request):
    return render(request,'services.html')



def mybookings(request):
     data=bookings.objects.all()
     return render(request,'bookings.html',{'objects':data})

def adminbookings(request):
    data=bookings.objects.all()
    return render(request,'adminview.html',{'objects':data})

def book(request):
    if request.method =='POST':
        custName=request.POST['customerName']
        contact=request.POST['contactNumber']
        gastype=request.POST['gasType']
        quantity=request.POST['quantity']
        address=request.POST['addr']
        adding_data=bookings(customerName=custName,contactNumber=contact,address=address,gastype=gastype,quantity=quantity)
        adding_data.save()
        return redirect('/home')
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
    return render(request,'login.html')

'''def register_view(request):
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

    return render(request, 'registration.html')'''

def register(request):
     if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # In a real application, hash the password and save to the database
            # For simplicity, this example stores the password in plain text
            User=registerUser(username=username, password=password,email=email,conformpassword=confirm_password)
            User.save()
            messages.success(request, 'Registration successful!')
            return redirect('/login')
     return render(request,'registration.html')

def register1(request):
     if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # In a real application, hash the password and save to the database
            # For simplicity, this example stores the password in plain text
            user=User.objects.create_user(username=username, password=password,email=email)
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('/login')
     return render(request,'registration.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            
            #messages.success(request, 'Login successful!')
            return redirect('/adminbookings')  # Redirect to the home page or any other desired page
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'adminlogin.html')

'''def searching(request):
    if request.method =='POST':
        type= request.POST.get('select')
        search=request.POST['search']
        sdata=searchings(selectfields=type,search=search)
        sdata.save()
        return redirect('/adminfetch')
    return render(request,'search.html',{})'''
    

def searching(request):
    se=request.POST['search']
    data=bookings.objects.filter(address__icontains=se)
    data1=bookings.objects.filter(customerName__icontains=se)
    data2=bookings.objects.filter(gastype__icontains=se)
    
    return render(request,'search.html',{'object':data,'object1':data1,'object2':data2}) 


   
    
'''def fetching(request):
        rows=searchings.objects.all().count()
        type=searchings.objects.values('selectfields')[rows-2:rows-1]
        search=searchings.objects.values('search')[rows-2:rows-1]
        
        if type=="customerName":
             data=bookings.objects.filter(customerName=search)
        elif type=="contactNumber":
             data=bookings.objects.filter(contactNumber=search)
        elif type=="gastype":
             data=bookings.objects.filter(gastype=search)
        elif type=="quantity":
             data=bookings.objects.filter(quantity=search)
        elif type=="address":
             data=bookings.objects.filter(address=search)
        else:
             return HttpResponse('Not found!')
        return render(request,'fetchdata.html',{'object':data})'''
    
    
   