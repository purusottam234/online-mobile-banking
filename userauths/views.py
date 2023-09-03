from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User

# Create your views here.

def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account was created successfully.')
            new_user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('index')
    if request.user.is_authenticated:
        messages.warning(request, f'Hey you are already logged in.')
        return redirect('index')


    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"userauths/signup.html",context)

def loginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in Successfully")
                return redirect('index')
            if request.user.is_authenticated:
                messages.warning(request, f'Hey you are already logged in.')
                return redirect('index')
            else:
                messages.warning(request, "Username or password doesn't exists")
                return redirect('sign_in')

        except:
            messages.warning(request,'User doesnot exists')
    return render(request, 'userauths/signin.html')


def logoutView(request):
    logout(request.user)
    messages.success(request, "You have successfully logout.")
    return redirect('index')
