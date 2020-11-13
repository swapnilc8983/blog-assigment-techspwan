from django.shortcuts import render, redirect
from blog.models import Blog 
from dashboard.forms import BlogForm
from django.contrib import messages



def home(request):
    blogs = Blog.objects.filter(status = "Publish").order_by('-id')
    return render (request, 'blogpage/home-page.html', { 'bloglist' : blogs })

def blog(request , slug):
    blogpage = Blog.objects.filter(slug=slug).first()
    contex = { 'blogpage' : blogpage}

    return render (request, 'blogpage/post-page.html', contex)

