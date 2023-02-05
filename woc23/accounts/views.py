from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,path,reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm,Com_Form,PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
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

@login_required(login_url='login')
def addentry(request):
    form=Com_Form();
    if request.method == 'POST':
        print(request.POST)
        form = Com_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'YOU HAVE SUCCESSFULLY ENTERED DETAILS')
            return redirect('home')
    context = {'form':form}
    return render(request, 'accounts/add.html',context)

@login_required(login_url='login')
def posts(request):
    return render(request,"posts.html",{price:200})

@method_decorator(login_required,name='dispatch')
class BlogView(ListView):
    model = Post
    template_name = "accounts/blog.html"
    
@method_decorator(login_required,name='dispatch')
class DetailView(DetailView):
    model = Post
    template_name = "accounts/blog1.html"
    
@method_decorator(login_required,name='dispatch')
class AddPostView(CreateView):
    model = Post
    form_class=PostForm
    template_name='accounts/create_post.html'
    
@method_decorator(login_required,name='dispatch')
class UpdatePostView(UpdateView):
    model = Post
    template_name='accounts/update_post.html'
    fields=['title','body']
    
@method_decorator(login_required,name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name='accounts/delete_post.html'
    success_url=reverse_lazy('posts')

@ login_required
def favourite_list(request):
    favourite_posts = request.user.favourites.all()
    return render(request,'accounts/book.html',{'favourite_posts':favourite_posts})


@ login_required
def favourite_add(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())