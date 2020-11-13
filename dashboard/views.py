from django.shortcuts import render, redirect
from blog.models import Blog
from dashboard.forms import BlogForm, CreateUserForm
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    contex = {'form': form}
    return render (request, 'dashboard/register.html', contex)

def Login(request):
    if request.user.is_authenticated:
        return redirect('bloglist')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bloglist')
            else:
                messages.info(request, 'Username OR Password Wrong')
    return render (request, 'dashboard/login.html')

@login_required(login_url = 'login')
def Logout(request):

    logout(request)

    return redirect('login')

@login_required(login_url = 'login')
def index(request):
    # Post Count
    # contex = { }
    return render (request, 'dashboard/dashboard.html')


@login_required(login_url = 'login')
def BlogList(request):
    # Query For Database (Blog)
    bloglist = Blog.objects.all().order_by('-id')


    contex = { 'Blogs': bloglist }
    return render (request, 'dashboard/dashboard.html', contex )


@login_required(login_url = 'login')
def Createblog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    contex = {'form': form }

    return render (request, 'dashboard/addblog.html', contex )


@login_required(login_url = 'login')
def Updateblog(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = BlogForm(instance = blog)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES, instance = blog)
        if form.is_valid():
            form.save()
    contex = {'form': form, 'blog': blog }

    return render (request, 'dashboard/update-blog.html', contex )


@login_required(login_url = 'login')
def Deleteblog(request,slug):
    # Delete Blog
    blog = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('bloglist')
    contex = {'blog': blog}
    return render (request, 'dashboard/delete-blog.html',contex )