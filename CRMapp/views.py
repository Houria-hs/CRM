from django.shortcuts import render , redirect
from django.contrib.auth import logout , login , authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Customer

# Create your views here.



# home view
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


# authentication system ( registration , login , logout)
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



































































