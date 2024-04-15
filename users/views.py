from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

def landingPage(request):
    
    context = {
        'title': 'Home',
        'user' : request.user,
    }
    return render(request, 'users/index.html', context)

def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        #user validation from here 
        auth = authenticate(request, username=username, password=password)
        if auth is not None:#sucessful login
            login(request,auth)
            return redirect('landing_page')
        else:
            error_message = "Login Failed! please check your usename and password"
            messages.error(request, error_message)

    context = {
        'title': 'Login',
    }
    return render(request, 'users/login.html', context)

def singupuser(request):
    context = {
        'title': 'Sing Up',
    }
    if request.method == 'POST':
        # firstname = request.POST['firstname']
        # print(firstname)
        # lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists."
            return render(request, 'login.html', {'error_message': error_message})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            messages.success(request, "Username has been created. You can Log in now.")
            return redirect('landing_page')

    return render(request, 'users/signup.html', context)

def aboutus(request):
    context = {
        'title': 'About us',
    }
    return render(request, 'users/AboutUs.html', context)

def logoutUser(request):
    logout(request)

    return render(request, 'users/index.html')




