from django.shortcuts import render , redirect
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm , AddRecordForm
from django.contrib import messages
from .models import Customer 



# home view + the login function
def home(request):
    customers = Customer.objects.all()
    # log in system
    if request.method == 'POST':
        loginform = AuthenticationForm(data = request.POST)
        if loginform.is_valid():
            login(request , loginform.get_user())
            messages.success(request , 'Welcome , you have been loged in!')
            return redirect('home')
    else:
        loginform= AuthenticationForm()
    return render(request , 'home.html' , {'loginform':loginform , 'customers':customers})


# authentication system ( registration , logout)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            login(request ,  form.save() )
            username = form.cleaned_data.get('username')
            messages.success(request , f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html' , { 'form':form })

def logout_view(request):
    logout(request)
    return redirect('home')

# CRUD operations on customer records
def customer_record(request , pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id = pk)
        return render(request , 'indv-record.html' , {'customer_record':customer_record})
    else:
        messages.warning( request , 'You must be logged in !')
        return redirect('home')

def Delete_record(request , pk):
    if request.user.is_authenticated:
        delete_record = Customer.objects.get(id=pk)
        delete_record.delete()
        messages.success(request , 'Record Deleted Successufully')
        return redirect('home')
    else:
        messages.warning( request , 'You must be logged !')
        return redirect('home')

def Add_record(request):
    add_record_form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if add_record_form.is_valid():
                add_record_form.save()
                messages.success(request , 'Record added successufuly!')
                return redirect('home')
            else:
                messages.success(request, "Please correct the errors below.")
        return render(request , 'add_record.html' , {"add_record_form":add_record_form})
    else:
        messages.success(request , 'You are not authorised for this page , please log In !')
        redirect('home')

def update_record(request , pk):
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id = pk)
        add_record_form = AddRecordForm(request.POST or None , instance = current_record )
        if add_record_form.is_valid():
            add_record_form.save()
            messages.success( request , 'Record updated !')
            return redirect('home')
        return render(request , 'update_record.html', {'add_record_form':add_record_form})
    else:
        messages.success(request , 'You are not authorised , please Sign-up or Log In !')
        return redirect('home')






















































