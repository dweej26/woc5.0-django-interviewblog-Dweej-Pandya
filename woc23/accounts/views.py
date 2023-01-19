from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse,path
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import OrderForm,CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def regis(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'YOU HAVE SUCCESSFULLY REGISTERED')
                return redirect('login')
        
        context={'form':form}
        return render(request, 'accounts/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = AuthenticationForm()
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR Password is Incorrect')
                return redirect('login')
        else:
            form = AuthenticationForm()
        context={'form':form}
        return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('first')

def welcome(request):
    return render(request, 'accounts/welcome.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def products(request):
    return render(request, 'accounts/products.html')

@login_required(login_url='login')
def customer(request):
    return render(request, 'accounts/customer.html')
