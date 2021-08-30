from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm,ContectForm
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate,logout as auth_logout
from .models import Post,Contect
from django.contrib.auth.models import Group
import os
# Create your views here.

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.order_by('id').reverse()
    return render(request,'blog/home.html',{'posts':posts})


def deshboard(request):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()
        email = request.session.get('email')
        posts = Post.objects.filter(written_by=full_name)        
        gps = user.groups.all()
        return render(request,'blog/deshboard.html',{'posts':posts,'full_name':full_name,'groups':gps,'email':email})
    else:
        return HttpResponseRedirect('/login/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations !! You have become an Author.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def login(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=username,password=userpass)
                if user:
                    auth_login(request,user)
                    messages.success(request,'Logged in Successfully !!!')
                    return HttpResponseRedirect('/deshboard')
        else:
            form = LoginForm()
            messages.info(request,"Please Login First")
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/deshboard')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                written_by= form.cleaned_data['written_by']
                pst = Post(title=title, desc=desc,written_by=written_by)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/deshboard')
    else:
        return HttpResponseRedirect('/login/')

def contect(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContectForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Congratulations !! Your Message Successfully Submit ')
        else:
            form = ContectForm()
           
        return render(request,'blog/contect.html',{'form':form})
    return HttpResponseRedirect('/login')

def about(request):
    return render(request,'blog/about.html')



















def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')